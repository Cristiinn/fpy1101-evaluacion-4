lista_libros = []


def validar_titulo(Titulo):
    if Titulo.strip() == "":
        return False
    else:
        return True

def validar_copias(copias):
    if copias >= 0:
        return True
    else:
        return False
def validar_prestamo(prestamo):
    if prestamo > 0:
        return True
    else:
        return False



def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")



def leer_opcion():
    opcion = int(input("Seleccione una opción: "))
    return opcion



def agregar_libro(lista):

    print("> Ingrese los datos del libro que desea agregar:")

    Titulo = input("Titulo: ").strip()
    copias = int(input("N° de copias: "))
    prestamo = int(input("N° de dias del prestamo: "))


    # validacion ingreso de datos agregar_libro

    if validar_titulo(Titulo) == False:
        print("El título no puede estar vacío.")

    elif validar_copias(copias) == False:
        print("El número de copias debe ser mayor o igual a 0")

    elif validar_prestamo(prestamo) == False:
        print("El número de dias del prestamo debe ser mayor a 0")

    else:

        libro = {
            "titulo": Titulo,
            "copias": copias,
            "prestamo": prestamo,
            "disponible": False
        }

        lista.append(libro)
        print("El libro fue agregado correctamente.")



def buscar_libro(lista, Titulo):
    posicion = -1

    for i in range(len(lista)):

        if lista[i]["titulo"] == Titulo:
            posicion = i

    return posicion



def eliminar_libro(lista):

    Titulo = input("Ingrese el titulo del libro que desea eliminar: ").strip()

    posicion = buscar_libro(lista, Titulo)

    if posicion != -1:

        lista.append(posicion)
        print("El libro fue eliminado correctamente.")

    else:
        print("El libro '" + Titulo + "' no se encuentra registrado.")



def actualizar_disponibilidad(lista):

    for libro in lista:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False
            print("La disponibilidad fue actualizada correctamente.")



def mostrar_libros(lista):

    actualizar_disponibilidad(lista)

    print("\n=== LISTA DE LIBROS ===")


    if len(lista) == 0:
        print("No hay libros registrados.")
    else:
        for libro in lista:

            print("Título:", libro["titulo"])
            print("Copias:", libro["copias"])
            print("Préstamo:", libro["prestamo"])

            if libro["disponible"] == True:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: SIN COPIAS")
            print("********************************************")


while True:

    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_libro(lista_libros)
    elif opcion == 2:
        Titulo = input("Ingrese el titulo del libro que desea buscar: ").strip()
        posicion = buscar_libro(lista_libros, Titulo)
        if posicion != -1:
            print("Libro encontrado en la posición:", posicion)
            print(lista_libros[posicion])
        else:
            print("El libro no se encuentra registrado.")


    elif opcion == 3:
        eliminar_libro(lista_libros)
    elif opcion == 4:

        actualizar_disponibilidad(lista_libros)
    elif opcion == 5:

        mostrar_libros(lista_libros)
    elif opcion == 6:

        print("Gracias por usar el sistema. Vuelva Pronto")
        break
    else:
        print("Opción no válida.")
