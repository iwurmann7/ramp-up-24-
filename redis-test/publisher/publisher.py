from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
import redis

app = FastAPI()

redis_conn = redis.Redis(host='redis', port=6379)

class PublishRequest(BaseModel):
    message: str
    
@app.get("/")
def read_root():
    return{"message": "My name is Ilan"}

@app.post("/send")
def send_message(payload: PublishRequest):
    try:
        redis_conn.publish('my_channel', payload.message)
        return {"status": "Message sent"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
@app.get("/openapi.jason")
async def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="Your API", version="1.0.0", routes=app.routes))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)