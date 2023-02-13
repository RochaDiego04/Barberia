from random import randint
import queue
import pygame


# for:
# Agregar clientes que serán numeros random de tiempo
# Agregar barberos que serán una lista de queues
# Asignar estos valores a la clase
# Metodo para verificar si los barberos están vacios y si es asi, asignarles clientes
# Cuando se asignen los clientes a las queues ir disminuyendo de 1 en 1 sus tiempos
# Cuando el tiempo de un cliente llegue a 0, borrar al cliente con get()

class Clase_Barberia:

    def __init__(self):
        self.lista_de_colas_barberos = []
        self.lista_barberos = None
        self.cola_clientes = None
        self.cantidad_barberos = 1
        self.cantidad_clientes = 1

    def crear_clientes(self):
        cola_clientes = queue.Queue()
        tiempo_aleatorio = randint(5, 10)
        cola_clientes.put(tiempo_aleatorio)
        self.cola_clientes = cola_clientes  # Agregamos un cliente a la cola
        self.cantidad_clientes += 1  # Agregamos un cliente cada que se llame a esta funcion

        '''def crear_barberos(self):
        for barberos in range(self.cantidad_barberos):
            barbero = queue.Queue()
            yield barbero'''

    def crear_barberos(self):
        cola_barbero = queue.Queue()
        self.lista_de_colas_barberos.append(cola_barbero)
        self.cantidad_barberos += 1  # Agregamos un barbero cada que se llame a esta funcion

    def verificar_barberos_desocupados(self):
        for i, cola_barbero in enumerate(self.lista_de_colas_barberos):
            if cola_barbero.empty():
                cliente = self.cola_clientes.get()  # Sacamos al cliente de la cola de clientes
                cola_barbero.put(cliente)  # Agregamos al cliente a la cola de un barbero
                print(f"Agregado a la cola del barbero {cola_barbero}")
            else:
                print(f"barbero {i} lleno")

    def verificar_fila_vacia(self):
        if self.cola_clientes.empty():
            print("No hay más clientes")
            return True  # Si la fila esta vacia retorna true
        else:
            return False  # Si la fila esta vacia retorna true

'''        for elemento in self.lista_barberos:
            print(elemento.queue)
        print(self.cola_clientes)'''



