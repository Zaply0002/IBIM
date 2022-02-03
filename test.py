"""
import Consultoria.consultas as con
archivo1 = "Proyecto1_Normal.ifc"
archivo2 = 'prueba02.ifc'
con.cargarArchivo(archivo2)
print()

info = con.InformacionGeneralProyecto()
#print(info)


obj = con.obtenerObjeto('IfcBuildingStorey')

propiedades = con.ObtenerPropiedadesObjeto(obj)
#print(propiedades)

tipoPropiedades = con.TipoDePropiedadesObjeto(obj)
#print(tipoPropiedades)

propiedadesFiltrados=con.CadenaPropiedadesFiltradoObjeto(obj, 'Datos de identidad')
#print(propiedadesFiltrados)



objs = con.ObtenerObjetosQueLoComponen(obj)

for i in objs:
    print(i)
    print()
"""
import requests
import io

# Probando el endpoint sin parametro
resp = requests.get('http://127.0.0.1:8000/saludo')
print(resp.text) # Hola mundo

# Probando el endpoint con parametro
resp = requests.get('http://127.0.0.1:8000/saludo?nombre=Cristian')
print(resp.text) # Hola Cristian