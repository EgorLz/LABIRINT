import pygame
import sys

pygame.init()

count_of_points = 9

points = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

point_y = len(points)
point_x = len(points[0])

graf = [[2, 4], [1, 3, 5], [2, 9], [1, 5], [2, 4, 6], [3, 5, 9], [8], [7, 9], [6, 8]]
no_reb = [[4, 7], [5, 8]]

screen = pygame.display.set_mode((point_x * 150, point_y * 150))
screen.fill("white")
pygame.display.set_caption('Лабиринт')

def draw():
    screen.fill("white")
    for i in range(0, point_x):
        for h in range(0, point_y):
            pygame.draw.rect(screen, "black", (150 * i, 150 * h, 150, 150), 2)

    for i in range(0, len(no_reb)):
        first = int(no_reb[i][0])
        end = int(no_reb[i][1])
        if end - first == 3:
            pygame.draw.line(screen, "black", [((end % point_x) - 1) * 150, 150 * (end // point_y)], [(end % point_x) * 150, 150 * (end // point_y)], 8)
draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                draw()
                x = event.pos[0] // 150
                y = event.pos[1] // 150
                pos = [x * 150 + 75, y * 150 + 75]
                pygame.draw.circle(
                    screen, "red", pos, 70)
                pygame.display.update()
    pygame.display.flip()
