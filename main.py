from functions import c2, func_soliyev, konstantin,p1, inoyatov
from fastapi import FastAPI
from funcartur import artur
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Calculation
import os

DATABASE_URL = "sqlite:///./proekt.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TwoNumbers(BaseModel):
    x: float
    y: float

app = FastAPI(
    title="MMM",
    version="1.0.0",
    description="Платформа для покупки и продажи",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/c2")
def get_c2(x: float, y: float):
    result = c2(x, y)
    db = SessionLocal()
    db_calc = Calculation(operation="c2", x=x, y=y, result=result)
    db.add(db_calc)
    db.commit()
    db.close()
    return {"result": result}

@app.post("/c2")
def post_c2(data: TwoNumbers):
    result = c2(data.x, data.y)
    db = SessionLocal()
    db_calc = Calculation(operation="c2", x=data.x, y=data.y, result=result)
    db.add(db_calc)
    db.commit()
    db.close()
    return {"result": result}

@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    result = func_soliyev(x, y)
    db = SessionLocal()
    db_calc = Calculation(operation="soliyev", x=x, y=y, result=result)
    db.add(db_calc)
    db.commit()
    db.close()
    return {"result": result}

@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    result = func_soliyev(data.x, data.y)
    db = SessionLocal()
    db_calc = Calculation(operation="soliyev", x=data.x, y=data.y, result=result)
    db.add(db_calc)
    db.commit()
    db.close()
    return {"result": result}

@app.get("/konstantin")
def get_konstantin(x: float, y: float):
    return {"result": konstantin(x, y)}
@app.post("/konstantin")
def post_konstantin(data: TwoNumbers):
    return {"result": konstantin(data.x, data.y)}

@app.get("/Shakirjanov")
def get_p1(x: float, y: float):
    return {"result": p1(x, y)}

@app.post("/Shakirjanov")
def post_p1(data: TwoNumbers):
    return {"result": p1(data.x,data.y)}

@app.get("/artur")
def get_c2(x: float, y: float):
 return {"result": artur(x, y)}
@app.post("/artur")
def post_c2(data: TwoNumbers):
 return {"result": artur(data.x, data.y)}

@app.get("/inoyatov")
def get_inoyatov(x: float, y: float ):
    return {"result": inoyatov(x, y)}

@app.post("/inoyatov")
def post_inoyatov(data: TwoNumbers):
    return {"result": inoyatov(data.x, data.y)}

@app.get("/artur")
def get_c2(x: float, y: float):
 return {"result": artur(x, y)}
@app.post("/artur")
def post_c2(data: TwoNumbers):
 return {"result": artur(data.x, data.y)}


@app.get("/history")
def get_history():
    db = SessionLocal()
    calculations = db.query(Calculation).order_by(Calculation.created_at.desc()).all()
    db.close()
    return {
        "total": len(calculations),
        "calculations": [
            {
                "id": calc.id,
                "operation": calc.operation,
                "x": calc.x,
                "y": calc.y,
                "result": calc.result,
                "created_at": calc.created_at.isoformat()
            }
            for calc in calculations
        ]
    }

@app.get("/")
async def root():
    return FileResponse("index.html", media_type="text/html")

if os.path.exists("index.html"):
    app.mount("/static", StaticFiles(directory="."), name="static")
