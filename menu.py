import requests
from cuadros import Cuadro
from cuadros import CuadroNuevo
from colorama import Fore, init

init()


url = "https://api.nasa.gov/EPIC/api/natural?api_key=dSdS9JgyrQVCUhYHB6kzDfT0EMkgfoW2FYw2j6tj"

http_rsp = requests.get(url)
cuadros_rsp = http_rsp.json()

#print(cuadros_rsp)   #ESTE ES EL DICCIONARIOOO

cuadros = []
compras = []


for c in cuadros_rsp:
    cuadros.append(Cuadro(c['identifier'], c['image']))


def menu():
    print(Fore.MAGENTA + '### IMAGENES ESPACIALES ###')
    print(Fore.RESET)

    while True:
        print('1) Seleccionar imagen del cuadro')
        print('2) Personaliza tu cuadro')
        print("3) Carrito")
        print('4) Finalizar compra')
        print('5) Salir del programa')

        option = input('<<')

        if option == '1':
            for cuadro in cuadros:
                print(cuadro)
            print('Coloca el ID de la imagen que desee')

            #print(id_y_medidas)
            id_cuadro = input('<<')

            print(f'Ingrese la opcion 2) para personalizar su cuadro! \n')



        elif option == '2':
            print('Selecciona la medida que desees')
            print("Medidas posibles:")
            print("1) 18x24 --> PRECIO: $800")
            print("2) 20x30 --> PRECIO $1000")
            print("3) 30x40 --> PRECIO: $1500")
            print("4) 40x40 --> PRECIO: $2000")
            print("5) 40x50 --> PRECIO: $2300")
            print("6) 50x70 --> PRECIO: $3000")
            print("7) 70x80 --> PRECIO: $3500")
            print("8) 70x100 --> PRECIO: $4000")

            medidas = input('Coloca la opcion que desees: >>')
            med = ''
            precio = 0
            if medidas == '1':
                med += '18x24'
                precio += 800
            elif medidas == '2':
                med += '20x30'
                precio += 1000
            elif medidas == '3':
                med += '30x40'
                precio += 1500
            elif medidas == '4':
                med += '40x40'
                precio += 2000
            elif medidas == '5':
                med += '40x50'
                precio += 2300
            elif medidas == '6':
                med += '50x70'
                precio += 3000
            elif medidas == '7':
                med += '70x80'
                precio += 3500
            elif medidas == '8':
                med += '80x100'
                precio += 4000


            mi_cuadro = CuadroNuevo(med, precio)
            print(mi_cuadro)

            dict = {}
            dict["ID cuadro"] = id_cuadro
            dict["Medidas del cuadro"] = med
            dict["Precio del cuadro $"] = precio
            compras.append(dict)

        elif option == '3':
            print(f"Listado de compras: {compras}")

        elif option == "4":
            print(f"Articulos seleccionados: {compras}")
            print("Metodos de Pago:")
            print("1) Efectivo")
            print("2) Tarjeta de credito")
            print("3) Tarjeta de debito")
            print("4) Mercado Pago")

            pago = input("Seleccione su forma de pago: ")

            print("Ahora elija su forma de envio")
            print("1) Correo")
            print("2) A domicilio (Cargo adicional)")

            envio = input(">> ")

            print("¡Gracias por su compra en CYOS!")


        elif option == '5':
            print("El programa finalizo, gracias por visitarnos, vuelva pronto!")
            print('Que tenga un hermoso dia! :)')
            break

        else:
            print('Opcion invalida. Ingrese una opcion valida')


#CODIGO:

menu()

