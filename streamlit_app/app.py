import os
import sys
import io
from datetime import datetime
import requests

# ✅ Add 'project' directory to sys.path
current_file_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_file_dir, '..'))
sys.path.insert(0, project_dir)

import streamlit as st
from app.clustering_pipeline import clustering_pipeline
from app.visualization import plot_cluster_pca, plot_attendance_vs_score, plot_score_dist
import pandas as pd
import matplotlib.pyplot as plt

print("sys.path:", sys.path)
print("Listing project dir:", os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))

st.set_page_config(page_title="Student Dropout Risk App", layout = "wide")


st.markdown("""
<style>
/* --- Page Background (Dark Gradient, not Black) --- */
html, body, .appview-container .main {
    background: linear-gradient(135deg, #1f2933, #2b3644, #3a4454);
    color: #f0f2f6;
}

/* --- Layout Padding --- */
.appview-container .main .block-container {
    padding: 2rem 3rem;
}

/* --- Headings --- */
h1, h2, h3, h4 {
    color: #ffffff;
    font-weight: 700;
}
h1 {
    font-size: 2.4rem;
    margin-bottom: 0.8rem;
    text-shadow: 2px 2px 6px rgba(0, 217, 255, 0.7);
}
h3 {
    font-size: 1.4rem;
    color: #cbd5e1;
}

/* --- Markdown Styling --- */
.stMarkdown p {
    color: #e5e7eb;
    font-size: 1.05rem;
    line-height: 1.6;
}

/* --- Info Boxes (st.info, st.success etc) --- */
.stAlert {
    background-color: rgba(255, 255, 255, 0.05);
    border-left: 5px solid #00bcd4;
    border-radius: 10px;
    padding: 1rem;
    color: #f1f1f1;
}

/* --- Expander --- */
details {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1.2rem;
}
summary {
    font-weight: 600;
    font-size: 1.1rem;
    color: #f8f9fa;
}

/* --- File Uploader --- */
.stFileUploader {
    background-color: rgba(255,255,255,0.03);
    border: 1px dashed #6ec6ff;
    padding: 1rem;
    border-radius: 10px;
}
.stFileUploader label {
    color: #cce7ff;
    font-weight: bold;
}

/* --- Buttons --- */
.stDownloadButton > button {
    background-image: linear-gradient(to right, #00bcd4, #26c6da);
    color: white;
    font-weight: 600;
    padding: 0.6rem 1.2rem;
    font-size: 1rem;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    margin-top: 0.5rem;
    transition: 0.3s ease-in-out;
}
.stDownloadButton > button:hover {
    background-image: linear-gradient(to right, #e53935, #b71c1c);
    color: white !important;
    transform: scale(1.05);
}

/* --- DataFrame Table --- */
.stDataFrame {
    background-color: rgba(255,255,255,0.03);
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* --- Plots, Charts, Images --- */
.stPlotlyChart, .stImage, .stAltairChart, .stPyplot {
    background-color: rgba(255,255,255,0.04);
    padding: 1rem;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Streamlit app for Student Dropout Risk & Behavior Clustering


st.title("📚 Student Dropout Risk & Behavior Clustering")

st.info("👉 Upload your student CSV to detect dropout risks using AI-based clustering. See performance patterns, visualize behavior, and download insights.")

st.markdown("### 📘 How This App Works")
with st.expander("🧠 View Explanation", expanded=False):
    st.markdown("""
    This tool helps identify students at risk of dropping out by analyzing their academic and participation data using **unsupervised machine learning (KMeans clustering)**.

    ### 🔎 How It Works:
    - Upload your student CSV file containing quiz scores, attendance, GPA, and more or download sample CSV provided.
    - The app cleans the data, applies feature engineering, and uses **PCA** for dimensionality reduction.
    - Then it applies KMeans to group students into **5 clusters** based on risk levels.

    ### 🧠 Cluster Labels:
    - 🟥 **High Risk**: Urgent intervention needed. Low GPA, poor attendance, and missing assignments.
    - 🟧 **Moderate Risk**: Weak performance in some areas — monitor closely.
    - 🟨 **Mild Risk**: Average, may need support to improve.
    - 🟩 **Low Risk**: Consistent performance with minor dips.
    - 🟦 **No Risk**: Excellent academic and behavioral performance.""")

    st.markdown("""### 📥 Sample CSV template""")
    st.info("""If you're not sure how your file should look, download a ready-to-use template:
    """)
    
    # Download button for sample CSV
    # st.info("👉 Don't have a file? Download the template below.")

    file_path = os.path.join(os.path.dirname(__file__), 'data', 'student_template.csv')
    with open(file_path, "rb") as f:
        st.download_button(
            label= "⬇️ Download CSV Template",
            data = f,
            file_name="student_template.csv",
            mime="text/csv"
    )



uploaded_file = st.file_uploader("Upload Your csv here", type=["csv"])

REQUIRED_COLUMNS = [
    'student_id', 'name', 'age', 'gender',
    'quiz1_marks', 'quiz2_marks', 'quiz3_marks',
    'total_assignments', 'assignments_submitted',
    'midterm_marks', 'final_marks',
    'previous_gpa',
    'total_lectures', 'lectures_attended',
    'total_lab_sessions', 'labs_attended'
]


def fig_to_png_bytes(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png', bbox_inches = 'tight')
    buf.seek(0)
    return buf

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_cols:
        st.error(f"❌ Missing required columns: {', '.join(missing_cols)}")
        st.stop()

    st.success("✅ File uploaded successfully! Analyzing student performance...")


    ## For FastAPI 

    # files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}

    # response = requests.post("http://127.0.0.1:8000/predict/", files=files)

    # if response.status_code == 200:
    #     result = response.json()
    #     if result.get("status") == "success":
    #         clustered_df = pd.DataFrame(result["data"])
    #         st.write(clustered_df.head())
    #     else:
    #         st.error(f"API Error: {result.get('message')}")
    # else:
    #     st.error(f"API call failed with status code {response.status_code}")

    ## Direct Streamlit approach

    clustered_df = clustering_pipeline(df, visualize=False)

    # Show key metrics
    st.subheader("🔍 Cluster Summary")
    st.markdown("Each student is grouped into a cluster based on academic performance and participation. This helps identify who may be at risk of dropping out.")

    st.write(clustered_df['risk_label'].value_counts().rename_axis("Risk Level").reset_index(name="Students"))
    
    # st.bar_chart(risk_counts.set_index("Risk Level"))


    # Show dataframe
    st.subheader("📋 Clustered Data Preview")
    st.dataframe(clustered_df.head())

    # Download button
    csv = clustered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download Clustered Report CSV",
        data=csv, 
        file_name=f"clustered_output_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv", 
        mime='text/csv'
        )


    st.subheader("📊 Visualizations")
    st.markdown("##### These visualizations help teachers understand student group patterns and highlight performance gaps.")


    # PCA Scatter
    st.markdown("### 🎯 PCA Cluster Visualization")
    st.info("This scatter plot shows how students are grouped based on their academic performance and participation. Each color represents a different risk cluster.")
    
    fig1 = plot_cluster_pca(clustered_df)
    st.pyplot(fig1)
    png1 = fig_to_png_bytes(fig1)
    st.download_button(label= "📥 Download PCA Plot as PNG", data= png1, file_name="pca_plot.png", mime="image/png")

    st.markdown("### 📈 Attendance vs Score")
    st.info("This scatter plot shows the relationship between attendance percentage and total score. It helps identify students who may be at risk due to low attendance or performance.")
    fig2 = plot_attendance_vs_score(clustered_df)
    st.pyplot(fig2)
    png2 = fig_to_png_bytes(fig2)
    st.download_button(label = "📥 Download Attendance vs Score Plot", data = png2, file_name='attendance_vs_score.png', mime= 'image/png')

    st.markdown("### 📊 Score Distribution")
    st.info("This histogram shows the distribution of total scores across all students. It helps visualize overall performance trends.")
    fig3 = plot_score_dist(clustered_df)
    st.pyplot(fig3)
    png3 = fig_to_png_bytes(fig3)
    st.download_button(label = "📥 Download Score Distribution Plot", data = png3, file_name='score_distribution.png', mime= 'image/png')

st.markdown(
    """
    <style>
    /* Gradient line separator */
    .footer-separator {
        height: 3px;
        width: 100%;
        background: linear-gradient(to right, #00c6ff, #0072ff);
        margin: 2rem 0 1rem 0;
        border-radius: 5px;
    }

    /* Footer Styling */
    .footer-text {
        text-align: center;
        font-size: 0.95rem;
        color: #cccccc;
    }

    .footer-text a {
        color: #91cfff;
        text-decoration: none;
        margin: 0 8px;
        position: relative;
        transition: all 0.3s ease-in-out;
    }

    /* Glow on hover */
    .footer-text a:hover {
        color: #ffffff;
        text-shadow: 0 0 8px #00e6ff, 0 0 12px #00c6ff;
    }
    </style>

    <div class="footer-separator"></div>

    <div class="footer-text">
        An AI-driven student analysis tool by <strong>Muhammad Khubaib Ahmad</strong>
    </strong><br>
        <a href="https://github.com/Khubaib8281" target="_blank">🔗 GitHub</a> |
        <a href="https://www.linkedin.com/in/muhammad-khubaib-ahmad-" target="_blank">💼 LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)


# streamlit run project/streamlit_app/app.py