"""
--- Part Two ---

As you walk up the hill, you suspect that the Elves will want to turn this 
into a hiking trail. The beginning isn't very scenic, though; perhaps you 
can find a better starting point.

To maximize exercise while hiking, the trail should start as low as 
possible: elevation a. The goal is still the square marked E. However, the 
trail should still be direct, taking the fewest steps to reach its goal. 
So, you'll need to find the shortest path from any square at elevation a to 
the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the 
square marked S that counts as being at elevation a). If you start at the 
bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with 
elevation a to the location that should get the best signal?

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
    
        #reversed bit of part 1
        if altitude-1 > grid[y][x]: return False
        return self.path[y][x] > self.val

    def fill_routes(self, grid:list) -> None:
        while self.options:
            pos_y, pos_x = pos = self.options.pop()
            if grid[pos_y][pos_x]==97: # 97 is ord("a")-the goal
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
    txt = data.replace("S","a").split("\n")[:-1]
grid =[[*map(ord,list(row))] for row in txt]
rows, cols = len(grid), len(grid[0])

#start at end
start_y,start_x = start = divmod(data.replace("\n","").find("E"), cols)
grid[start_y][start_x] = 122

path = Path(rows, cols, start)
while not path.completed:
    path.fill_routes(grid)
    if path.val == 448: break

print(path.val-1, "steps")

#Total steps : 446
