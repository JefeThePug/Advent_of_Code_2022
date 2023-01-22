"""
--- Part Two ---

Now, you just need to put all of the packets in the right order. Disregard 
the blank lines in your list of received packets.

The distress signal protocol also requires that you include two additional 
divider packets:

[[2]]
[[6]]

Using the same rules as before, organize all packets - the ones in your 
list of received packets as well as the two divider packets - into the 
correct order.

For the example above, the result of putting the packets in the correct 
order is:

[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]

Afterward, locate the divider packets. To find the decoder key for this 
distress signal, you need to determine the indices of the two divider 
packets and multiply them together. (The first packet is at index 1, the 
second packet is at index 2, and so on.) In this example, the divider 
packets are 10th and 14th, and so the decoder key is 140.

Organize all of the packets into the correct order. What is the decoder key 
for the distress signal?

"""

import ast


def compare(left, right) -> bool:
    if isinstance(left, list): 
        left.append("X")
    else:
        left = [left, "X"]
    if isinstance(right, list): 
        right.append("X")
    else:
        right = [right, "X"]
    parts = list(zip(left, right))
    
    for L, R in parts:
        if (isinstance(L, int) and isinstance(R, int)) or L=="X" or R=="X":
            if L == R: continue
            if L == "X": return True
            if R == "X": return False

            if L < R: return True
            if L > R: return False
        else:
            x = compare(L,R)
            if x is not None:
                return x


with open("input.txt") as f:
    data = f.read().replace("\n\n","\n").split("\n")[:-1]
data.append("[[2]]")
data.append("[[6]]")

sorted = False
while not sorted:
    sorted = True
    for i in range(0,len(data)-1):
        left = ast.literal_eval(data[i])
        right = ast.literal_eval(data[i+1])
        if not compare(left, right):
            sorted = False
            data[i], data[i+1] = data[i+1], data[i]

decoder_a = data.index("[[2]]")+1 
decoder_b = data.index("[[6]]")+1

print(decoder_a * decoder_b)

# Decoder key is : 26200     (Not the fastest code... Takes 15 seconds)
