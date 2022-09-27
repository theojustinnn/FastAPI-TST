from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/")
async def save_identity(nim: str = Form(), nama: str = Form()):
    return {"NIM": nim, "Nama" : nama}