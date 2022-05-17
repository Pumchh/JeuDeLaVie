

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


def verifAroundBlock(map:list, x:int, y:int, width:int=1, height:int=1) -> int:
    """
    :param map: map where you set the new state
    :param x: coordinate x
    :param y: coordinate y
    :param width: width to analyse to the left and the right of the block
    :param height: height to analyse above and below the block
    :return: int: block around the block who are on state 1
    """
    coordoX = x - width
    coordoY = y - height
    count = 0

    for i in range(height*2+1):
        coordoY = y - height
        for j in range(width*2+1):

            if 0 <= coordoX < XMap and 0 <= coordoY < YMap:
                if map[coordoX][coordoY] == 1:
                    count += 1
            coordoY += 1
        coordoX += 1

    if map[x][y] == 1:
        return count - 1
    else:
        return count


def rules(map:list, x:int, y:int, comesLife:list=(3), stayAlive:list=(2, 3), analysisX:int=1, analysisY:int=1) -> None:
    """
    :param map: map to apply the rule
    :param x: coordinate x
    :param y: coordinate y
    :param comesLife: number of alive block needed to born
    :param stayAlive: number of alive boccks needed to stay alive
    :param analysisX: width to analyse to the left and the right of the block
    :param analysisY: height to analyse above and below the block
    :return: None
    """
    if map[x][y] == 0:
        if verifAroundBlock(map, x, y, analysisX, analysisY) in comesLife:
            setState(map, x, y)

    elif map[x][y] == 1:
        if verifAroundBlock(map, x, y, analysisX, analysisY) not in stayAlive:
            setState(map, x, y)

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

