import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH = 800
HEIGHT = 600
FPS = 60  # частота обновления экрана (FPS)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Визуализация сортировки методом пузырька")

# Цвета
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Генерация случайного массива
def generate_array(size):
    return [random.randint(1, 100) for _ in range(size)]

# Сортировка методом пузырька с анимацией
def bubble_sort_animation(arr):
    n = len(arr)
    clock = pygame.time.Clock()
    for i in range(n):
        for j in range(0, n-i-1):
            # Обмен значений, если они в неправильном порядке
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            # Отображение изменений на экране
            draw_array(arr, j, j+1)
            clock.tick(FPS)  # Управляем скоростью сортировки

# Функция для рисования массива на экране
def draw_array(arr, highlighted1=None, highlighted2=None):
    SCREEN.fill(WHITE)
    bar_width = WIDTH // len(arr)

    for i, val in enumerate(arr):
        bar_height = (val / 100) * HEIGHT
        color = BLUE
        if i == highlighted1 or i == highlighted2:
            color = RED  # Подсветка элементов, которые меняются местами
        pygame.draw.rect(SCREEN, color, (i * bar_width, HEIGHT - bar_height, bar_width, bar_height))

    pygame.display.update()

# Основная функция
def main():
    array_size = 50  # Размер массива
    arr = generate_array(array_size)

    # Отображаем начальный массив
    draw_array(arr)

    # Главный цикл программы
    running = True
    started = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
                    bubble_sort_animation(arr)

        if not started:
            font = pygame.font.SysFont("Arial", 20)
            text = font.render("Нажмите SPACE для начала сортировки", True, BLACK)
            SCREEN.blit(text, (WIDTH // 4, HEIGHT // 2))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()