from random import randint
import queue
import pygame
import time


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
        tiempo_aleatorio = randint(50, 100)
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
                print(f"{cliente}Agregado a la cola del barbero {cola_barbero}")
                return cola_barbero
            else:
                print(f"barbero {i} lleno")
        return queue.Queue() #En caso de que todas las colas esten llenas, retornamos una vacia

    def verificar_fila_vacia(self):
        if self.cola_clientes.empty():
            print("No hay más clientes")
            return True  # Si la fila esta vacia retorna true
        else:
            return False  # Si la fila esta vacia retorna true

    def disminuir_contadores(self, cola_barbero):
        if cola_barbero.empty():
            pass
        else:
            # Inicializar el temporizador con el elemento en la cola del barbero
            tiempo_restante = cola_barbero.queue[0]

            # Bucle para el temporizador
            while tiempo_restante > 0:
                print(f"Tiempo restante: {tiempo_restante}")
                tiempo_restante -= 1
                time.sleep(1)
            return cola_barbero

    def eliminar_cliente(self, cola_barbero):  # Recibe la cola del barbero donde esta el cliente al que se le
        # terminó el tiempo
        cliente_eliminado = cola_barbero.get()
        print(f"{cliente_eliminado}Eliminado de la cola del barbero {cola_barbero}")

        pass
'''        for elemento in self.lista_barberos:
            print(elemento.queue)
        print(self.cola_clientes)'''



