myinput = []
with open('input7.txt') as f:
    myinput = f.read().split(',')

myinput = [int(value) for value in myinput]

def part1(input):
    fuels = []
    curr_fuel = 0
    for align in range(len(input)):
        curr_fuel = 0
        for position in input:
            curr_fuel += abs(position - align)
        fuels.append(curr_fuel)
    return min(fuels)

# A hilariously slow brute force, that works.
def part2(input):
    fuels = []
    curr_fuel = 0
    for align in range(len(input)):
        curr_fuel = 0
        for position in input:
            curr_fuel += sum(range(1, abs(position - align) + 1))
        fuels.append(curr_fuel)
    return min(fuels)


print(part1(myinput))
print(part2(myinput))
