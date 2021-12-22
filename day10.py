myinput = []
with open('input10.txt') as f:
    myinput = f.read().splitlines()

def part1(my_input):
    pairs = {')' : '(', ']':'[', '}':'{', '>':'<' }
    points = 0
    for line in my_input:
        stack = []
        for char in line:
            if char in pairs:
                # check that the end of the stack matches pairs [char]
                if stack[-1] != pairs[char]:
                    if char == ')':
                        points += 3
                    elif char == ']':
                        points += 57
                    elif char == '}':
                        points += 1197
                    elif char == '>':
                        points += 25137
                    break
                else:
                    stack.pop()
            else:
                stack.append(char)
    return points

def disgardCorrupted(my_input):
    altered_input = my_input.copy()
    pairs = {')':'(', ']':'[', '}':'{', '>':'<' }
    for line in my_input:
        stack = []
        for char in line:
            if char in pairs:
                # check that the end of the stack matches pairs [char]
                if stack[-1] != pairs[char]:
                    altered_input.remove(line)
                    break
                else:
                    stack.pop()
            else:
                stack.append(char)
    return altered_input

def getPointValue(stack):
    total_score = 0
    stack.reverse()
    for char in stack:
        score = total_score * 5
        if char == '(':
            score += 1
        elif char == '[':
            score += 2
        elif char == '{':
            score += 3
        elif char == '<':
            score += 4
        total_score = score
    return total_score


def part2(myinput):
    incomplete_lines = disgardCorrupted(myinput)
    total_scores = []
    for line in incomplete_lines:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{', '>':'<' }
        for char in line:
            if char in pairs:
                # check that the end of the stack matches pairs [char]
                stack.pop()
            else:
                stack.append(char)
        total_scores.append(getPointValue(stack))
    total_scores.sort()
    return total_scores[len(total_scores)//2]

print(part1(myinput))
print(part2(myinput))