import pygame
import time
import queue
from random import randint


class Barberia:
    def __init__(self):
        self.lista_de_colas_barberos = []
        self.cola_clientes = queue.Queue()

    def crear_clientes(self):
        tiempo_aleatorio = randint(50, 100)
        self.cola_clientes.put(tiempo_aleatorio)

    def crear_barberos(self):
        cola_barbero = queue.Queue()
        self.lista_de_colas_barberos.append(cola_barbero)

    def verificar_barberos_desocupados(self):
        for cola_barbero in self.lista_de_colas_barberos:
            if cola_barbero.empty():
                return cola_barbero
        return None

    def disminuir_contadores(self):
        for cola_barbero in self.lista_de_colas_barberos:
            if not cola_barbero.empty():
                tiempo_restante = cola_barbero.get()
                if tiempo_restante > 0:
                    tiempo_restante -= 1
                    cola_barbero.put(tiempo_restante)

    def eliminar_cliente(self, cola_barbero):
        cliente_eliminado = cola_barbero.get()
        print(f"{cliente_eliminado} eliminado de la cola del barbero")

    def hay_clientes(self):
        return not self.cola_clientes.empty()



# Configuración inicial
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60

# Inicializar Pygame
pygame.init()
pygame.display.set_caption("Barbería de Diego Rocha")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Cargar imágenes
IMG_BARBERO = pygame.image.load("BarberoImg.png")
IMG_PERSONA = pygame.image.load("PersonaImg.png")

# Inicializar variables
barbero_pos = (50, 30)
persona_pos = (290, 420)
tiempo_inicio = None

# Inicializar objetos
barberia_puñeta = Barberia()
barberia_puñeta.crear_barberos()

# Funciones
def imprimir_texto(texto, fuente, color, x, y):
    render = fuente.render(texto, True, color)
    screen.blit(render, (x, y))


def imprimir_imagen(imagen, pos):
    screen.blit(imagen, pos)


def manejar_eventos():
    global persona_pos, tiempo_inicio

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                persona_pos = barbero_pos
                tiempo_inicio = time.time()

            elif evento.key == pygame.K_p:
                barberia_puñeta.crear_clientes()

            elif evento.key == pygame.K_b:
                barberia_puñeta.crear_barberos()

    return True


def dibujar_pantalla():
    # Fondo
    screen.fill((255, 255, 255))

    # Personajes
    imprimir_imagen(IMG_BARBERO, barbero_pos)
    imprimir_imagen(IMG_PERSONA, persona_pos)

    # Tiempo
    if tiempo_inicio:
        tiempo_transcurrido = int(time.time() - tiempo_inicio)
        imprimir_texto(f"Tiempo transcurrido: {tiempo_transcurrido}s", pygame.font.SysFont("Arial", 24), (0, 0, 0), 10, 10)

    # Colas
    for i, cola_barbero in enumerate(barberia_puñeta.lista_de_colas_barberos):
        imprimir_texto(f"Barbero {i + 1} ({cola_barbero.qsize()})", pygame.font.SysFont("Arial", 24), (0, 0, 0), 400,
                       50 + 50 * i)

    imprimir_texto(f"Clientes en espera: {barberia_puñeta.cola_clientes.qsize()}", pygame.font.SysFont("Arial", 24),
                   (0, 0, 0), 10, SCREEN_HEIGHT - 50)

    # Actualizar pantalla
    pygame.display.update()


# Loop principal
while True:
    if not manejar_eventos():
        break

    # Crear clientes
    if randint(0, 100) < 10 and barberia_puñeta.hay_clientes():
        cola_barbero_vacio = barberia_puñeta.verificar_barberos_desocupados()

        if cola_barbero_vacio:
            tiempo = barberia_puñeta.cola_clientes.get()
            cola_barbero_vacio.put(tiempo)
        else:
            print("Todos los barberos están ocupados")

    # Disminuir contadores de los barberos
    barberia_puñeta.disminuir_contadores()

    # Eliminar clientes de las colas de los barberos
    for cola_barbero in barberia_puñeta.lista_de_colas_barberos:
        if not cola_barbero.empty():
            tiempo_restante = cola_barbero.queue[0]
            if tiempo_restante == 0:
                barberia_puñeta.eliminar_cliente(cola_barbero)

    # Dibujar en pantalla
    dibujar_pantalla()

    # Esperar para mantener la tasa de FPS
    pygame.time.Clock().tick(FPS)