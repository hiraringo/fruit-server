# lib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
# model
from db import session
from fruit import *
import encoder
import db

FILE_PATH = Jinja2Templates(directory="static")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))

# --- --- --- --- --- ---
# Routing
# --- --- --- --- --- ---

# GET /
@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    print('--- ---zzz')
    return FILE_PATH.TemplateResponse("admin-page.html", {"request": request})

# GET /fruits/:id/
@app.get("/fruits/{id}", response_class=HTMLResponse)
async def get_by_id(request: Request, id: int):
    fruits = session.query(Fruit).filter(Fruit.id==id).all()
    table = encoder.table(fruits)
    return table

# GET /fruits/
@app.get("/fruits/")
def get():
    fruits = session.query(Fruit).all()
    table = encoder.table(fruits)
    return table

# POST /fruits/
@app.post("/fruits/")
async def post(request: Request):
    body = await request.body()
    s = body.decode('utf-8')
    dict = json.loads(s)
    name = dict['name']
    f = Fruit(name, "日本")
    session.add(f)  
    session.commit()
    return "POST OK" # あとはDBの成否判定

# PUT /fruits/: id
@app.put("/fruits/{id}")
async def put(request: Request, id: int):
    f = session.query(Fruit).filter(Fruit.id==id).first()
    body = await request.body()
    s = body.decode('utf-8')
    dict = json.loads(s)
    f.country = dict['country']
    session.commit()
    return "PUT OK"  # あとはDBの成否判定

# DELETE /fruits/: id
@app.delete("/fruits/{id}")
async def delete(request: Request, id: int):
    session.query(Fruit).filter(Fruit.id==id).delete()
    session.commit()
    return "DELETE OK"  # あとはDBの成否判定

