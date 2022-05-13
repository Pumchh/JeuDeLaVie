

def genMap(x:int, y:int) -> list:
    """
    :param x: number of columns
    :param y: numbers of lignes
    :return: map with the size x and y
    """
    _map = [[0 for i in range(x)] for j in range(y)]
    return _map


def printMap(map:list) -> None:
    """
    :param map: map to print
    :return: None
    """
    cara = ""
    for i in map:
        cara += "\n"
        for j in i:
            if j == 0:
                cara += "-"
            elif j == 1:
                cara += "*"
    print(cara)

def setState(map:list, x:int, y:int) -> None:
    """
    :param map: map where you set the new state
    :param x: coordinate x
    :param y: coordinate y
    :return: None
    """
    if map[x][y] == 0:
        map[x][y] = 1
    else:
        map[x][y] = 0


"""       
def verifAroundBlock(map:list, x:int, y:int, hight:int=1, width:int=1) -> int:
    coordoX = x - width 
    coordoY = y - hight 
    count = 0
  
    for i in range(hight*2+1):
        coordoY += 1
        coordoX = x - width
        for j in range(width*2+1):
            coordoX += 1
            if coordoX >= 0 and coordoY >= 0 and coordoX < XMap and coordoY < YMap:
                if map[coordoX][coordoY] == 1 and i != j:
                    count += 1
    return count
"""

# AJouter conditions bords du tableau
def verifAroundBlock(map:list, x:int, y:int) -> int:
    counter = 0

    if y > 1 and x > 1:
        if map[y - 1][x - 1] == 1:
            counter += 1

    if x > 1:
        if map[y][x - 1] == 1:
            counter += 1

    if y < YMap-1 and x > 1:
        if map[y + 1][x - 1] == 1:
            counter += 1

    if y > 1:
        if map[y - 1][x] == 1:
            counter += 1

    if y < YMap-1:
        if map[y + 1][x] == 1:
            counter += 1

    if y > 1 and x < XMap-1:
        if map[y - 1][x + 1] == 1:
            counter += 1

    if x < XMap-1:
        if map[y][x + 1] == 1:
            counter += 1

    if x < XMap-1:
        if map[y + 1][x + 1] == 1:
            counter += 1

    return counter


def rules(map, x, y):

    if map[x][y] == 0:
        if verifAroundBlock(map, x, y) == 3:
            setState(map, x, y)

    elif map[x][y] == 1:
        if verifAroundBlock(map, x, y) <= 2 or verifAroundBlock(map, x, y) >= 4:
            setState(map, x, y)

        elif verifAroundBlock(map, x, y) == 2 or verifAroundBlock(map, x, y) == 3:
            #pas de changement
            pass
    else:
        print("Erreur, ne sait pas quoi faire aux coord ({},{})".format(x, y))


XMap = 6
YMap = 6

map = genMap(XMap, YMap)

printMap(map)


setState(map, 3, 3)

print("\n")

printMap(map)

print(verifAroundBlock(map, 4, 4))

