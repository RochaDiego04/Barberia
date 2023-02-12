import pygame
import time

# Inicializar Pygame
pygame.init()

# Configurar la ventana
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Titulo e icono
pygame.display.set_caption("Barbería de Diego Rocha")

# Cargar la imagen de píxeles y posicion inicial
img_barbero = pygame.image.load("BarberoImg.png")
barbero_x = 50
barbero_y = 30

img_persona = pygame.image.load("PersonaImg.png")
persona_x = 290
persona_y = 420

# Inicializar la variable del tiempo
tiempo_inicio = None


def barbero():
    screen.blit(img_barbero, (barbero_x, barbero_y))


def persona(x, y):
    screen.blit(img_persona, (x, y))


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB de la pantalla
    screen.fill((255, 255, 255))

    for evento in pygame.event.get():
        # Evento para cerrar la ventana
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento para moverse a la ubicacion del barbero
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            persona_x = barbero_x
            persona_y = barbero_y
            tiempo_inicio = time.time()

    # LLamar a personajes
    barbero()
    persona(persona_x, persona_y)

    # Mostrar el tiempo transcurrido en la pantalla
    if tiempo_inicio:
        tiempo_transcurrido = int(time.time() - tiempo_inicio)
        tiempo_texto = f"Tiempo transcurrido: {tiempo_transcurrido} segundos"
        tiempo_fuente = pygame.font.Font(None, 20)
        tiempo_render = tiempo_fuente.render(tiempo_texto, True, (0, 0, 0))
        screen.blit(tiempo_render, (SCREEN_WIDTH - 220, 10))

    # Imprimir labels de instrucciones
    instrucciones_barbero_texto = "Tecla [b] para añadir barberos"
    instrucciones_persona_texto = "Tecla [p] para añadir personas"
    instrucciones_fuente = pygame.font.Font(None, 20)
    instrucciones_barbero_render = instrucciones_fuente.render(instrucciones_barbero_texto, True, (0, 0, 0))
    instrucciones_persona_render = instrucciones_fuente.render(instrucciones_persona_texto, True, (0, 0, 0))
    screen.blit(instrucciones_barbero_render, (30, 400))
    screen.blit(instrucciones_persona_render, (30, 420))

    pygame.display.update()

# Salir de Pygame
pygame.quit()
