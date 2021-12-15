myinput = []
with open('input6.txt') as f:
    myinput = f.read().split(',')

myinput = [int(value) for value in myinput]

# part 1 
def part1(myinput):
    days = 0
    today = myinput
    tomorrow = myinput
    while days < 80:
        for i in range(len(today)):
            if today[i] == 0:
                tomorrow[i] = 6
                tomorrow.append(8)
            else:
                tomorrow[i] = today[i] - 1
        days += 1
    return len(tomorrow)

def part2(fishes):
    days = 0
    state = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5:0, 6:0, 7:0, 8:0}
    for fish in fishes:
        state[fish] = state[fish] + 1
    print(state)
    tomorrow = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5:0, 6:0, 7:0, 8:0}
    while days < 256:
        for i in range(8, -1, -1):
            if i == 0:
                tomorrow[8] = state[0]
                tomorrow[6] = tomorrow[6] + state[0]
            else:
                tomorrow[i-1] = state[i]
        state = tomorrow.copy()
        days += 1
    return sum(state.values())

print(part2(myinput))