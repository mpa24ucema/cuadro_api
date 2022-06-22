from flask import Flask, jsonify, request
from datos import medidas
from datos import cuadros_rsp
from datos import cuadros
from datos import imagen
from datos import cuadros_nuevos
from datos import aniadir_medidas
from datos import medidas_solas
from datos import aniadir_ids
from datos import id_solos
from id_y_medidas import id_y_medidas


import random

app = Flask(__name__)

#FUNCIONES PARA AÑADIR MEDIDAS Y IDS
aniadir_medidas(medidas)
aniadir_ids(id_y_medidas)


#ACA GENERAMOS LA API DE TERCEROS DE LA NASA
@app.route('/nasa', methods=['GET'])
def nasaGet():
    return jsonify({'cuadros:': cuadros_rsp, 'status': 'ok'})



#ACA HACEMOS QUE DE LA API DE LA NASA NOS TRAIGA ID Y IMAGEN
@app.route('/cuadros', methods=['GET'])
def imagenesGet():
    return jsonify({'imagenes disponibles:': cuadros, 'status': 'ok'})



#ACA EL CLIENTE ELIGE LA IMAGEN
@app.route('/imagen/<id>', methods=['GET'])
def imagenGet(id):
    return f'ID imagen:{id} \n '\
           f'Imagen: {imagen}' \



#ACA GENERAMOS LA TABLA DE MEDIDAS
@app.route('/medidas', methods=['GET'])
def medidasGet():
    return jsonify({'medidas:': medidas, 'status': 'ok'})



#ACA  EL CLIENTE PONE QUE IMAGEN Y MEDIDA QUIERE     #ESTO ES LO DE LOS CHICOSSS
@app.route('/micuadro', methods=['POST'])
def miCuadroPost():
    orden_de_compra = str(random.randint(1000000, 9000000))
    imagen_uni = ''
    precio_uni = ''
    id_post = request.json['id']
    medida_post = request.json['medida']
    for p in medidas:
        if medida_post == p['medida']:
            precio_uni += p['precio']
    for c in id_y_medidas:
        if id_post == c['id']:
            imagen_uni += c['imagen']
    cuadro_nuevo = {
        'id' : id_post,
        'medidas' : medida_post,
        'imagen' : imagen_uni,
        "orden_de_compra" : orden_de_compra,
        'precio' : precio_uni
    }

    if id_post in id_solos and medida_post in medidas_solas:
        cuadros_nuevos.append(cuadro_nuevo)

        return jsonify({'mensaje' : 'fue creado con exito', 'cuadro personalizado' : cuadros_nuevos, "orden de compra generada": orden_de_compra})
    else:
        return jsonify({"Orden de compra": orden_de_compra, 'Error':'Se ingresaron datos incorrectos (deben ser medidas y ids existentes)'})



# ACA SE PODRIA MODIFICAR EL CUADRO este es la prueba por si sale mal
@app.route("/micuadro/<orden_de_compra>", methods=["PUT"])
def clientes_put(orden_de_compra):
    orden_nueva = {}
    precio_uni = ""
    imagen_uni = ""
    body = request.json
    id_post = body["id"]
    medida_post = body["medida"]

    for p in medidas:
        if medida_post == p['medida']:
            precio_uni += p['precio']
    for c in id_y_medidas:
        if id_post == c['id']:
            imagen_uni += c['imagen']

    if id_post in id_solos and medida_post in medidas_solas:
        cuadros_nuevos.append(orden_nueva)

        for cuadro in cuadros_nuevos:
            if cuadro["orden_de_compra"] == orden_de_compra:
                orden_nueva["id"] = id_post
                orden_nueva["medida"] = medida_post
                orden_nueva["orden_de_compra"] = orden_de_compra
                orden_nueva["imagen"] = imagen_uni
                orden_nueva["precio"] = precio_uni
                cuadros_nuevos.remove(cuadro)
                #cuadros_nuevos.append(orden_nueva)

                return jsonify({"orden_de_compra": orden_de_compra, "id": id_post, "medidas": medida_post, "imagen": imagen_uni, "precio": precio_uni})
    else:
        return jsonify({"Orden de compra": orden_de_compra, 'Error':'Se ingresaron datos incorrectos (deben ser medidas y ids existentes)'})




#ACA HACEMOS QUE DE LA API DE LA NASA NOS TRAIGA ID Y IMAGEN CON LA MODIFICACIONNN!
@app.route('/micuadro', methods=['GET'])
def micuadro_Get():
    return jsonify({'Cuadros seleccionados en el carrito': cuadros_nuevos, 'status': 'ok'})



#ACA ELIMINAMOS EL CUADRO
@app.route("/micuadro/<orden_de_compra>", methods= ["DELETE"])
def CuadroDelete(orden_de_compra):
    for c in cuadros_nuevos:
        if c["orden_de_compra"] == orden_de_compra:
            cuadros_nuevos.remove(c)
            return jsonify({"cuadro eliminado": c, "busqueda": orden_de_compra, "status": "ok"})
    return jsonify({"busqueda": orden_de_compra, "status": "not found"})






#ESTO SIMEPRE VA AL FINAL!!
if __name__ == '__main__':
    app.run(debug=True, port=4000)







