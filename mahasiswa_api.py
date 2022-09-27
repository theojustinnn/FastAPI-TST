# Nama  : Theodore Justin Lionar
# NIM   : 18220011
# Tugas : FastAPI

# Import class
from fastapi import FastAPI, File, UploadFile
import json

# Create instance
app = FastAPI(debug=True)

# Define path
@app.post("/mahasiswa")                             # post -> add

# Python function
def upload_json(file_json: UploadFile = File(...)):
    data_mahasiswa = json.load(file_json.file)      # json.load convert json to dict
    return data_mahasiswa