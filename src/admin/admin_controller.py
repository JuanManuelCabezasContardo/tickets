from fastapi import Request
from src.db_function import db_insert,db_select

def index():
    select = "SELECT * FROM TICKET order by ID desc"
    salida = db_select(select)
    return {"request":{},"tabla":salida}

