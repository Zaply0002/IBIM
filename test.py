
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

