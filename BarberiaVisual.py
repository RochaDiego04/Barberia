import pygame

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


def barbero():
    screen.blit(img_barbero, (barbero_x, barbero_y))


def persona():
    screen.blit(img_persona, (persona_x, persona_y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB de la pantalla
    screen.fill((255, 255, 255))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    # LLamar a personajes
    barbero()
    persona()

    pygame.display.update()


# Salir de Pygame
pygame.quit()