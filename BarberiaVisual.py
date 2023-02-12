import pygame
import time

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
            elif evento.key == pygame.K_b:
                print("Agregar barbero")
            elif evento.key == pygame.K_p:
                print("Agregar persona")

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
        imprimir_texto(f"Tiempo transcurrido: {tiempo_transcurrido} segundos", pygame.font.Font(None, 20), (0, 0, 0),
                       SCREEN_WIDTH - 220, 10)

    # Instrucciones
    imprimir_texto("Tecla [b] para añadir barberos", pygame.font.Font(None, 20), (0, 0, 0), 30, 400)
    imprimir_texto("Tecla [p] para añadir personas", pygame.font.Font(None, 20), (0, 0, 0), 30, 420)

    # Actualizar pantalla
    pygame.display.update()

    return True


# Bucle principal
jugando = True
reloj = pygame.time.Clock()

while jugando:
    jugando = manejar_eventos()
    dibujar_pantalla()
    reloj.tick
