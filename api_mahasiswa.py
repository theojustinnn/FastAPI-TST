# Nama  : Theodore Justin Lionar
# NIM   : 18220011
# Tugas : FastAPI

# Import class
from fastapi import FastAPI
from pydantic import BaseModel

# Create instance
app = FastAPI()

# Create model
class Identitas(BaseModel):
    Name: str
    NIM: int

# Create data
data_mahasiswa = {
    1: {
        "Nama": "Dummy",
        "NIM" : 0
    }
}

# Define path for view data
@app.get("/view")
async def view_name():
    return data_mahasiswa

# Define path for add data
@app.post("/add")
async def add_name(identitas: Identitas):
    if identitas.NIM in data_mahasiswa:
        return {"Error" : "Mahasiswa Sudah Terdaftar"}
    data_mahasiswa[identitas.NIM] = {"Nama" : identitas.Name, "NIM" : identitas.NIM}
    return data_mahasiswa
