
import ifcopenshell as ifc




def obtenerProyecto(rutaArchivo):
    proyecto = NULL
    try:
        proyecto = archivoIfc.by_type("IfcProyect")[0]
    except:
        print("No se pudo obtener el proyecto")
    return proyecto


def ObtenerInfoOnjetos(archivoIfc,tipo = "IfcBuildingElement"):
    elementos = archivoIfc.by_type(tipo)
    for elemento in elementos:
        print(elemento)
    print('Hay {} elementos de tipo {} en la construcción'.format(len(elementos),tipo))

archivo = ifc.open('d')
archivo