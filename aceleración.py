import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triángulo Acelerado")

# Colores
WHITE = (255, 255, 255)

# Triángulo
x, y = WIDTH // 2, HEIGHT // 2
triangle_speed = 0
acceleration = 0.1

# Bucle principal de juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Manejo de teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        triangle_speed -= acceleration
    elif keys[pygame.K_DOWN]:
        triangle_speed += acceleration
    else:
        # Desaceleración cuando no se presionan las teclas
        if triangle_speed > 0:
            triangle_speed -= acceleration / 2
        elif triangle_speed < 0:
            triangle_speed += acceleration / 2

    # Actualizar posición vertical del triángulo
    y += triangle_speed

    # Límites de la ventana
    if y < 0:
        y = 0
        triangle_speed = 0
    elif y > HEIGHT:
        y = HEIGHT
        triangle_speed = 0

    # Limpiar la pantalla
    win.fill(WHITE)

    # Dibujar el triángulo
    triangle_points = [(x, y - 20), (x - 20, y + 20), (x + 20, y + 20)]
    pygame.draw.polygon(win, (0, 0, 255), triangle_points)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad de fotogramas
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()