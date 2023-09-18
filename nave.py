import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triángulo Rotativo y Acelerado")

# Colores
WHITE = (255, 255, 255)

# Triángulo
x, y = WIDTH // 2, HEIGHT // 2
triangle_rotation = 0  # Ángulo de rotación inicial
rotation_speed = 2  # Velocidad de rotación en grados por fotograma
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
    if keys[pygame.K_RIGHT]:
        triangle_rotation += rotation_speed
    elif keys[pygame.K_LEFT]:
        triangle_rotation -= rotation_speed

    # Limite de ángulo de rotación
    triangle_rotation %= 360

    if keys[pygame.K_UP]:  # Invertido: ahora la flecha arriba acelera hacia adelante
        triangle_speed += acceleration
    elif keys[pygame.K_DOWN]:  # Invertido: ahora la flecha abajo desacelera o retrocede
        triangle_speed -= acceleration
    else:
        # Desaceleración cuando no se presionan las teclas
        if triangle_speed > 0:
            triangle_speed -= acceleration / 2
        elif triangle_speed < 0:
            triangle_speed += acceleration / 2

    # Actualizar posición y ángulo
    x += triangle_speed * math.sin(math.radians(triangle_rotation))
    y -= triangle_speed * math.cos(math.radians(triangle_rotation))  # El signo menos invierte la dirección

    # Límites de la ventana
    if x < 0:
        x = 0
        triangle_speed = 0
    elif x > WIDTH:
        x = WIDTH
        triangle_speed = 0
    if y < 0:
        y = 0
        triangle_speed = 0
    elif y > HEIGHT:
        y = HEIGHT
        triangle_speed = 0

    # Limpiar la pantalla
    win.fill(WHITE)

    # Dibujar el triángulo con rotación
    triangle_points = [(x, y - 20), (x - 20, y + 20), (x + 20, y + 20)]

    # Rotar el triángulo
    rotated_triangle = []
    for point in triangle_points:
        x_new = (point[0] - x) * math.cos(math.radians(triangle_rotation)) - (point[1] - y) * math.sin(
            math.radians(triangle_rotation)) + x
        y_new = (point[0] - x) * math.sin(math.radians(triangle_rotation)) + (point[1] - y) * math.cos(
            math.radians(triangle_rotation)) + y
        rotated_triangle.append((x_new, y_new))

    pygame.draw.polygon(win, (0, 0, 255), rotated_triangle)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad de fotogramas
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
