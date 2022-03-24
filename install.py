#!/usr/bin/python
import os
from config_parametres import libraries
from src.db_function import create_tables
def pip_install(library):
    cmd = "pip install %s "% (library)
    os.system(cmd)
    print(cmd)


if __name__ == "__main__":
    print("<------Instalando librerias ------>")
    for library in libraries:
        pip_install(library)
    print("<------Creando Base de datos----->")
    create_tables()
    print("<-----Instalacion completada------>")
