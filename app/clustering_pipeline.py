from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from app.preprocessing import clean_engineer_features, categorize_performance, categorize_participation, label_risk
from app.visualization import plot_score_dist, plot_attendance_vs_score, plot_cluster_pca
from sklearn.cluster import KMeans

def clustering_pipeline(df, n_clusters=5, visualize=True):
    df = clean_engineer_features(df)
    
    # Select only numerical features
    features = ['avg_quiz_score', 'assignment_completion_ratio',
                'attendance_percentage', 'lab_participation_ratio',
                'exam_score_avg', 'total_score']
    
    X = df[features]
    
    # Scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Dimensionality Reduction (PCA)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    # Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X_pca)
    
    df['cluster'] = clusters
    df['pca_x'] = X_pca[:, 0]
    df['pca_y'] = X_pca[:, 1]

    cluster_summary = df.groupby('cluster')[[
    'avg_quiz_score',
    'assignment_completion_ratio',
    'attendance_percentage',
    'midterm_marks',
    'final_marks'
    ]].mean().round(2).sort_values(by='attendance_percentage', ascending=True)

    # print(cluster_summary)

    # cluster_summary.to_csv("D:\PROGRAMMING\DATA SCIENCE\Student_Dropout_Risk_&_Behavior_Clustering_Project\project\data\cluster_summary.csv", index=False)



    # Categorize based on rules
    df['performance_category'] = df.apply(lambda row: categorize_performance(row['total_score']), axis=1)

    df['participation_category'] = df.apply(lambda row: categorize_participation(
    row['attendance_percentage'],
    row['assignment_completion_ratio'], lab_ratio=None), axis=1)

    df = label_risk(df)


    if visualize:
        print("📊 Showing Visualizations:")
        plot_score_dist(df)
        plot_attendance_vs_score(df)
        plot_cluster_pca(df)
    
    return df
