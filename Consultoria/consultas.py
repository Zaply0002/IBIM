

import ifcopenshell as ifc
import ifcopenshell.util.element as element



def cargarArchivo(ruta):
    global archivo
    archivo = ifc.open(ruta)

#- - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - -

def obtenerObjeto(tipo, posicion=0):
   return archivo.by_type(tipo)[posicion]
   
def ListaIfcObject(tipo):
    return archivo.by_type(tipo)

"""
def ObtenerInfoOnjetos(tipo = "IfcBuildingElement"):
    
    elementos = archivo.by_type(tipo)
    for elemento in elementos:
        print(elemento)
    return str('Hay {} elementos de tipo {} en la construcción'.format(len(elementos),tipo))
"""

def ObtenerNumeroXTipo(tipo):
    elementos = archivo.by_type(tipo)
    return len(elementos)

def ListaIfcObject(tipo):
    return archivo.by_type(tipo)


def ObtenerContenedorObjeto(objeto):
    return element.get_container(objeto)

def ObtenerObjetosQueLoComponen(objeto):
    lista = list()
    for obj in objeto.IsDecomposedBy[0].RelatedObjects:
        lista.append(obj)
    return lista

def ObtenerPropiedadesObjeto(IfcObject):
    return element.get_psets(IfcObject)

def CadenaPropiedadesFiltradoObjeto(objeto, tipo):
    propiedades = element.get_psets(objeto)
    filtrados= propiedades.get(tipo)
    return filtrados

def TipoDePropiedadesObjeto(objeto):
    lista = element.get_psets(objeto).keys()
    claves = []
    for i in lista:
        claves.append(i)
    return claves



def InformacionGeneralProyecto():
    proyecto = obtenerObjeto('IfcProject')
    OwnerGivenName = proyecto.OwnerHistory.OwningUser.ThePerson.GivenName
    OrganizacionName = proyecto.OwnerHistory.OwningUser.TheOrganization.Name
    Roles = proyecto.OwnerHistory.OwningUser.TheOrganization.Roles
    ApplicationDeveloper = proyecto.OwnerHistory.OwningApplication.ApplicationDeveloper.Name
    IFCVersion = archivo.schema


    informacion = {'OwnerGivenName':OwnerGivenName, 'OrganizacionName':OrganizacionName, 'Roles':Roles,
                'ApplicationDeveloper':ApplicationDeveloper, 'IFCVersion':IFCVersion }

    return informacion

