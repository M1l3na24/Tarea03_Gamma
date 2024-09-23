# Programa: PruebaSecuencia.py
# Objetivo: Prueba de los metodos de la clase conjunto.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 18-09-2024


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
                secuencia = Cs.Secuencia(size, edad)  # Creamos el Conjunto de tamanio ad-hoc
            with open(archivoo, encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                lector.__next__()  # Salta la primera línea
                for fila in lector:
                    secuencia.agregar(Em.Empleado(fila[1],  # Nombre
                                                  fila[2],  # Apellidos
                                                  datetime.strptime(fila[3], "%d/%m/%Y").date(),  # Nacimiento
                                                  fila[4],  # Correo
                                                  int(fila[0]),  # Numero Empleado
                                                  float(fila[5])))  # Salario
                existe = True
                print(f"El archivo {archivoo} se leyo exitosamente!\n")
        except FileNotFoundError:
            print("El archivo no existe!\n")
            archivoo = input("Escribe el nombre del archivo CSV: ")
    return secuencia


def crear_empleado(num_emp: int) -> Em.Empleado:
    """
    Método para solicitar los datos y crear un empleado, a partir de un
    número de empleado
    :param num_emp: El número de empleado, no repetido del Empleado
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


a = None  # mi secuencia
id_emp1 = set()  # Para almacenar los ID no repetidos
id_emp2 = set()  # Para almacenar los ID no repetidos


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
    print("9. Determinar la Secuencia esta vacia")
    print("10. Determinar la cardinalidad de la Secuencia")
    print("11. Vaciar la Secuencia")
    print("12. Devolver la Secuencia con elementos unicos")
    print("13. Ordenar la Secuencia")
    print("14. Mostrar la Secuencia")
    print("[S]alir")
    accion = input("¿Qué deseas hacer?: ").upper()
    if accion not in "1,2,3,4,5,6,7,8,9,10,11,12,13,14,S" or len(accion) > 2:
        print("No se que deseas hacer!\n")
        continue
    match accion:
        case "1":  # Crear una secuencia
            print("1. Tamaño estándar")
            print("2. Definido por el usuario")
            opcion = input("Elige una opción: ")
            if accion not in "1,2" or len(opcion) != 1:
                print("No sé qué deseas hacer!\n")
                continue
            match opcion:
                case "1":  # Tamaño estándar
                    comparador = input("Especifica el tipo de comparador que utilizaras:")
                    a = Cs.Secuencia(comparador)
                case "2":  # Definido por el usuario
                    size = int(input("Dame el tamaño del Conjunto: "))
                    comparador = input("Especifica el tipo de comparador que utilizaras:")
                    a = Cs.Secuencia(size, comparador)
        case "2":  # "2. Agregar un elemento a la Secuencia"
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                while True:  # Para agregar repetidamente elementos en la Secuencia
                    while True:  # Para validar que el número de Empleado sea único
                        num_emp = int(input("Escribe el id de empleado: "))
                        if num_emp not in id_emp1:
                            id_emp1.add(num_emp)
                            break
                        else:
                            print(f"El número de empleado {num_emp} ya existe, se debe ingresar otro!\n")
                            continue
                    emp = crear_empleado(num_emp)
                    if emp is not None:
                        a.agregar(emp)
                        print("El elemento se agregó exitosamente!\n")
                    else:
                        print("El elemento no fue agregado!\n")
                    resp = input("Deseas seguir agregando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
        case "3":  # Agregar un elemento n veces a la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                while True:  # Para agregar repetidamente elementos en la Secuencia
                    while True:  # Para validar que el número de Empleado sea único
                        num_emp = int(input("Escribe el id de empleado: "))
                        n_veces = int(input("Escribe cuantas veces lo deseas agregar: "))
                        if num_emp not in id_emp1:
                            id_emp1.add(num_emp)
                            break
                        else:
                            print(f"El número de empleado {num_emp} ya existe, se debe ingresar otro!\n")
                            continue
                    emp = crear_empleado(num_emp)
                    if emp is not None:
                        a.agregar(emp, n_veces)
                        print(f"El elemento se agregó exitosamente {n_veces} veces!\n")
                    else:
                        print("El elemento no fue agregado!\n")
                    resp = input("Deseas seguir agregando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
        case "4":  # Llenar nueva Secuencia desde archivo
            print("Este metodo permite crear una secuencia nueva adecuada al tamanio de datos del archivo que se "
                  "introduzca. No importa si ya se habia creado una secuencia anteriormente. El comparador"
                  "por default con el que se creara sera por edad")
            archivo = input("Escribe el nombre del archivo CSV: ")
            a = leer_archivo(archivo)
        case "5":  # Eliminar un elemento de la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                while True:
                    num_emp = int(input("Escribe el id de empleado: "))
                    emp = crear_empleado(num_emp)  # necesitas la informacion completa tal cual del empleado
                    if emp is not None:
                        a.eliminar(emp)
                        print("El elemento se eliminó exitosamente!\n")
                    else:
                        print("El elemento no fue eliminado!\n")
                    resp = input("Deseas seguir eliminando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
        case "6":  # Eliminar un elemento n veces de la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                while True:
                    num_emp = int(input("Escribe el id de empleado: "))
                    n_veces = int(input("Escribe el numero de veces que lo deseas eliminar: "))
                    emp = crear_empleado(num_emp)  # necesitas informacion completa tal cual del empleado
                    if emp is not None:
                        a.eliminar(emp, n_veces)
                        print(f"El elemento se eliminó exitosamente {n_veces} veces!\n")
                    else:
                        print("El elemento no fue eliminado!\n")
                    resp = input("Deseas seguir eliminando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
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
                            print("El elemento está contenido!\n")
                        else:
                            print("El elemento no está contenido!\n")
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
                    resp = input("Deseas seguir eliminando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
        case "9":  # Determinar la Secuencia esta vacia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                if a.esta_vacia():
                    print("La Secuencia está vacia")
                    break
                else:
                    print("La Secuencia no está vacia")
                    break
        case "10":  # Determinar la cardinalidad de la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                print(f"La cardinalidad de la secuencia es {a.cardinalidad()}")
                break
        case "11":  # Vaciar la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                a.vaciar()
                print("La Secuencia ha sido vaciada exitosamente!\n")
                break
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
                    case "2":  # Edad
                        a.comparador = edad
                        ordenada = a.ordenar()
                        print(ordenada)
                    case "3":  # Salario, nombre y edad
                        a.comparador = salario_nombre_edad
                        ordenada = a.ordenar()
                        print(ordenada)
                    case "4":  # Numero de empleado
                        a.comparador = numero_empleado
                        ordenada = a.ordenar()
                        print(ordenada)
                    case "S":  # Salir
                        print('Regresando al menu principal')
            opcion = ""
        case "14":  # Mostrar la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
            else:
                print(a)
                print()
        case "S":  # Salir
            print("Hasta luego! :D\n")
            break
