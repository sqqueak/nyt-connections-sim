import itertools
import pprint
spots = []

for i in range(4):
    for j in range(4):
        spots.append(f'{i}{j}')

counter = 0
grids = {}
rotate = {
    "00":"03",
    "01":"13",
    "02":"23",
    "03":"33",
    "10":"02",
    "11":"12",
    "12":"22",
    "13":"32",
    "20":"01",
    "21":"11",
    "22":"21",
    "23":"31",
    "30":"00",
    "31":"10",
    "32":"20",
    "33":"30"
}

def same(g1, g2):
    for i in range(4):
        for j in range(4):
            if g1[i][j] != g2[i][j]:
                return False
    return True

for item in itertools.combinations(spots, 4):
    grid = [[" " for x in range(4)] for y in range(4)]
    for cell in item:
        row, col = cell[0], cell[1]
        grid[int(row)][int(col)] = "*"

    if len(grids) > 0:
        counted = True

        ### ROTATIONS ###
        temp_item = list(item)
        for _ in range(4):
            for i,coordinate in enumerate(temp_item):
                temp_item[i] = rotate[coordinate]
            if tuple(sorted(temp_item)) in grids.keys():
                grids[tuple(sorted(temp_item))].append(grid)
                counted = False

        if counted:
            grids[tuple(sorted(item))] = [grid]
    else:
        grids[tuple(sorted(item))] = [grid]
    
pprint.pprint(grids)
print(len(grids))