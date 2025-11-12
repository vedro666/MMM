from functions import c2, func_soliyev
from fastapi import Query  # third-party
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.middleware.cors import CORSMiddleware

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
