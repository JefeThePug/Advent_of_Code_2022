"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river 
you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle 
input). The heightmap shows the local area from above broken into a grid; 
the elevation of each square of the grid is given by a single lowercase 
letter, where a is the lowest elevation, b is the next-lowest, and so on up 
to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and 
the location that should get the best signal (E). Your current position (S) 
has elevation a, and the location that should get the best signal (E) has 
elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps 
as possible. During each step, you can move exactly one square up, down, 
left, or right. To avoid needing to get out your climbing gear, the 
elevation of the destination square can be at most one higher than the 
elevation of your current square; that is, if your current elevation is m, 
you could step to elevation n, but not to elevation o. (This also means 
that the elevation of the destination square can be much lower than the 
elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You 
could start by moving down or right, but eventually you'll need to head 
toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each 
square moving up (^), down (v), left (<), or right (>). The location that 
should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the 
location that should get the best signal?

"""


class Path:
    def __init__(self, rows:int, cols:int, start:tuple) -> None:
        self.rows = rows
        self.cols = cols
        self.path = [[float("inf") for _ in range(cols)] for __ in range(rows)]
        s_y, s_x = start
        self.options = {(s_y, s_x)}
        self.next = set()
        self.val = 0
        self.completed = False
        
    def can_tred(self, grid:list, pos:tuple, target:tuple) -> bool:
        y, x = target
        altitude = grid[pos[0]][pos[1]]
        if any(target[i] < 0 for i in range(2)): return False
        if x >= self.cols or y >= self.rows: return False
        if self.path[y][x] < self.val: return False
        if altitude+1 < grid[y][x]: return False
        return self.path[y][x] > self.val

    def fill_routes(self, grid:list) -> None:
        while self.options:
            pos_y, pos_x = pos = self.options.pop()
            if grid[pos_y][pos_x]==123: # 123 is ord("{") which is the End position
                self.completed = True
            self.path[pos_y][pos_x] = self.val
            for n in [-1,1]:
                if self.can_tred(grid, pos, (pos_y, pos_x+n)):
                    self.next.add((pos_y, pos_x+n))
                if self.can_tred(grid, pos, (pos_y+n, pos_x)):
                    self.next.add((pos_y+n, pos_x))
            
        self.options, self.next = self.next, set()
        self.val += 1

    
    
with open("input.txt") as f:
    data = f.read()
    txt = data.replace("E","{").split("\n")[:-1]
grid =[[*map(ord,list(row))] for row in txt]
rows, cols = len(grid), len(grid[0])

start_y,start_x = start = divmod(data.replace("\n","").find("S"), cols)
grid[start_y][start_x] = 97

path = Path(rows, cols, start)
while not path.completed:
    path.fill_routes(grid)
    if path.val == 448: break

print(path.val-1, "steps")

#Total steps : 447
