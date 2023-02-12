from random import randint
import queue


class Barberia:

    def __init__(self, cantidad_barberos, cantidad_clientes):
        self.lista_barberos = None
        self.cola_clientes = None
        self.cantidad_barberos = cantidad_barberos
        self.cantidad_clientes = cantidad_clientes

    def crear_clientes(self):
        cola_clientes = queue.Queue()
        for clientes in range(self.cantidad_clientes):
            tiempo_aleatorio = randint(5, 10)
            cola_clientes.put(tiempo_aleatorio)
        self.cola_clientes = cola_clientes

        '''def crear_barberos(self):
        for barberos in range(self.cantidad_barberos):
            barbero = queue.Queue()
            yield barbero'''

    def crear_barberos(self):
        lista_barberos = []
        for clientes in range(self.cantidad_barberos):
            cola_barbero = queue.Queue()
            lista_barberos.append(cola_barbero)
        self.lista_barberos = lista_barberos

    def asignar_cliente_a_barbero(self):
        if self.cola_clientes.empty():
            print("No hay más clientes")
            return
        for i, cola_barbero in enumerate(self.lista_barberos):
            if cola_barbero.empty():
                cliente = self.cola_clientes.get()  # Sacamos al cliente de la cola de clientes
                cola_barbero.put(cliente)  # Agregamos al cliente a la cola de un barbero
            else:
                print(f"barbero {i} lleno")
        print(self.lista_barberos)
        print(self.cola_clientes)


barberia_puñeta = Barberia(5, 3)
barberia_puñeta.crear_clientes()
barberia_puñeta.crear_barberos()
barberia_puñeta.asignar_cliente_a_barbero()