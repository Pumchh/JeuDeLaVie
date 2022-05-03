

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
    for i in map:
        print(i)


def setBlock(map:list, x:int, y:int) -> None:

    if map[x][y] == 0:
        map[x][y] = 1
    else:
        map[x][y] = 0
 


       
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



def regles():
    pass


XMap = 10
YMap = 10

map = genMap(XMap, YMap)

printMap(map)


setBlock(map, 4, 4)
setBlock(map, 4, 5)
setBlock(map, 4, 6)
setBlock(map, 5, 4)
setBlock(map, 5, 5)
setBlock(map, 5, 6)
setBlock(map, 6, 4)
setBlock(map, 6, 5)
setBlock(map, 6, 6)

print("\n")

printMap(map)

print(verifAroundBlock(map, 4, 4))

