myinput = []
with open('input9.txt') as f:
    myinput = f.read().splitlines()

mod_input = [list(line) for line in myinput]

for i in range(len(mod_input)):
    for j in range(len(mod_input[i])):
        mod_input[i][j] = int(mod_input[i][j])

print(len(mod_input))
def part1(mod_input):
    sum_risk_levels = 0
    coordinates_of_lows = []
    for i in range(len(mod_input)):
        for j in range(len(mod_input[i])):
            # check all 4 adjacencies.
            comparable = []
            if i > 0:
                # add top value to the comparable array
                comparable.append(mod_input[i-1][j])
            if i < len(mod_input) - 1:
                # add bottom value to the comparable array
                comparable.append(mod_input[i+1][j])
            if j > 0:
                # add left value to the comparable array
                comparable.append(mod_input[i][j-1])
            if j < len(mod_input[i]) - 1:
                # add right value to the comparable array
                comparable.append(mod_input[i][j+1])
            if mod_input[i][j] < min(comparable):
                sum_risk_levels += mod_input[i][j] + 1
                coordinates_of_lows.append([i, j])
    print("coordinates of lows", coordinates_of_lows)
    return sum_risk_levels

def findLowPoints(mod_input):
    coordinates_of_lows = []
    for i in range(len(mod_input)):
        for j in range(len(mod_input[i])):
            # check all 4 adjacencies.
            comparable = []
            if i > 0:
                # add top value to the comparable array
                comparable.append(mod_input[i-1][j])
            if i < len(mod_input) - 1:
                # add bottom value to the comparable array
                comparable.append(mod_input[i+1][j])
            if j > 0:
                # add left value to the comparable array
                comparable.append(mod_input[i][j-1])
            if j < len(mod_input[i]) - 1:
                # add right value to the comparable array
                comparable.append(mod_input[i][j+1])
            if mod_input[i][j] < min(comparable):
                coordinates_of_lows.append([i, j])
    coordinates_of_lows = [tuple(x) for x in coordinates_of_lows]
    return coordinates_of_lows

def returnAdjacent(mod_input, i, j):
    adjacent = []
    if i > 0:
        # add top value to the adjacent array
        adjacent.append([i-1, j])
    if i < len(mod_input) - 1:
        # add bottom value to the adjacent array
        adjacent.append([i+1, j])
    if j > 0:
        # add left value to the adjacent array
        adjacent.append([i,j-1])
    if j < len(mod_input[i]) - 1:
        # add right value to the adjacent array
        adjacent.append([i,j+1])
    adjacent = [tuple(x) for x in adjacent]
    return adjacent

def basinSearch(mod_input, starting):
    discovered = set()
    adjacency = returnAdjacent(mod_input, starting[0], starting[1])
    queue = [starting]

    while queue:
        current = queue.pop(0)
        for coord in returnAdjacent(mod_input, current[0], current[1]):
            value_at_coord = mod_input[coord[0]][coord[1]]
            if coord not in discovered and value_at_coord < 9:
                discovered.add(coord)
                queue.append(coord)
    return len(discovered)

def part2(mod_input):
    basin_totals = []
    low_points = findLowPoints(mod_input)
    for point in low_points:
        basin_totals.append(basinSearch(mod_input, point))
    basin_totals.sort(reverse=True)
    return basin_totals[0] * basin_totals[1] * basin_totals[2]

print(part1(mod_input))
print(part2(mod_input))