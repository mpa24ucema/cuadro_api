#ACA SE GUARDAN DATOS IMPORTANTES QUE DESPUES VOY A IMPORTAR!

import requests
from id_y_medidas import id_y_medidas


#Api de terceros NASA

url = 'https://api.nasa.gov/EPIC/api/natural?api_key=dSdS9JgyrQVCUhYHB6kzDfT0EMkgfoW2FYw2j6tj'
http_rsp = requests.get(url)
cuadros_rsp = http_rsp.json() #Este es el diccionario de la nasa ya en formato json


#Datos que vamos a usar: ID y imagen
cuadros = []
for cuadro in cuadros_rsp:
    cuadros.append(cuadro['identifier'])
    cuadros.append(cuadro['image'])
    imagen = cuadro['image']

    id_solos = []


def aniadir_ids(cuadros):
    for m in cuadros:
        id_solos.append(m['id'])
    return id_solos



#Lista de medidas
medidas = [
    {"medida": "18x24","precio": "$800"},
    {"medida": "20x30","precio": "$1000"},
    {"medida": "30x40","precio": "$1500"},
    {"medida": "40x40","precio": "$2000"},
    {"medida": "40x50","precio": "$2300"},
    {"medida": "50x70","precio": "$3000"},
    {"medida": "70x80","precio": "$3500"},
    {"medida": "80x100","precio": "$4000"}
]


#LISTA DE MEDIDAS SOLAS
medidas_solas = []
def aniadir_medidas(medidas):
    for m in medidas:
        medidas_solas.append(m['medida'])
    return medidas_solas

#LISTA DE ID SOLOS
'''id_solos = []
def aniadir_ids(cuadros):
    for m in cuadros:
        id_solos.append(m['id'])
    return id_solos
aniadir_ids(cuadros)
print(cuadros)
'''

aniadir_medidas(medidas)

#Lista donde se guarda el cuadro personalizado
cuadros_nuevos = []

#Lista CARRITO donde se guarda: ID, IMAGEN, MEDIDAS Y PRECIO

