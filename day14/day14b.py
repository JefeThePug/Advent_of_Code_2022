"""
--- Part Two ---

You realize you misread the scan. There isn't an endless void at the bottom 
of the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite 
horizontal line with a y coordinate equal to two plus the highest y 
coordinate of any point in your scan.

In the example above, the highest y coordinate of any point is 9, and so 
the floor is at y=11. (This is as if your scan contained one extra rock 
path like -infinity,11 -> infinity,11.) With the added floor, the example 
above now looks like this:

        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->

To find somewhere safe to stand, you'll need to simulate falling sand until 
a unit of sand comes to rest at 500,0, blocking the source entirely and 
stopping the flow of sand into the cave. In the example above, the 
situation finally looks like this after 93 units of sand come to rest:

............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################

Using your scan, simulate the falling sand until the source of the sand 
becomes blocked. How many units of sand come to rest?

"""

import re
from math import ceil


def drop(grid:list, bottom:int, offset:int) -> tuple:
    y,x = 0, 500-offset
    while True:        
        if grid[y+1][x] == ".":
            y += 1
        elif grid[y+1][x-1] == ".":
            y += 1
            x -= 1
        elif grid[y+1][x+1] == ".":
            y += 1
            x += 1
        else:
            grid[y][x] = "o"
            break
        if y==bottom:
            grid[y][x] = "o"
            break
                  
    return y==0, grid

def build_rocks(grid:list, path:list, offset:int) -> list:
    for part in range(len(path)-1):
        x1, y1 = map(int,path[part].split(","))
        x2, y2 = map(int,path[part+1].split(","))
        x1 -= offset
        x2 -= offset
        
        if x1 == x2: #horizontal line
            for i in range(min(y1,y2),max(y1,y2)+1):
                grid[i][x1] = "#"
        else:  #y1 == y2 vertical line
            for i in range(min(x1,x2),max(x1,x2)+1):
                grid[y1][i] = "#"
    return grid

        
with open("input.txt") as f:
    data = f.read().replace(" -> ","-")

# setup grid
rockbottom = 1 + max(map(lambda x: int(x[1:]), re.findall(r",\d+", data)))
gridwidth = 2*rockbottom+2
offset = 500-(gridwidth//2)
grid = [["."]*(gridwidth+4) for _ in range(rockbottom+3)]
grid[0][500-offset] = "+"

# build rocks
for line in data.split("\n"):
    grid = build_rocks(grid, line.split("-"), offset)

# fall sand
sand_count = 0
overflow = False
while not overflow:
    sand_count += 1
    overflow, grid = drop(grid, rockbottom, offset)
    
print(sand_count)    

# Total Units of Sand : 26683
