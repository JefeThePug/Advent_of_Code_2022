"""
--- Part Two ---

Content with the amount of tree cover available, the Elves just need to 
know the best spot to build their tree house: they would like to be able to 
see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and 
right from that tree; stop if you reach an edge or at the first tree that 
is the same height or taller than the tree under consideration. (If a tree 
is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the 
rules above; the proposed tree house has large eaves to keep it dry, so 
they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

3 0 3 7 3
2 5[5]1 2
6 5 3 3 2
3 3 5 4 9
3 5 3 9 0

 - Looking up, its view is not blocked; it can see 1 tree (of height 3).
 - Looking left, its view is blocked immediately; it can see only 1 tree 
   (of height 5, right next to it).
 - Looking right, its view is not blocked; it can see 2 trees.
 - Looking down, its view is blocked eventually; it can see 2 trees (one 
   of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance 
in each of the four directions. For this tree, this is 4 (found by 
multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the 
middle of the fourth row:

3 0 3 7 3
2 5 5 1 2
6 5 3 3 2
3 3[5]4 9
3 5 3 9 0

 - Looking up, its view is blocked at 2 trees (by another tree with a 
   height of 5).
 - Looking left, its view is not blocked; it can see 2 trees.
 - Looking down, its view is also not blocked; it can see 1 tree.
 - Looking right, its view is blocked at 2 trees (by a massive tree of 
   height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for 
the tree house.

Consider each tree on your map. What is the highest scenic score possible 
for any tree?

"""

from math import prod


def up(grid: list, n:tuple) -> int:
    col, row = n
    total = 1
    for x in grid[:col][::-1]:
        if x[row] >= grid[col][row]: break
        total += 1
    return total

def down(grid: list, n:tuple) -> int:
    col, row = n
    total = 1
    for x in grid[col + 1:]:
        if x[row] >= grid[col][row]: break
        total += 1
    return total

def left(grid: list, n:tuple) -> int:
    col, row = n
    total = 1
    for x in grid[col][:row][::-1]:
        if x >= grid[col][row]: break
        total += 1
    return total

def right(grid: list, n:tuple) -> int:
    col, row = n
    total = 1
    for x in grid[col][row + 1:]:
        if x >= grid[col][row]: break
        total += 1
    return total

directions = [up, down, left, right]

def barrier_grid(grid:list) -> list:
    for i, row in enumerate(grid[1:-1], 1):
        grid[i] = ":" + row[1:-1] + ":"
        cap = [":"* len(grid)]
    return cap + grid[1:-1] + cap

with open("input.txt") as f:
    grid = barrier_grid(f.read().split("\n")[:-1])

scores = []
for col in range(1, len(grid) - 1):
    for row in range(1, len(grid[0]) - 1):
        scores.append(prod(f(grid,(col,row)) for f in directions))
        
print(max(scores))

# Highest Scenic Score : 574080
