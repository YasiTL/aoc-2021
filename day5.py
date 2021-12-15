myinput = []
with open('input5.txt') as f:
    myinput = f.read().splitlines()

point_pairs = []
for line in myinput:
    pair = line.split('->')
    x1 = pair[0].split(',')
    p1 = [int(val) for val in x1]
    x2 = pair[1].split(',')
    p2 = [int(val) for val in x2]
    point_pairs.append([p1, p2])

def findOverlap(pairs):
    all_coords = set()
    overlap_count = 0
    duplicate_seen = set()
    for pair in pairs:
        x1 = pair[0][0]
        y1 = pair[0][1]
        x2 = pair[1][0]
        y2 = pair[1][1]
        if x1 == x2:
            y_min = min(y1, y2)
            y_max = max(y1, y2)
            while y_min <= y_max:
                if (x1, y_min) in all_coords and (x1, y_min) not in duplicate_seen:
                    duplicate_seen.add((x1,y_min))
                    overlap_count += 1
                else:
                    all_coords.add((x1, y_min))
                y_min += 1
        elif pair[0][1] == pair[1][1]:
            x_min = min(x1, x2)
            x_max = max(x1, x2)
            while x_min <= x_max:
                if (x_min, y1) in all_coords and (x_min, y1) not in duplicate_seen:
                    duplicate_seen.add((x_min, y1))
                    overlap_count += 1
                else:
                    all_coords.add((x_min, y1))
                x_min += 1
        else: #handle diagonal case for part 2
            diff = max(abs(x1 - x2), abs(y1 - y2))
            while diff >= 0:
                if (x1, y1) in all_coords and (x1, y1) not in duplicate_seen:
                    duplicate_seen.add((x1, y1))
                    overlap_count += 1
                else:
                    all_coords.add((x1, y1))
                if x1 > x2:
                    x1 -= 1
                else:
                    x1 += 1
                if y1 > y2:
                    y1 -= 1
                else:
                    y1 += 1
                diff -= 1 # decriment the difference counter
    return overlap_count
        
print(findOverlap(point_pairs))
