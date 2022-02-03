from fastapi import FastAPI
app = FastAPI()


#Indicamos el endpoint
@app.get("/saludo")
#se puede poner un parametro como opcional
#los parámetros deben indicar el tipo de valor que pasarle
def saludo(nombre = None):
    if nombre is None:
        return 'Hola mundo'
    else:
        return 'hola '+nombre

