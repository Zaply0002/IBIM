
import ifcopenshell as ifc
from ifcopenshell import geom


print(ifc.version)

# Abrir archivo ifc
archivo = ifc.open('Proyecto1_Normal.ifc')


# Obtener todas los elementos de la construcción
elementos = archivo.by_type('IfcElement')
# Imprimir paredes
for elemento in elementos:
    print(elemento.Name)
print('Hay {} elementos en la construcción'.format(len(elementos)))

print('\n- - - - \n')

# Obtener todas las paredes
paredes = archivo.by_type('IfcWall')
# Imprimir paredes
for pared in paredes:
    print(pared)
    print('\n')
print('Hay {} paredes'.format(len(paredes)))


print('\n- - - - \n')
