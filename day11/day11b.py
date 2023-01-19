"""
--- Part Two ---
You're worried you might not ever get your items back. So worried, in fact, 
that your relief that a monkey's inspection didn't damage an item no longer 
causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from 
reaching ridiculous levels. You'll need to find another way to keep your 
worry levels manageable.

At this rate, you might be putting up with these monkeys for a very long 
time - possibly 10000 rounds!

With these new rules, you can still figure out the monkey business after 
10000 rounds. Using the same example above:

== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
Monkey 0 inspected items 52166 times.
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
Monkey 3 inspected items 52013 times.

After 10000 rounds, the two most active monkeys inspected items 52166 and 
52013 times. Multiplying these together, the level of monkey business in 
this situation is now 2713310158.

Worry levels are no longer divided by three after each item is inspected; 
you'll need to find another way to keep your worry levels manageable. 
Starting again from the initial state in your puzzle input, what is the 
level of monkey business after 10000 rounds?

"""

import operator as op #add, mul, sub, truediv
from math import prod

class Monkey:
    BIGMOD = float("inf")
    
    def __init__(self, func:callable, n:int, test:int, monks:tuple, *args:int) -> None:
        self.items = []
        self.func = func
        self.n = n
        self.test = test
        self.monks = {True: monks[0], False: monks[1]}
        self.inspections = 0
        if args: self.add_items(*args)
        
    def add_items(self, *items:int) -> None:
        for item in items:
            self.items.append(self.func(item, self.n) % Monkey.BIGMOD)
            
    def pass_items(self) -> list:
        packages = [(self.monks[item%self.test==0], item) for item in self.items]
        self.items.clear()
        self.inspections += len(packages)
        return packages
    
    
def gather_monkey_data(s: str) -> Monkey:
    opers = {"+": op.add, "*": op.mul, "-": op.sub, "/": op.truediv}
    
    c = s.split("\n")
    args = [*map(int,c[1].split(":")[1].strip().split(","))]
    calc = c[2].split("=")[1].strip().split()
    if calc[0] == calc[-1]: func, n = pow, 2
    else: func, n = opers[calc[1]], int(calc[-1])
    test = int(c[3].split()[-1].strip())
    recip = (int(c[4].split()[-1].strip()),int(c[5].split()[-1].strip()))
    return Monkey(func, n, test, recip, *args)

with open("input.txt") as f:
    cmds = f.read().split("\n\n")

monkeys = [gather_monkey_data(cmd) for cmd in cmds]
Monkey.BIGMOD = prod([m.test for m in monkeys])

for x in range(10000):
    for monk in monkeys:
        package = monk.pass_items()
        for m,p in package:
            monkeys[m].add_items(p)

num_inspections = sorted([monk.inspections for monk in monkeys])[::-1]
print(op.mul(*num_inspections[:2]))

#Monkey Business Level is : 17408399184
