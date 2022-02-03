"""
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

"""


from flask import Flask, jsonify, request
app = Flask()

# Indicamos que lance el servidor y el puerto por el cual lanzarse
if __name__=='__main__':
    app.run(debug=True, port=8000)

# Indicamos el endpoint y el método a ejecutar en dicho endpoint
@app.route('/saludo', method = ['GET']) #GET es el método por defecto, no es necesario indicarlo
def saludo():
    # indicamos el parámetro a pasar
    nombre = request.args.get('nombre')

    if nombre is None and nombre is str: # validamos manualmente el tipo de dato
        texto = 'Hola '+nombre
    else:
        texto = 'Hola mundo'

    # return texto
    # Para devolver la cadena en formato json
    return jsonify({'Mensaje':texto}) 

