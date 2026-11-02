from fastapi import FastAPI

app = FastAPI()
# Feature nuevo
@app.get("/")
def read_root():
    return {"status": "success", "message": "¡Hello World desde el Gateway de la Pecera Inteligente!"}
