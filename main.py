from functions import c2, func_soliyev, konstantin,p1
from funcInoyatov import inoyatov
from fastapi import FastAPI
from pydantic import BaseModel

class TwoNumbers(BaseModel):
    x: float
    y: float

print(c2(9,16))
print(func_soliyev(3,4))

app = FastAPI( title="MMM", version="1.0.0",
description="Платформа для покупки и продажи",
docs_url="/docs",
redoc_url="/redoc",
#debug=settings.DEBUG, 
)

@app.get("/c2")
def get_c2(x: float, y: float):
    return {"result": c2(x, y)}
@app.post("/c2")
def post_c2(data: TwoNumbers):
    return {"result": c2(data.x, data.y)}

@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    return {"result": func_soliyev(x, y)}
@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    return {"result": func_soliyev(data.x, data.y)}

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

@app.get("/inoyatov")
def get_inoyatov(x: float, y: float ):
    return {"result": inoyatov(x, y)}
@app.post("/inoyatov")
def post_inoyatov(data: TwoNumbers):
    return {"result": inoyatov(data.x, data.y)}