from fastapi import Request
from src.db_function import db_insert,db_select

def Hello_world():
    return {"Hello": "World"} 

def NewTicket(name: str):
    from uuid import uuid4
    rand_token = uuid4()
    insert= """INSERT INTO TICKET(name,token,status) VALUES('%s','%s','creado')""" % (name,rand_token)
    salida = db_insert(insert)
    if (salida==1):
        return {"response":"todo bien milhouse"}
    else:
        return {"response":"Solo son dias bart"}

def Tickets():
    select = "SELECT * FROM TICKET"
    salida = db_select(select)
    return {"response":salida}


def status(state: str,id: int):
    insert= """UPDATE TICKET SET status='%s' WHERE ID =%s""" % (state, id)
    salida = db_insert(insert)
    if (salida==1):
        return {"response":"todo bien milhouse"}
    else:
        return {"response":"Solo son dias bart"}
    return 1