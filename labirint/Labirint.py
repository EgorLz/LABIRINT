import pygame
import sys

pygame.init()

count_of_points = 9

points = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

point_y = len(points)
point_x = len(points[0])

graf = {1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5],
        5: [2, 4, 6],
        6: [3, 5, 9],
        7: [8],
        8: [7, 9],
        9: [6, 8]}

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


def dfs_paths(graph, start, end):
    way = [(start, [start])]  # (vertex, path)
    while way:
        (vertex, path) = way.pop()
        for next in set(graph[vertex]) - set(path):
            if next == end:
                yield path + [next]
            else:
                way.append((next, path + [next]))

def printp(path):
    for f in path:
        if f % 3 == 0:
            point_x = 2
            point_y = f // 3 - 1
        else:
            point_x = f % 3 - 1
            point_y = f // 3
        pygame.draw.rect(screen, "yellow", (150 * point_x + 5, 150 * point_y + 5, 142, 142))

def robot(x, y):
    pygame.draw.circle(
                    screen, "red", (x * 150 + 75, y * 150 + 75), 70)

def roboty(x, y):
    pygame.draw.circle(
                    screen, "yellow", (x * 150 + 75, y * 150 + 75), 70)


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
            if event.button == 2:
                draw()
                pygame.display.update()
            if event.button == 3:
                x_end = event.pos[0] // 150
                y_end = event.pos[1] // 150
                pygame.display.update()

                paths = list(dfs_paths(graf, points[y][x], points[y_end][x_end]))

                paths2 = []
                for i in paths:
                    paths2.append(len(i))
                path = paths[paths2.index(min(paths2))]

                draw()
                roboty(x, y)
                printp(path)
                robot(x_end, y_end)
                x, y = x_end, y_end
                pygame.display.update()
    pygame.display.flip()
