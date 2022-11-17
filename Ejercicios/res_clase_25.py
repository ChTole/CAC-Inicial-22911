"""
El sitio https://jsonplaceholder.typicode.com/users tiene alojados datos de usuarios en formato JSON. 
Utilizando la librería requests, capturar los datos y generar un libro de MS Excel con la siguiente información:
- id / name / email / phone / website
Tener en cuenta los tipos de colecciones a recorrer (y como acceder a los datos).

Dificultad adicional 1: generar un nuevo script de Python que realice una búsqueda dentro del libro creado permitiendo seleccionar la columna a filtrar.

Dificultad adicional 2: generar un nuevo script de Python que permita agregar una columna llamada "fecha de nacimiento" y solicite por consola el ingreso de los datos para cada usuario. Utilizar el módulo datetime y corroborar que cada dato ingresado para construir la fecha sea de acuerdo al formato dd/mm/aaaa. Por ejemplo:
- si ingreso 23/04/1998, la fecha se crea
- si ingreso 43/15/2005, la fecha no se crea.
"""

import requests
from openpyxl import Workbook

solicitud = requests.get('https://jsonplaceholder.typicode.com/users')

# print(solicitud.status_code)  # 200, conexión exitosa!
# print(solicitud.content)

datos = solicitud.json()

# print(datos)
# de datos necesito  id / name / email / phone / website

libro = Workbook()
hoja = libro.active
hoja.title = "DatosJSON"
encabezado =["id","name","email","phone","website"]
hoja.append(encabezado)

for item in datos:
    hoja.append([
        item['id'], 
        item['name'], 
        item['email'], 
        item['phone'], 
        item['website']
    ])
    
libro.save(filename= r'D:\CodoACodo\Comision 22911\Clase31\datosJson.xlsx')
libro.close()