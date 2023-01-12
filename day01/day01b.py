"""
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized 
that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total 
Calories carried by the top three Elves carrying the most Calories. That way, even if 
one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), 
then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). 
The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those 
Elves carrying in total?

"""

def calorie_list(s: str) -> int:
    elf_load = [sum(map(int,i.split("\n"))) for i in s.split("\n\n")]
    return sorted(elf_load)[::-1]

def get_top_n(calories: list, n: int) -> int:
    return sum(calories[0:n])


with open("input.txt") as f:
    calories = calorie_list(f.read()[:-1])
    print(get_top_n(calories, 3))
    
#total is 193697