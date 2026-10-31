from fastapi import FastAPI
# Comentario para probar las actions
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "¡Hello World desde el Gateway de la Pecera Inteligente!"}
