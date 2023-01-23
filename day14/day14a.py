"""
--- Day 14: Regolith Reservoir ---

The distress signal leads you to a giant waterfall! Actually, hang on - the 
signal seems like it's coming from the waterfall itself, and that doesn't 
make any sense. However, you do notice a little path that leads behind the 
waterfall.

Correction: the distress signal leads you behind a giant waterfall! There 
seems to be a large cave system here, and the signal definitely leads 
further inside.

As you begin to make your way deeper underground, you feel the ground 
rumble for a moment. Sand begins pouring into the cave! If you don't 
quickly figure out where the sand is going, you could quickly become 
trapped!

Fortunately, your familiarity with analyzing the path of falling material 
will come in handy here. You scan a two-dimensional vertical slice of the 
cave above you (your puzzle input) and discover that it is mostly air with 
structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y 
coordinates that form the shape of the path, where x represents distance to 
the right and y represents distance down. Each path appears as a single 
line of text in your scan. After the first point of each path, each point 
indicates the end of a straight horizontal or vertical line to be drawn 
from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

This scan means that there are two paths of rock; the first path consists 
of two straight lines, and the second path consists of three straight 
lines. (Specifically, the first path consists of a line of rock from 498,4 
through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:

  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.

Sand is produced one unit at a time, and the next unit of sand is not 
produced until the previous unit of sand comes to rest. A unit of sand is 
large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile 
immediately below is blocked (by rock or sand), the unit of sand attempts 
to instead move diagonally one step down and to the left. If that tile is 
blocked, the unit of sand attempts to instead move diagonally one step down 
and to the right. Sand keeps moving as long as it is able to do so, at each 
step trying to move down, then down-left, then down-right. If all three 
possible destinations are blocked, the unit of sand comes to rest and no 
longer moves, at which point the next unit of sand is created back at the 
source.

A - So, drawing sand that has come to rest as o, the first unit of sand 
simply falls straight down and then stops:
B - The second unit of sand then falls straight down, lands on the first 
one, and then comes to rest to its left:
C - After a total of five units of sand have come to rest, they form this 
pattern:
D - After a total of 22 units of sand:
E - Finally, only two more units of sand (●) can possibly come to rest:

      (A)          (B)          (C)          (D)          (E)
   ......+...   ......+...   ......+...   ......+...   ......+...
   ..........   ..........   ..........   ..........   ..........
   ..........   ..........   ..........   ......o...   ......o...
   ..........   ..........   ..........   .....ooo..   .....ooo..
   ....#...##   ....#...##   ....#...##   ....#ooo##   ....#ooo##
   ....#...#.   ....#...#.   ....#...#.   ....#ooo#.   ...●#ooo#.
   ..###...#.   ..###...#.   ..###...#.   ..###ooo#.   ..###ooo#.
   ........#.   ........#.   ......o.#.   ....oooo#.   ....oooo#.
   ......o.#.   .....oo.#.   ....oooo#.   ...ooooo#.   .●.ooooo#.
   #########.   #########.   #########.   #########.   #########.

Once all 24 units of sand shown above have come to rest, all further sand 
flows out the bottom, falling into the endless void. Just for fun, the path 
any new sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
●..........

Using your scan, simulate the falling sand. How many units of sand come to 
rest before sand starts flowing into the abyss below?

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
        if y>=bottom:
            break
                  
    return y>=bottom, grid

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
rockwidth = set(map(lambda x: int(x[:-1]), re.findall(r"\d+,", data)))
gridwidth = ceil((max(rockwidth) - min(rockwidth))/10)*10
offset = min(rockwidth) - 2
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

    

print(sand_count - 1)    

# Total Units of Sand : 897
