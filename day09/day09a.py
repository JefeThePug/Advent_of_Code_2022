"""
--- Day 9: Rope Bridge ---

This rope bridge creaks as you walk along it. You aren't sure how old it 
is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge 
which was carved out by the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to 
distract yourself by modeling rope physics; maybe you can even figure out 
where not to step.

Consider a rope with a knot at each end; these knots mark the head and the 
tail of the rope. If the head moves far enough away from the tail, the tail 
is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to 
model the positions of the knots on a two-dimensional grid. Then, by 
following a hypothetical series of motions (your puzzle input) for the 
head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in 
fact, the head (H) and tail (T) must always be touching (diagonally 
adjacent and even overlapping both count as touching):

  ....     ....     ....
  .TH.     .H..     .H.. (H covers T)
  ....     ..T.     ....

If the head is ever two steps directly up, down, left, or right from the 
tail, the tail must also move one step in that direction so it remains 
close enough:

.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -> ... -> .T.
...    .H.    .H.
...    ...    ...

Otherwise, if the head and tail aren't touching and aren't in the same row 
or column, the tail always moves one step diagonally to keep up:

.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -> ...H. -> ..TH.
.T...    .T...    .....
.....    .....    .....

You just need to work out where the tail goes as the head follows a series 
of motions. Assume the head and the tail both start at the same position, 
overlapping.

For example:

R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

This series of motions moves the head right four steps, then up four steps, 
then left three steps, then down one step, and so on. After each step, 
you'll need to update the position of the tail if the step means the head 
is no longer adjacent to the tail. Visually, these motions occur as follows 
(s marks the starting position as a reference point):

== Initial State ==
  ......
  ......
  ......
  ......
  H.....  (H covers T, s)

== R 4 ==
  ......     ......     ......     ......
  ......     ......     ......     ......
  ......     ......     ......     ......
  ......     ......     ......     ......
  TH....     sTH...     s.TH..     s..TH.
(T covers s)

== U 4 ==
  ......     ......     ......     ....H.
  ......     ......     ....H.     ....T.
  ......     ....H.     ....T.     ......
  ....H.     ....T.     ......     ......
  s..T..     s.....     s.....     s.....

== L 3 ==
  ...H..     ..HT..     .HT...
  ....T.     ......     ......
  ......     ......     ......
  ......     ......     ......
  s.....     s.....     s.....

== D 1 ==
  ..T...
  .H....
  ......
  ......
  s.....

== R 4 ==
  ..T...     ..T...     ......     ......
  ..H...     ...H..     ...TH.     ....TH
  ......     ......     ......     ......
  ......     ......     ......     ......
  s.....     s.....     s.....     s.....

== D 1 ==
  ......
  ....T.
  .....H
  ......
  s.....

== L 5 ==
  ......     ......     ......     ......     ......
  ....T.     ....T.     ......     ......     ......
  ....H.     ...H..     ..HT..     .HT...     HT....
  ......     ......     ......     ......     ......
  s.....     s.....     s.....     s.....     s.....

== R 2 ==
  ......     ......
  ......     ......
  .H....     .TH...
  ......     ......
  s.....     s.....
(H covers T)

After simulating the rope, you can count up all of the positions the tail 
visited at least once. In this diagram, s again marks the starting position 
(which the tail also visited) and # marks other positions the tail visited:

  ..##..
  ...##.
  .####.
  ....#.
  s###..

So, there are 13 positions the tail visited at least once.

Simulate your complete hypothetical series of motions. How many positions 
does the tail of the rope visit at least once?

"""


class Leader:
    def __init__(self):
        self.pos = [0, 0]
        
    def move(self, direction:list) -> None:
        for i in range(2):
            self.pos[i] += direction[i]

class Follower:
    def __init__(self):
        self.pos = [0, 0]
        self.direction = [0, 0]
        
    def move(self, opponent:list) -> list:
        if any(abs(self.pos[i] - opponent[i]) >1 for i in range(2)):
            for i in range(2):
                self.pos[i] += self.direction[i]
        
        for i in range(2):
                self.direction[i] = opponent[i] - self.pos[i]

        return self.pos

def get_instruction(i:str) -> tuple:
    listkey = {"U": [0,-1], "R": [1, 0], "D": [0, 1], "L": [-1, 0]}
    target, mult = i.split()
    return listkey[target], int(mult)
    

with open("input.txt") as f:
    instruc = f.read().split("\n")[:-1]

head = Leader()
tail = Follower()
tail_locations = set()
    
for i in instruc:
    target, mult = get_instruction(i)

    for _ in range(mult):
        head.move(target)
        tail_locations.add((*tail.move(head.pos),))

print(len(tail_locations))

#Positions Tail Visited: 6087
