
# 🎓 Student Dropout Risk & Behavior Clustering 🚀

A production-ready Machine Learning web app that identifies student dropout risks based on academic performance, attendance, and participation using **unsupervised clustering techniques**.

This app enabl
# 🎓 Student Dropout Risk & Behavior Clustering 🚀

A production-ready Machine Learning web app that identifies student dropout risks based on academic performance, attendance, and participation using **unsupervised clustering techniques**.

This app enables teachers or academic institutions to upload student data (CSV) and receive cluster analysis along with **risk categorization**, enabling early interventions.

---

## 🔥 Features

- 🧠 **Unsupervised Learning with KMeans Clustering**
- 🔍 **Behavior & Performance Analysis**
- 🎯 **Dropout Risk Labeling** (High, Moderate, Mild, Low, No Risk)
- 📊 **Interactive Visualizations**:
  - PCA Cluster Plot
  - Attendance vs. Score Plot
  - Score Distribution
- 🗂️ **Accepts CSV Uploads**, processes dynamically
- 📥 **Downloadable Clustered Reports & Plots**
- 🌐 **Deployed with Streamlit App for UI**
- ⚙️ **FastAPI for Model API Service**
- 🔄 **CI/CD Pipeline with GitHub Actions**
- 🐳 **Docker Ready** for scalable deployment (Optional)

---

## 🚀 Tech Stack

- **Python** (Data & Backend)
- **scikit-learn** (Clustering, PCA)
- **Pandas, NumPy** (Data handling)
- **Matplotlib, Seaborn** (Visualization)
- **Streamlit** (Web Dashboard)
- **FastAPI** (API Endpoint)
- **GitHub Actions** (CI/CD)
- **Docker** (Containerization - optional)

---

## 🗂️ Project Folder Structure

```
Student_Dropout_Risk_Clustering_Project/
│
├── app/                  # Core logic & pipelines
│   ├── __init__.py
│   ├── preprocessing.py   # Cleaning, feature engineering
│   ├── clustering_pipeline.py
│   ├── visualization.py   # Plotting functions
│
├── streamlit_app/         # Streamlit frontend app
│   └── app.py
│
├── fastapi_app/           # FastAPI backend API
│   └── main.py
│
├── data/                  # Sample datasets
│   └── student_sample.csv
│
├── notebooks/             # Exploratory notebooks & testing
│
├── .github/workflows/     # CI/CD workflow files
│
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker container (optional)
├── README.md              # Project overview
└── .gitignore
```

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/your-username/student-dropout-risk-app.git
cd student-dropout-risk-app
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv env
source env/bin/activate  # (Linux/Mac)
env\Scriptsctivate     # (Windows)
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit App
```bash
cd streamlit_app
streamlit run app.py
```

### 5️⃣ Run FastAPI (Optional)
```bash
cd fastapi_app
uvicorn main:app --reload
```

---

## 🎯 How to Use

1. Prepare your student CSV file with the following columns:

| student_id | name | age | gender | quiz1_marks | quiz2_marks | quiz3_marks | total_assignments | assignments_submitted | midterm_marks | final_marks | previous_gpa | total_lectures | lectures_attended | total_lab_sessions | labs_attended |
|-------------|------|-----|--------|--------------|-------------|-------------|-------------------|-----------------------|---------------|-------------|--------------|-----------------|-------------------|---------------------|---------------|

2. Upload the CSV in the Streamlit app.

3. Get:
- Risk Label (`High Risk`, `Moderate`, `Mild`, `Low`, `No Risk`)
- Downloadable clustered report CSV
- Plots (PCA, Attendance vs Score, Score Distribution)

4. API available for programmatic interaction via FastAPI.

---

## 🧠 Risk Label Logic

- Risk is calculated using a weighted combination of:
  - Attendance
  - Quiz Average
  - Assignment Completion
  - Midterm & Final Marks

- Students are clustered into groups (`KMeans Clustering`) and assigned:
  - 🚨 High Risk
  - ⚠️ Moderate Risk
  - 🟡 Mild Risk
  - 🟢 Low Risk
  - ✅ No Risk

---

## 🔄 CI/CD

- Automated testing & deployment via **GitHub Actions**.
- ✅ Ensures code quality, auto deployment (optional with Docker/Streamlit Cloud/Render).

---

## 🏗️ Future Enhancements

- 🌐 Switch to a PostgreSQL Database for scalable data storage.
- 🔑 Add Authentication (Admin/Teacher Login).
- 📜 SQL Playground within app for custom queries.
- 📈 Add time-series analysis (Track progress over semesters).
- 🤖 Integrate with LMS APIs for live data.

---
     
## 👨‍💻 Author

**Muhammad Khubaib Ahmad**  
Junior Data Scientist | AI & ML Enthusiast  
[LinkedIn](https://www.linkedin.com/in/muhammad-khubaib-ahmad-) | [GitHub](https://github.com/Khubaib8281)

---

## ⭐ Acknowledgements

- UCI, Kaggle, and Open Datasets for data inspiration.
- Streamlit, FastAPI, scikit-learn community.

---
   
## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).
es teachers or academic institutions to upload student data (CSV) and receive cluster analysis along with **risk categorization** enabling early interventions.

---

## 🔥 Features

- 🧠 **Unsupervised Learning with KMeans Clustering**
- 🔍 **Behavior & Performance Analysis**
- 🎯 **Dropout Risk Labeling** (High, Moderate, Mild, Low, No Risk)
- 📊 **Interactive Visualizations**:
  - PCA Cluster Plot
  - Attendance vs. Score Plot
  - Score Distribution
- 🗂️ **Accepts CSV Uploads**, processes dynamically
- 📥 **Downloadable Clustered Reports & Plots**
- 🌐 **Deployed with Streamlit App for UI**
- ⚙️ **FastAPI for Model API Service**
- 🔄 **CI/CD Pipeline with GitHub Actions**
- 🐳 **Docker Ready** for scalable deployment (Optional)

---

## 🚀 Tech Stack

- **Python** (Data & Backend)
- **scikit-learn** (Clustering, PCA)
- **Pandas, NumPy** (Data handling)
- **Matplotlib, Seaborn** (Visualization)
- **Streamlit** (Web Dashboard)
- **FastAPI** (API Endpoint)
- **GitHub Actions** (CI/CD)
- **Docker** (Containerization - optional)

---

## 🗂️ Project Folder Structure

```
Student_Dropout_Risk_Clustering_Project/
│
├── app/                  # Core logic & pipelines
│   ├── __init__.py
│   ├── preprocessing.py   # Cleaning, feature engineering
│   ├── clustering_pipeline.py
│   ├── visualization.py   # Plotting functions
│
├── streamlit_app/         # Streamlit frontend app
│   └── app.py
│
├── fastapi_app/           # FastAPI backend API
│   └── main.py
│
├── data/                  # Sample datasets
│   └── student_sample.csv
│
├── notebooks/             # Exploratory notebooks & testing
│
├── .github/workflows/     # CI/CD workflow files
│
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker container (optional)
├── README.md              # Project overview
└── .gitignore
```

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/your-username/student-dropout-risk-app.git
cd student-dropout-risk-app
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv env
source env/bin/activate  # (Linux/Mac)
env\Scriptsctivate     # (Windows)
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit App
```bash
cd streamlit_app
streamlit run app.py
```

### 5️⃣ Run FastAPI (Optional)
```bash
cd fastapi_app
uvicorn main:app --reload
```

---

## 🎯 How to Use

1. Prepare your student CSV file with the following columns:

| student_id | name | age | gender | quiz1_marks | quiz2_marks | quiz3_marks | total_assignments | assignments_submitted | midterm_marks | final_marks | previous_gpa | total_lectures | lectures_attended | total_lab_sessions | labs_attended |
|-------------|------|-----|--------|--------------|-------------|-------------|-------------------|-----------------------|---------------|-------------|--------------|-----------------|-------------------|---------------------|---------------|

2. Upload the CSV in the Streamlit app.

3. Get:
- Risk Label (`High Risk`, `Moderate`, `Mild`, `Low`, `No Risk`)
- Downloadable clustered report CSV
- Plots (PCA, Attendance vs Score, Score Distribution)

4. API available for programmatic interaction via FastAPI.

---

## 🧠 Risk Label Logic

- Risk is calculated using a weighted combination of:
  - Attendance
  - Quiz Average
  - Assignment Completion
  - Midterm & Final Marks

- Students are clustered into groups (`KMeans Clustering`) and assigned:
  - 🚨 High Risk
  - ⚠️ Moderate Risk
  - 🟡 Mild Risk
  - 🟢 Low Risk
  - ✅ No Risk

---

## 🔄 CI/CD

- Automated testing & deployment via **GitHub Actions**.
- ✅ Ensures code quality, auto deployment (optional with Docker/Streamlit Cloud/Render).

---

## 🏗️ Future Enhancements

- 🌐 Switch to a PostgreSQL Database for scalable data storage.
- 🔑 Add Authentication (Admin/Teacher Login).
- 📜 SQL Playground within app for custom queries.
- 📈 Add time-series analysis (Track progress over semesters).
- 🤖 Integrate with LMS APIs for live data.

---

## 👨‍💻 Author

**Muhammad Khubaib Ahmad**  
Junior Data Scientist | AI & ML Enthusiast  
[LinkedIn](https://www.linkedin.com/in/muhammad-khubaib-ahmad-) | [GitHub](https://github.com/Khubaib8281)

---

## ⭐ Acknowledgements

- UCI, Kaggle, and Open Datasets for data inspiration.
- Streamlit, FastAPI, scikit-learn community.

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).
