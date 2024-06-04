from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{Ilan}")
async def read_item(Ilan: str):
    return {"message": f"Hello, {Ilan}"}
   











