from typing import final


myinput = []
with open('input8.txt') as f:
    myinput = f.read().splitlines()

mod_input = [line.split('|') for line in myinput]

def part1(input):
    easy_digit_count = 0
    for note in input:
        output = note[1].split()
        for signal in output:
            if len(signal) == 2 or len(signal) == 3 or len(signal) == 4 or len(signal) == 7:
                easy_digit_count += 1
    return easy_digit_count

def oneSet(input):
    for element in input:
        if len(element) == 2:
            return set(element)

def sevenSet(input, special1set):
    for element in input:
        if len(element) == 3:
            return set(element) - special1set

def fourSet(input, special1set):
    for element in input:
        if len(element) == 4:
            return set(element) - special1set

def eightSet(input, special1set, special4set, special7set):
    for element in input:
        if len(element) == 7:
            return set(element) - special1set - special4set - special7set

def decideNumber(shared_1_elements, shared_4_elements, shared_7_elements, shared_8_elements):
    # decide what the element is 
    if sum([shared_1_elements, shared_4_elements, shared_7_elements, shared_8_elements]) == 2:
        return 1
    elif sum([shared_1_elements, shared_4_elements, shared_7_elements, shared_8_elements]) == 3:
        return 7
    elif sum([shared_1_elements, shared_4_elements, shared_7_elements, shared_8_elements]) == 4:
        return 4
    elif sum([shared_1_elements, shared_4_elements, shared_7_elements, shared_8_elements]) == 7:
        return 8
    if shared_1_elements == 1 and shared_4_elements == 1 and shared_7_elements == 1 and shared_8_elements == 2:
        return 2
    elif shared_1_elements == 2 and shared_4_elements == 1 and shared_7_elements == 1 and shared_8_elements == 2:
        return 0
    elif shared_1_elements == 1 and shared_4_elements == 2 and shared_7_elements == 1 and shared_8_elements == 1:
        return 5
    elif shared_1_elements == 2 and shared_4_elements == 2 and shared_7_elements == 1:
        return 9
    elif shared_1_elements == 1 and shared_4_elements == 2 and shared_7_elements == 1 and shared_8_elements == 2:
        return 6 # uses special 8 segment
    else:
        return 3
    


def part2(input):
    sum_all_entries = 0
    for note in input:
        # content input before the | and after
        in_notes = note[0].split()
        out_notes = note[1].split()
        # special sets that describe unique segments 1, 7 and 4 
        special_1 = oneSet(in_notes) # size 2
        special_4 = fourSet(in_notes, special_1) # size 2
        special_7 = sevenSet(in_notes, special_1) # size 1
        special_8 = eightSet(in_notes, special_1, special_4, special_7)
        decoding_dict = {}
        for signal in in_notes:
            shared_1_elements = 0
            shared_4_elements = 0
            shared_7_elements = 0 # really can only ever be 0 or 1, but for continuity var is included
            shared_8_elements = 0
            for segment in signal:
                if segment in special_1:
                    shared_1_elements += 1
                if segment in special_4:
                    shared_4_elements += 1
                if segment in special_7:
                    shared_7_elements += 1
                if segment in special_8:
                    shared_8_elements += 1
            decided_num = decideNumber(shared_1_elements, shared_4_elements, shared_7_elements, shared_8_elements)
            # Key is the signal, value is the decided number it equals
            decoding_dict[''.join(sorted(signal))] = decided_num
        
        final_display = ''
        for signal in out_notes:
            final_display = final_display + str(decoding_dict[''.join(sorted(signal))])
        sum_all_entries += int(final_display)
    return sum_all_entries

print(part1(mod_input))
print(part2(mod_input))