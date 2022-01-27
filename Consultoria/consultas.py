
import ifcopenshell as ifc
import ifcopenshell.util.element as element



def cargarArchivo(ruta):
    global archivo
    archivo = ifc.open(ruta)

def obtenerObjeto(tipo, posicion=0):
   return archivo.by_type(tipo)[posicion]
   
def ListaIfcObject(tipo):
    return archivo.by_type(tipo)

def ObtenerInfoOnjetos(tipo = "IfcBuildingElement"):
    
    elementos = archivo.by_type(tipo)
    for elemento in elementos:
        print(elemento)
    print('Hay {} elementos de tipo {} en la construcción'.format(len(elementos),tipo))


def ObtenerNumeroXTipo(tipo):
    elementos = archivo.by_type(tipo)
    return len(elementos)

def ListaIfcObject(tipo):
    return archivo.by_type(tipo)

def ObtenerPropiedadesObjeto(IfcObject):
    return element.get_psets(IfcObject)

def CadenaPropiedadesFiltradoObjeto(objeto, tipo):
    propiedades = element.get_psets(objeto)
    filtrados= propiedades.get(tipo)
    print(filtrados)

def TipoDePropiedadesObjeto(objeto):
    lista = element.get_psets(objeto).keys()
    claves = []
    for i in lista:
        claves.append(i)
    return claves

