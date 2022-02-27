from typing import Optional

from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.api_function import  Hello_world, NewTicket,Tickets,status
from src.admin.admin_controller import index
app = FastAPI()

templates = Jinja2Templates(directory="src")

@app.get("/")
def ping():
    return Hello_world()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/Tickets")
async def tickets_admin():
    return templates.TemplateResponse("admin/admin_view.html",index())

@app.get("/Crear_ticket/{name}")
async def Crear_ticket(name: str):
    return NewTicket(name)

@app.get("/tickets/")
async def muestra_datos():
    return Tickets()

@app.get("/status/{id}/{state}")
def cambiar_status(id:str,state:str):
    return status(state,id)