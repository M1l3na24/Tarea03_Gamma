# Programa: PruebaSecuencia.py
# Objetivo: Prueba de los metodos de la clase conjunto.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 24-09-2024


import ClassSecuencia as Cs
import Empleado as Em
from datetime import datetime
import csv


def leer_archivo(archivoo: str) -> Cs.Secuencia:
    """
    Metodo para leer un archivo y construir una secuencia con dichos datos
    :param archivoo: El nombre del archivo que se va a leer
    :return: Una Secuencia con los datos leidos
    """
    secuencia = None
    existe = False  # El archivo no existe
    while not existe:
        try:
            with open(archivoo, encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                size = sum(1 for _ in lector)  # Saber el numero de lineas
                secuencia = Cs.Secuencia(size, "edad")  # Creamos el Conjunto de tamanio ad-hoc
            with open(archivoo, encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                lector.__next__()  # Salta la primera linea
                for fila in lector:
                    secuencia.agregar(Em.Empleado(fila[1],  # Nombre
                                                  fila[2],  # Apellidos
                                                  datetime.strptime(fila[3], "%d/%m/%Y").date(),  # Nacimiento
                                                  fila[4],  # Correo
                                                  int(fila[0]),  # Numero Empleado
                                                  float(fila[5])))  # Salario
                    id_emp1.add(int(fila[0]))
                existe = True
                print(f"El archivo {archivoo} se leyo exitosamente!\n")
        except FileNotFoundError:
            print("El archivo no existe!\n")
            archivoo = input("Escribe el nombre del archivo CSV "
                             "(incluyendo la extension del tipo de archivo '.csv'): ")
    return secuencia


def crear_empleado(num_emp: int) -> Em.Empleado:
    """
    Metodo para solicitar los datos y crear un empleado, a partir de un
    numero de empleado
    :param num_emp: El numero de empleado, no repetido del Empleado
    :return: Un objeto Empleado
    """
    emp = None
    try:  # Flujo exitoso
        nombre = input("Escribe el nombre: ")
        apellidos = input("Escribe los apellidos: ")
        nacimiento = input("Escribe la fecha de nacimiento(dd-mm-aaaa): ")
        email = input("Escribe el correo: ")
        salario = float(input("Escribe el salario del empleado: "))
        # Creamos el Empleado y lo agregamos al Conjunto
        emp = Em.Empleado(nombre, apellidos,
                          datetime.strptime(nacimiento, "%d-%m-%Y").date(),
                          email, num_emp, salario)
    except ValueError:
        print(f"La fecha {nacimiento} no corresponde con el formato dd-mm-aaaa!\n")
    return emp


a = b = None  # mis secuencias
id_emp1 = set()  # Para almacenar los ID no repetidos


def menu_ordenar() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar para ordenar un objeto de la clase Secuenciable
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Como deseas ordenar:\n'
                        '1. Apellido y nombre\n'
                        '2. Edad\n'
                        '3. Salario, nombre y edad\n'
                        '4. Numero de empleado\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,3,4,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn
# Metodos comparadores entre empleados.


def apellido_nombre(a: Em.Empleado, b: Em.Empleado) -> int:
    nombre_1 = a.apellidos + ' ' + a.nombre
    nombre_2 = b.apellidos + ' ' + b.nombre
    if nombre_1 < nombre_2:
        return -1
    elif nombre_1 > nombre_2:
        return 1
    else:
        return 0


def edad(a: Em.Empleado, b: Em.Empleado) -> int:
    if a > b:
        return -1
    else:
        return 1


def salario_nombre_edad(a: Em.Empleado, b: Em.Empleado) -> float:
    dif_salario = a.salario - b.salario
    # Si son iguales bajo el parametro salario
    if dif_salario == 0:
        dif_nombre = apellido_nombre(a, b)
        if dif_nombre == 0:
            dif_edad = edad(a, b)
            return dif_edad
        return dif_nombre
    return dif_salario


def numero_empleado(a: Em.Empleado, b: Em.Empleado) -> int:
    return a.num_emp - b.num_emp


while True:
    print("1. Crear una Secuencia")
    print("2. Agregar un elemento a la Secuencia")
    print("3. Agregar un elemento n veces a la Secuencia")
    print("4. Llenar nueva Secuencia desde archivo")
    print("5. Eliminar un elemento de la Secuencia")
    print("6. Eliminar un elemento n veces de la Secuencia")
    print("7. Determinar si una Secuencia contiene un elemento")
    print("8. Determinar el numero de repeticiones de un elemento en la Secuencia")
    print("9. Determinar si la Secuencia esta vacia")
    print("10. Determinar la cardinalidad de la Secuencia")
    print("11. Vaciar la Secuencia")
    print("12. Devolver la Secuencia con elementos unicos")
    print("13. Ordenar la Secuencia")
    print("14. Mostrar la Secuencia")
    print("15. Crear una segunda Secuencia desde archivo")
    print("16. Determinar si mis dos secuencias son iguales")
    print("[S]alir")
    accion = input("¿Que deseas hacer?: ").upper()
    if accion not in "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,S" or len(accion) > 2:
        print("No se que deseas hacer!\n")
        continue
    match accion:
        case "1":  # Crear una secuencia
            try:
                print("1. Tamaño estandar")
                print("2. Definido por el usuario")
                opcion = input("Elige una opcion: ")
                if accion not in "1,2" or len(opcion) != 1:
                    print("No se que deseas hacer!\n")
                    continue
                match opcion:
                    case "1":  # Tamaño estandar
                        comparador = input("Especifica el tipo de comparador que utilizaras \n"
                                           "(apellido_nombre, edad, salario_nombre_edad, numero_empleado):")
                        a = Cs.Secuencia(comparador)
                    case "2":  # Definido por el usuario
                        size = int(input("Dame el tamaño del Conjunto: "))
                        comparador = input("Especifica el tipo de comparador que utilizaras \n"
                                           "(apellido_nombre, edad, salario_nombre_edad, numero_empleado):")
                        a = Cs.Secuencia(size, comparador)
            except ValueError:
                print("El comparador no es valido o el tamanio no es un entero positivo.")
                continue
        case "2":  # Agregar un elemento a la Secuencia
            try:
                if a is None:
                    print("Debes crear primero una Secuencia!\n")
                    continue
                else:
                    while True:  # Para agregar repetidamente elementos en la Secuencia
                        while True:  # Para validar que el numero de Empleado sea unico
                            num_emp = int(input("Escribe el id de empleado: "))
                            if num_emp not in id_emp1:
                                id_emp1.add(num_emp)
                                break
                            else:
                                print(f"El numero de empleado {num_emp} ya existe, se debe ingresar otro!\n")
                                continue
                        emp = crear_empleado(num_emp)
                        if emp is not None:
                            a.agregar(emp)
                            print("El elemento se agrego exitosamente!\n")
                        else:
                            print("El elemento no fue agregado!\n")
                        resp = input("Deseas seguir agregando elementos? (s/n): ").lower()
                        if resp == 'n':
                            break
            except ValueError:
                print("Has ingresado valores invalidos.")
                continue
        case "3":  # Agregar un elemento n veces a la Secuencia
            try:
                if a is None:
                    print("Debes crear primero una Secuencia!\n")
                    continue
                else:
                    while True:  # Para agregar repetidamente elementos en la Secuencia
                        while True:  # Para validar que el numero de Empleado sea unico
                            num_emp = int(input("Escribe el id de empleado: "))
                            n_veces = int(input("Escribe cuantas veces lo deseas agregar: "))
                            if num_emp not in id_emp1:
                                id_emp1.add(num_emp)
                                break
                            else:
                                print(f"El numero de empleado {num_emp} ya existe, se debe ingresar otro!\n")
                                continue
                        emp = crear_empleado(num_emp)
                        if emp is not None:
                            a.agregar(emp, n_veces)
                            print(f"El elemento se agrego exitosamente!\n")
                        else:
                            print("El elemento no fue agregado!\n")
                        resp = input("Deseas seguir agregando elementos? (s/n): ").lower()
                        if resp == 'n':
                            break
            except ValueError:
                print("Has ingresado valores invalidos.")
                continue
        case "4":  # Llenar nueva Secuencia desde archivo
            print("Este metodo permite crear una secuencia nueva adecuada al tamanio de datos del archivo que se \n"
                  "introduzca. No importa si ya se habia creado una secuencia anteriormente. El comparador \n"
                  "por default con el que se creara sera por edad.")
            archivo = input("Escribe el nombre del archivo CSV "
                            "(incluyendo la extension del tipo de archivo '.csv'): ")
            a = leer_archivo(archivo)
        case "5":  # Eliminar un elemento de la Secuencia
            try:
                if a is None:
                    print("Debes crear primero una Secuencia!\n")
                    continue
                else:
                    while True:
                        num_emp = int(input("Escribe el id de empleado: "))
                        if num_emp not in id_emp1:
                            print("Ese numero de empleado no existe en la secuencia.")
                            break
                        else:
                            emp = crear_empleado(num_emp)  # necesitas la informacion completa tal cual del empleado
                            if emp is not None:
                                a.eliminar(emp)
                                if not a.contiene(emp):
                                    id_emp1.remove(num_emp)
                                print("El elemento se elimino exitosamente!\n")
                            else:
                                print("El elemento no fue eliminado!\n")
                            resp = input("Deseas seguir eliminando elementos? (s/n): ").lower()
                            if resp == 'n':
                                break
            except ValueError:
                print("Has ingresado valores invalidos.")
                continue
        case "6":  # Eliminar un elemento n veces de la Secuencia
            try:
                if a is None:
                    print("Debes crear primero una Secuencia!\n")
                    continue
                else:
                    while True:
                        num_emp = int(input("Escribe el id de empleado: "))
                        if num_emp not in id_emp1:
                            print("Ese numero de empleado no existe en la secuencia.")
                            break
                        n_veces = int(input("Escribe el numero de veces que lo deseas eliminar: "))
                        emp = crear_empleado(num_emp)  # necesitas informacion completa tal cual del empleado
                        if emp is not None and a.contiene(emp):
                            a.eliminar(emp, n_veces)
                            id_emp1.remove(num_emp)
                            print(f"El elemento se elimino exitosamente {n_veces} veces!\n")
                        else:
                            print("El elemento no fue eliminado!\n")
                        resp = input("Deseas seguir eliminando elementos? (s/n): ").lower()
                        if resp == 'n':
                            break
            except ValueError:
                print("Has ingresado valores invalidos.")
                continue
        case "7":  # Determinar si una Secuencia contiene un elemento
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                while True:
                    num_emp = int(input("Escribe el id de empleado: "))
                    emp = crear_empleado(num_emp)
                    if emp is not None:
                        if a.contiene(emp):
                            print("El elemento esta contenido!\n")
                        else:
                            print("El elemento no esta contenido!\n")
                    else:
                        print("El elemento no pudo ser buscado!\n")
                    resp = input("Deseas seguir buscando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
        case "8":  # Determinar el numero de repeticiones de un elemento en la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                while True:
                    num_emp = int(input("Escribe el id de empleado: "))
                    emp = crear_empleado(num_emp)
                    if emp is not None:
                        cuenta = a.repeticiones(emp)
                        print(f"El elemento {emp} esta {cuenta} veces en la Secuencia!\n")
                    else:
                        print("El elemento no puede contabilizarse!\n")
                    resp = input("Deseas seguir buscando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
        case "9":  # Determinar la Secuencia esta vacia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                if a.esta_vacia():
                    print("La Secuencia esta vacia")
                    continue
                else:
                    print("La Secuencia no esta vacia")
                    continue
        case "10":  # Determinar la cardinalidad de la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                print(f"La cardinalidad de la secuencia es {a.cardinalidad()}")
                continue
        case "11":  # Vaciar la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                a.vaciar()
                print("La Secuencia ha sido vaciada exitosamente!\n")
                continue
        case "12":  # Devolver la Secuencia con elementos unicos
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                sec_unico = a.secuencia_unico()
                print(sec_unico)
        case "13":  # 13. Ordenar la Secuencia
            opcion = menu_ordenar()
            while opcion != 'S':
                match opcion:
                    case "1":  # Apellido y nombre
                        a.comparador = apellido_nombre
                        ordenada = a.ordenar()
                        print(ordenada)
                        break
                    case "2":  # Edad
                        a.comparador = edad
                        ordenada = a.ordenar()
                        print(ordenada)
                        break
                    case "3":  # Salario, nombre y edad
                        a.comparador = salario_nombre_edad
                        ordenada = a.ordenar()
                        print(ordenada)
                        break
                    case "4":  # Numero de empleado
                        a.comparador = numero_empleado
                        ordenada = a.ordenar()
                        print(ordenada)
                        break
                    case "S":  # Salir
                        print('Regresando al menu principal')
            opcion = ""
        case "14":  # Mostrar la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
            else:
                print(a)
                print()
        case "15":  # Crear una segunda Secuencia desde archivo para poder utilizar __eq__
            print("Este metodo permite crear una segunda secuencia nueva adecuada al tamanio de datos del archivo \n "
                  "que se introduzca. No importa si ya se habia creado una secuencia anteriormente. El comparador \n"
                  "por default con el que se creara sera por edad")
            archivo = input("Escribe el nombre del archivo CSV "
                            "(incluyendo la extension del tipo de archivo '.csv'): ")
            b = leer_archivo(archivo)
        case "16":  # Determinar si dos secuencias son iguales
            if a is None:
                print("Debes crear primero una Secuencia!\n")
            elif b is None:
                print("Debes crear primero una segunda Secuencia!\n")
            else:
                respuesta = a == b  # es un bool
                if respuesta:
                    print(f"Las secuencias son iguales")
                else:
                    print("Las secuencias no son iguales")
        case "S":  # Salir
            print("Hasta luego! :D\n")
            break
