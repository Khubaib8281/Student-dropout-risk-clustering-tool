import sys
import os
from fastapi import FastAPI, File, UploadFile
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from io import StringIO

# ✅ Adjust Python path to import clustering_pipeline
current_file_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_file_dir, '..'))
sys.path.insert(0, project_dir)

from app.clustering_pipeline import clustering_pipeline

app = FastAPI(title="Student Dropout Risk Clustering API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "API is running fine 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
    
# CORS setup (so Streamlit can call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict/")
async def predict_cluster(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        decoded = contents.decode('utf-8')
        df = pd.read_csv(StringIO(decoded))
        
        clustered_df = clustering_pipeline(df)
        return {
            "status": "success",
            "data": clustered_df.to_dict(orient="records")
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

        


# uvicorn main:app --reload

# uvicorn project/api.main:app --reload

# uvicorn cd "D:\PROGRAMMING\DATA SCIENCE\Student_Dropout_Risk_&_Behavior_Clustering_Project\project\api".main:app --reload
