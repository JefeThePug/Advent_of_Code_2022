"""
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. 
Instead, the Elves would like to know the number of pairs that overlap at 
all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't 
overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 
2-6,4-8) do overlap:

 - 5-7,7-9 overlaps in a single section, 7.
 - 2-8,3-7 overlaps all of the sections 3 through 7.
 - 6-6,4-6 overlaps in a single section, 6.
 - 2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

"""


def has_overlap(elf1: str, elf2: str) -> bool:
    s1, e1 = map(int,elf1.split("-"))
    s2, e2 = map(int,elf2.split("-"))
    return bool(set(range(s1, e1+1)).intersection(range(s2, e2+1)))

def sum_overlap(arr: list) -> int:
    return sum([has_overlap(*group.split(",")) for group in arr])

with open("input.txt") as f:
    print(sum_overlap(f.read().split("\n")[:-1]))

# Total overlaps: 841
