#CUADROS

class Cuadro:
    def __init__(self, id, imagen):
        self.id = id
        self.imagen = imagen

    def __str__(self):
        return f'\t  \t \t **** Cuadro **** \n' \
               f'\t * ID:{self.id} \n' \
               f'\t * Imagen: {self.imagen} \n' \


class CuadroNuevo:
    def __init__(self, medidas, precio):
        self.medidas = medidas
        self.precio = precio

    def __str__(self):
        return f'\t ======= Tu cuadro personalizado es: ======= \n' \
               f'\t Medidas:{self.medidas} \n' \
               f'\t Precio $: {self.precio} \n' \
               f' Para terminar tu compra e ir al carrito ingrese la opcion 3), si quiere seguir comprando seleccione la opcion 1)'