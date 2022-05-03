from random import randint


def printMap(map):
    for i in map:
        print(i)


def counter(map, x, y):
    cnt = 0

    if map[y - 1][x - 1] == 1:
        cnt += 1
    elif map[y - 1][x] == 1:
        cnt += 1
    elif map[y - 1][x + 1] == 1:
        cnt += 1
    elif map[y][x - 1] == 1:
        cnt += 1
    elif map[y][x + 1] == 1:
        cnt += 1
    elif map[y + 1][x - 1] == 1:
        cnt += 1
    elif map[y + 1][x] == 1:
        cnt += 1
    elif map[y + 1][x + 1] == 1:
        cnt += 1

    return cnt


def changeState(map, x, y):
    if map[x][y] == 0:
        map[x][y] = 1
    else:
        map[x][y] = 0

    return map


nbColumns = 10
nbLignes = 10

map = [[0 for i in range(nbColumns)] for j in range(nbLignes)]

printMap(map)

print("\n")

changeState(map, 1, 1)
changeState(map, 1, 2)

printMap(map)

for i in range(map):
    for j in range(i):
        print(counter(map, i, j))
