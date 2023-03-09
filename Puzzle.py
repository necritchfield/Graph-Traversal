from collections import deque

def in_bounds(Board, a, b):
    if a >= 0 and b >= 0 and a < len(Board) and b < len(Board[0]) and Board[a][b] == '-':
        return True
    else:
        return False


def find_routes(Board, a, b, x, y, route, routes):
    if not in_bounds(Board, a, b):
        return
    
    if (a, b) == (x, y):
        routes.append(route)
        return
    
    Board[a][b] = '#'

    if in_bounds(Board, a - 1, b):
        find_routes(Board, a - 1, b, x, y, route + 'U', routes)
    if in_bounds(Board, a + 1, b):
        find_routes(Board, a + 1, b, x, y, route + 'D', routes)
    if in_bounds(Board, a, b - 1):
        find_routes(Board, a, b - 1, x, y, route + 'L', routes)
    if in_bounds(Board, a, b + 1):
        find_routes(Board, a, b + 1, x, y, route + 'R', routes)

    Board[a][b] = '-'

def get_coordinates(route, a, b, x, y):
    coordinates = deque([])
    coordinates.appendleft((x, y))
    for i in range(len(route),0,-1):
        if(route[i - 1] == 'U'):
            coordinates.appendleft((x + 1, y))
            x = x + 1
        if(route[i - 1] == 'D'):
            coordinates.appendleft((x - 1, y))
            x = x - 1
        if(route[i - 1] == 'L'):
            coordinates.appendleft((x, y + 1))
            y = y + 1
        if(route[i - 1] == 'R'):
            coordinates.appendleft((x, y - 1))
            y = y - 1
    coordinates = list(coordinates)
    return coordinates

def solve_puzzle(Board, Source, Destination):
    a = Source[0]
    b = Source[1]

    x = Destination[0]
    y = Destination[1]

    route = ""
    routes = []

    find_routes(Board, a, b, x, y, route, routes)

    if routes != []:
        result = routes[0]
        for i in range(0, len(routes)):
            if (len(routes[i]) < len(result)):
                result = routes[i]
        coordinates = get_coordinates(result, a, b, x, y)
    else:
        coordinates = None
        result = ""

    return coordinates, result

#Puzzle = [
#    ['-', '-', '-', '-', '-'],
#    ['-', '-', '#', '-', '-'],
#    ['-', '-', '-', '-', '-'],
#    ['#', '-', '#', '#', '-'],
#    ['-', '#', '-', '-', '-']
#]

#P2 = [
#    ['-'],
#    ['-'],
#    ['-'],
 #   ['#'],
 #   ['-']
#]

#print(solve_puzzle(P2,(0,0),(0,2)))