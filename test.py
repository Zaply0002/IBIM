
import Consultoria.consultas as con
archivo = "Proyecto1_Normal.ifc"
con.cargarArchivo(archivo)

obj = con.ListaIfcObject('IfcSlab')


x = con.ObtenerPropiedadesObjeto(obj[0])
#print (x)

con.CadenaPropiedadesFiltradoObjeto(obj[0],'BaseQuantities')

y = con.TipoDePropiedadesObjeto(obj[0])

print(y)