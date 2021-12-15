myinput = []
with open('input2.txt') as f:
    myinput = f.read().splitlines()

horizontal = 0
depth = 0
aim = 0

for i in myinput:
    i = i.split()
    if i[0] == 'forward':
        horizontal += int(i[1])
        depth += aim * int(i[1])
    elif i[0] == 'up':
        aim -= int(i[1])
    elif i[0] == 'down':
        aim += int(i[1])

print(horizontal * depth)