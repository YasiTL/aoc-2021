myinput = []
with open('input3.txt') as f:
    myinput = f.read().splitlines()

def part1(arr):
    total = [''] * len(arr[0])
    # for length first row
    g = ''
    e = ''
    for line in arr:
        for i in range(len(line)):
            total[i] += (str(line[i]))

    for col in total:
        if col.count('1') > col.count('0'):
            g += '1'
            e += '0'
        else:
            g += '0'
            e += '1'
    # solution 1
    # print(int(g,2) * int(e,2))
    return total

def part2(arr, index):
    if len(arr) == 1:
        print(arr)
        return arr[0]
    
    total = part1(arr)
    # flip between >= and < for 2 parts of solution
    if total[index].count('1') < total[index].count('0'):
        new_arr = []
        for e in arr:
            if e[index] == '1':
                new_arr.append(e)
        part2(new_arr, index + 1)
    else:
        new_arr = []
        for e in arr:
            if e[index] == '0':
                new_arr.append(e)
        part2(new_arr, index + 1)
       

print(part2(myinput, 0))

# yikes lmfao
print(int('010101101111', 2) * int('100110010111', 2))