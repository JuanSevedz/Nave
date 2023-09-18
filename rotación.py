import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triángulo Rotativo")

# Colores
WHITE = (255, 255, 255)

# Triángulo
x, y = WIDTH // 2, HEIGHT // 2
triangle_rotation = 0  # Ángulo de rotación inicial
rotation_speed = 2  # Velocidad de rotación en grados por fotograma

# Bucle principal de juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Manejo de teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:  # Invertido: ahora la flecha derecha rota a la izquierda
        triangle_rotation += rotation_speed
    elif keys[pygame.K_LEFT]:  # Invertido: ahora la flecha izquierda rota a la derecha
        triangle_rotation -= rotation_speed

    # Limite de ángulo de rotación
    triangle_rotation %= 360

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