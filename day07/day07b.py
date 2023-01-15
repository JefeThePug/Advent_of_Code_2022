"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the 
update, you need unused space of at least 30000000. You need to find a 
directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus 
the total amount of used space) is 48381165; this means that the size of 
the unused space must currently be 21618835, which isn't quite the 30000000 
required by the update. Therefore, the update still requires a directory 
with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

 - Delete directory e, which would increase unused space by 584.
 - Delete directory a, which would increase unused space by 94853.
 - Delete directory d, which would increase unused space by 24933642.
 - Delete directory /, which would increase unused space by 48381165.

Directories e and a are both too small; deleting them would not free up 
enough space. However, directories d and / are both big enough! Between 
these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on 
the filesystem to run the update. What is the total size of that directory?

"""


class Folder:
    def __init__(self, name:str) -> None:
        self.name = name
        self.contents = []
        self.folders = {}
    
    def add_file(self, val:int) -> None:
        self.contents.append(val)
    
    def add_folder(self, name:str) -> None:
        self.folders[name] = (Folder(name))
        
    def getsum(self) -> int:
        return sum(self.contents) + sum(f.getsum() for f in self.folders.values())


def get_contents(cmds:list) -> dict:
    base = Folder("base")
    active = [base]
    all_dirs = {base}
    
    for cmd in cmds:
        match cmd.split():
            case "$","cd", d:
                if d == "/": continue
                elif d == "..": active.pop()
                else: 
                    folder = active[-1].folders[f"{active[-1].name}/{d}"]
                    all_dirs.add(folder)
                    active.append(folder)
            case "$","ls":
                continue
            case "dir", d:
                active[-1].add_folder(f"{active[-1].name}/{d}")
            case n, _:
                active[-1].add_file(int(n))
                
    return {d.name:d.getsum() for d in all_dirs}


with open("input.txt") as f:
    totals = get_contents(f.read().split("\n")[:-1])
needed = max(totals.values()) - 40000000
print(min((t-needed,t) for t in totals.values() if t > needed)[1])

# Total size af all large directories: 3579501
