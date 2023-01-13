"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice 
the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly 
wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air 
conditioning, leather seats, an extra cup holder, and the ability to pick 
up and move multiple crates at once.

Again considering the example above, the crates begin in the same 
configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
 
However, the action of moving three crates from stack 1 to stack 3 means 
that those three moved crates stay in the same order, resulting in this new 
configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
 
Next, as both crates are moved from stack 2 to stack 1, they retain their 
order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
 
Finally, a single crate is still moved from stack 1 to stack 2, but now 
it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
 
In this example, the CrateMover 9001 has put the crates in a totally 
different order: MCD.

Before the rearrangement process finishes, update your simulation so that 
the Elves know where they should stand to be ready to unload the final 
supplies. After the rearrangement procedure completes, what crate ends up 
on top of each stack?

"""


from itertools import filterfalse as ff

def set_stacks(s: str) -> list:
    s = s.split("\n")[:s.count("\n")-2]
    x = len(max(s, key=len))
    s = [[" "]+[line[i+1:i+2] or " " for i in range(0,x,4)] for line in s]
    s = list(zip(*s[::-1]))
    return [list(ff(str.isspace, i)) for i in s]
    
def execute(s: str, cmds: list) -> str:
    s = set_stacks(s)
    for cmd in cmds:
        a,b,c = [int(i) for i in cmd.split() if i.isdigit()]
        x = s[b][len(s[b])-a:]
        del s[b][len(s[b])-a:]
        s[c].extend(x)
    return "".join([n.pop() for n in s[1:]])


with open("input.txt") as file:
    f = file.read()

split = f.find("move")
s, cmd = f[:split],f[split:]
print(execute(s, cmd.split("\n")[:-1]))

#Result is MHQTLJRLB
