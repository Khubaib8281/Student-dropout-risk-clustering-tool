# from app.preprocessing import clean_engineer_features
import sys
import os

# Add the parent directory of app to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:\PROGRAMMING\DATA SCIENCE\Student_Dropout_Risk_&_Behavior_Clustering_Project\Project')))

from app.clustering_pipeline import clustering_pipeline
import pandas as pd

df = pd.read_csv("D:\PROGRAMMING\DATA SCIENCE\Student_Dropout_Risk_&_Behavior_Clustering_Project\project\data\student_dropout_behavior_dataset.csv")

clustered_df = clustering_pipeline(df, n_clusters=5, visualize=False)

clustered_df.to_csv("D:\PROGRAMMING\DATA SCIENCE\Student_Dropout_Risk_&_Behavior_Clustering_Project\project\data\clustered_student_data.csv", index=False)   