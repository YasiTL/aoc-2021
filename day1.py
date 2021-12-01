myinput = []
with open('input1.txt') as f:
    myinput = f.read().splitlines()

numbers = [int(x) for x in myinput]

def part1(count):
    count = 0
    for i in range(1, len(myinput)):
        if myinput[i-1] < myinput[i]:
            count += 1
    return count

def part2(input):
    count = 0
    for i in range(1, len(myinput)-2):
        window1 = input[i-1] + input[i] + input[i+1]
        window2 = input[i] + input[i+1] + input[i+2]
        if window1 < window2:
            count += 1
    return count

print(part1(numbers))
print(part2(numbers))