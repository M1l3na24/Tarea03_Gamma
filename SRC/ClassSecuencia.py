# Programa: ClassSecuencia.py
# Objetivo: Mostrar la implementacion de la "interfaz" Conjuntable, para
#           ilustrar la creacion de un TAD de objetos.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 23-09-2024

import Interfaz_Conjuntable as Ic
import Empleado as Em
import numpy as np


class Secuencia(Ic.Conjuntable):
    def __init__(self, *params):
        """
        Constructor de la secuencia que contendra objetos del tipo Empleado.
        :param params: Forzosamente se tiene que especificar el comparador
                       que se utilizara para compara objetos dentro de la secuencia
                       Si no recibe nada mas es el constructor por omision (tamanio de la secuencia = 20).
                       Si recibe 2 parametros, es el constructor por parametros.
        """
        if len(params) == 1:  # Constructor por omision = conjunto de tamanio 20
            self.__datos = np.empty(20, dtype=Em.Empleado)
            self.__nd = 0
            if params[0] in ["apellido_nombre", "edad", "salario_nombre_edad", "numero_empleado"]:
                self.__comparador = params[0]
            else:
                raise ValueError("El tipo de comparador no existe")
            print("Se creo una Secuencia para 20 elementos!\n")
        elif len(params) == 2:  # Constructor por parametros
            self.__datos = np.empty(params[0], dtype=Em.Empleado)
            self.__nd = 0
            if params[1] in ["apellido_nombre", "edad", "salario_nombre_edad", "numero_empleado"]:
                self.__comparador = params[1]
            else:
                raise ValueError("El tipo de comparador no existe")
            print(f"Se creo una Secuencia para {params[0]} elementos!\n")
        else:
            raise ValueError("El parametro recibido no es valido!\n")

    @property
    def comparador(self):
        """
        Metodo GET para obtener el tipo de comparador de la secuencia de datos
        :return: EL arreglo de datos
        :rtype: np.array
        """
        return self.__datos

    @property
    def datos(self):
        """
        Metodo GET para obtener la secuencia de datos
        :return: EL arreglo de datos
        :rtype: np.array
        """
        return self.__datos

    @property
    def nd(self) -> int:
        """
        Metodo GET para obtener el numero de datos de la secuencia
        :return: El numero de datos insertados en la Secuencia
        :rtype: int
        """
        return self.__nd

    # Metodo set
    @comparador.setter
    def comparador(self, nuevo_comparador: callable):
        """
        Metodo SET para configurar el comparador que se utilizara para ordenar.
        :param nuevo_comparador: Funcion que actua como comparador.
        """
        self.__comparador = nuevo_comparador

    def agregar(self, *params):
        """
        Metodo para agregar un elemento a la Secuencia, siempre que sea posible.
        Nota: si la secuencia tiene limite y al agregar n veces un elemento se alcanza
        el limite antes de agregarlo n veces, solo se agregaran las que 'cupieron'.
        :param params: Si solo recibe un parametro, este debera de ser el elemento a agregar
                       Si recibe dos parametros, estos seran el elemento a agregar y el numero
                       de veces que se desea agregar.
        """
        if len(params) == 1:
            try:
                self.__datos[self.__nd] = params[0]
                self.__nd += 1
            except IndexError:
                print("No es posible agregar mas elementos!\n")
        elif len(params) == 2:
            try:
                for i in range(params[1]):
                    self.__datos[self.__nd] = params[0]
                    self.__nd += 1
            except IndexError:
                print("No es posible agregar mas elementos!\n")
        else:  # le doy mas de dos parametros
            raise Exception("El numero de parametros es invalido, debe ser 1 o 2")

    def eliminar(self, *params):
        """
        Metodo que permite eliminar todas las repeticiones del elemento dentro de la Secuencia,
        siempre que esto sea posible.
        :param params: Si solo recibe un parametro, este debera de ser el elemento a eliminar.
                        (en caso de estar repetido en la secuencia, este metodo eliminara el
                        primero que se encuentre)
                       Si recibe dos parametros, estos seran el elemento a eliminar y el numero
                       de veces que se desea eliminar.
                       (en caso de estar repetido en la secuencia, este metodo eliminara los
                       primeros nrep que se encuentre)
        """
        if len(params) == 1:
            # Hay que asegurarnos que el arreglo no este vacio y el elemento exista
            if not self.esta_vacia() and self.contiene(params[0]):
                encontro = False
                it1 = iter(self)
                i = 0
                try:
                    while True:
                        elem = next(it1)
                        if elem == params[0]:  # Lo encontro
                            if i == self.__nd - 1:  # El elemento esta al final
                                self.__nd -= 1  # Dejamos innaccesible el elemento
                            else:  # El elemento no esta al final
                                self.__nd -= 1
                                self.__datos[i] = self.__datos[self.__nd]
                            print(f"El elemento {params[0]} fue eliminado!\n")
                            encontro = True
                            # elimino el primero que encuentro
                            break
                        i += 1
                except StopIteration:
                    pass
                if not encontro:
                    print(f"El elemento {params[0]} no esta en la Secuencia!\n")

        elif len(params) == 2:
            elemento = params[0]
            n = params[1]
            # Hay que asegurarnos que el arreglo no este vacio y el elemento exista
            if not self.esta_vacia() and self.contiene(params[0]):
                # me ayudara a contar cuantos llevo eliminados
                eliminados = 0
                while eliminados < n:
                    it1 = iter(self)  # Reiniciar el iterador para cada búsqueda
                    encontro = False
                    i = 0
                    try:
                        while True:
                            elem = next(it1)
                            if elem == elemento:  # Lo encontro
                                if i == self.__nd - 1:  # El elemento esta al final
                                    self.__nd -= 1  # Dejamos innaccesible el elemento
                                else:  # El elemento no esta al final
                                    self.__nd -= 1
                                    self.__datos[i] = self.__datos[self.__nd]
                                print(f"El elemento {params[0]} fue eliminado!\n")
                                eliminados += 1
                                encontro = True
                                break  # Reiniciar busqueda
                            i += 1
                    except StopIteration:
                        pass
                    if not encontro:
                        print(f"Se eliminaron {eliminados} de {n} solicitadas. "
                              f"No se encontraron mas elementos.\n")
                        break
            else:
                print(f"El elemento {params[0]} no esta en la Secuencia!\n")

    def contiene(self, elemento: Em.Empleado) -> bool:
        """
        Metodo que permite saber si un elemento se encuentra contenido
        dentro de la Secuencia.
        :param elemento: El elemento a buscar
        :return: True si lo encontro, False en otro caso
        :rtype: bool
        """
        if not self.esta_vacia():
            try:
                it1 = iter(self)
                while True:
                    empleado = next(it1)
                    if empleado == elemento:
                        return True
            except StopIteration:
                pass
        return False

    def repeticiones(self, elemento: Em.Empleado) -> int:
        """
        Metodo que determina el numero de repeticiones que el elemento
        presenta dentro de la Secuencia.
        :param elemento: El elemento a determinar las repeticiones
        :return: El numero de veces que aparece en la Secuencia
        :rtype: int
        """
        contador = 0
        if not self.esta_vacia() and self.contiene(elemento):
            it1 = iter(self)
            try:
                while True:
                    empleado = next(it1)
                    if elemento == empleado:
                        contador += 1
            except StopIteration:
                pass
        return contador

    def esta_vacia(self) -> bool:
        """
        Metodo que permite saber si la Secuencia esta vacia.
        :return: True si esta vacia, False en otro caso.
        :rtype: bool
        """
        return self.__nd == 0

    def cardinalidad(self) -> int:
        """
        Metodo que permite conocer la cardinalidad de la Secuencia.
        :return: La cantidad de elementos almacenados en la Secuencia
        :rtype: int
        """
        return self.__nd

    def vaciar(self):
        """
        Metodo que permite vaciar la Secuencia de elementos.
        """
        self.__nd = 0

    def secuencia_unico(self):
        """
        Metodo que permite devolver la Secuencia de elementos unicos
        (sin repeticiones).
        :return: La Secuencia sin repetidos
        """
        copia = Secuencia(len(self.__datos), self.__comparador)
        it1 = iter(self)
        try:
            while True:
                elemento = next(it1)
                if not copia.contiene(elemento):
                    copia.agregar(elemento)
        except StopIteration:
            return copia

    def ordenar(self):
        """
        Metodo que permite devuelver la Secuencia de elementos ordenada.
        Utiliza Quick Sort y habilita la existencia de 4 comparadores
        por ejemplo, en el caso de los Empleados, se pueden ordenar por
        apellido y nombre, edad descendentemente, salario, nombre y edad\n
        o por numero de empleado.
        :return: La Secuencia ordenada
        """
        self.__ordenar_recursivo(0, self.__nd - 1, self.__comparador)
        return self

# Metodos extra

    def __str__(self):
        """
        Metodo que permite devolver una Secuencia como una cadena de caracteres
        :return: La secuencia en formato cadena
        """
        # Utilizando los iteradores
        it1 = iter(self)
        secuencia = "Secuencia: \n"
        try:
            while True:
                elem = next(it1)
                secuencia += str(elem) + "\n"
        except StopIteration:
            pass
        return secuencia

    def __eq__(self, otra_secuencia):
        """
        Metodo que permite determinar si dos secuencias son iguales
        :param otra_secuencia: La Secuencias con el que se va a comparar
        :return: True si son iguales, False en otro caso
        """
        respuesta = True  # Asumimos que las dos Secuencias son iguales
        # Utilizando los iteradores
        it1 = iter(self)
        # Verificamos que tengan la misma cardinalidad
        if self.cardinalidad() == otra_secuencia.cardinalidad():
            try:
                while True:
                    elem = next(it1)
                    if not otra_secuencia.contiene(elem):
                        respuesta = False
                        break
            except StopIteration:
                pass
        else:
            respuesta = False
        return respuesta

    def __iter__(self):
        """
        Metodo que permite inicializar el iterador de Secuencias
        :return: Un objeto iterable
        """
        self.pos = 0
        return self

    def __next__(self) -> Em.Empleado:
        """
        Metodo que permite obtener el siguiente elemento de la Secuencia
        :return: El siguiente elemento de la Secuencia
        :rtype: int
        """
        if self.pos < self.nd:
            a = self.datos[self.pos]
            self.pos += 1
            return a
        else:
            raise StopIteration

    def __particion(self, inicio, fin, comparador):
        """
        Esta funcion organiza los elementos del directorio de manera que todos los elementos
        menores o iguales al pivote estan a la izquierda y todos los elementos mayores estan
        a la derecha. El pivote se coloca en su posicion correcta.
        :param inicio: La posicion inicial
        :param fin: La posicion final
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: La posicion correcta del pivote
        :rtype: int
        """
        pivote = self.__datos[inicio]
        left = inicio + 1
        right = fin
        while True:
            while left <= right and comparador(self.__datos[left], pivote) <= 0:
                left += 1
            while comparador(self.__datos[right], pivote) > 0 and right >= left:
                right -= 1
            if right < left:
                break
            else:  # Intercambiamos los datos que no cumplieron las condiciones
                self.__datos[left], self.__datos[right] = self.__datos[right], self.__datos[left]
                # Movemos el pivote a la posici�n correcta
        self.__datos[inicio], self.__datos[right] = self.__datos[right], self.__datos[inicio]
        return right  # Devolvemos la posicion correcta del pivote

    def __ordenar_recursivo(self, inicio, fin, comparador):
        """
        Esta funcion aplica recursivamente el algoritmo Quick Sort a los subarreglos definidos por el pivote.
        :param inicio: La posicion inicial
        :param fin: La posicion final
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: Arreglo de contactos ordenado
        """
        if inicio < fin:
            posicion_part = self.__particion(inicio, fin, comparador)
            self.__ordenar_recursivo(inicio, posicion_part - 1, comparador)
            self.__ordenar_recursivo(posicion_part + 1, fin, comparador)
        return self.__datos
