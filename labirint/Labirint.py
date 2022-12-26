import pygame
import sys

pygame.init()

points = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

point_y = len(points)
point_x = len(points[0])

graf = [(1, 2), (2, 3), (2, 5), (3, 6), (6, 9), (4, 7), (7, 8), (4, 5), (5, 6)]

screen = pygame.display.set_mode((point_x * 150, point_y * 150))
screen.fill("white")
pygame.display.set_caption('Лабиринт')

for i in range(0, point_x):
    for h in range(0, point_y):
        pygame.draw.rect(screen, "black", (150 * i, 150 * h, 150, 150), 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
