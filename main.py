from functions import c2, func_soliyev
from fastapi import Query  # third-party
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI(
    title="MMM",
    version="1.0.0",
    description="Платформа для покупки и продажи товаров между студентами",
    docs_url="/docs",
    redoc_url="/redoc",
    #debug=settings.DEBUG,  # Используем из настроек
)


@app.get("/")
async def root():
    return {"message": "MMM API работает!", "status": "ok"}

print(c2(9,16))
print(func_soliyev(3,4))
class TwoNumbers(BaseModel):
    x: float
    y: float
@app.get("/c2")
def get_c2(x: float, y: float):
    return {"result": c2(x, y)}
@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    return {"result": func_soliyev(x, y)}
@app.post("/c2")
def post_c2(data: TwoNumbers):
    return {"result": c2(data.x, data.y)}
@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    return {"result": func_soliyev(data.x, data.y)}
