myinput = []
with open('input4.txt') as f:
    myinput = f.read().splitlines()

# Save called numbers, and remove it from the input along with the newline
called_numbers = myinput[0].split(',')
del myinput[0:2]

mod_input = [line.split() for line in myinput]
mod_input = [e for e in mod_input if e != []]

def convertToBoards(input):
    boards = []
    for i in range(0, len(input), 5):
        boards.append(input[i:i+5])
    return boards

def checkRows(board):
    for i in range(len(board)):
        num_called = 0
        for element in board[i]:
            if element == '!':
                num_called += 1
        if num_called == len(board[i]):
            return True
    return False

def checkCols(board):
    for i in range(len(board[0])):
        num_called = 0
        for j in range(len(board)):
            for element in board[j][i]:
                if element == '!':
                    num_called += 1
            if num_called == len(board):
                return True
    return False

def markBoard(board, called):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == called:
                board[i][j] = '!'
    return board

def sumUnmarked(board):
    total = 0
    for line in board:
        for element in line:
            if element != '!':
                total += int(element)
    return total

def checkBingoP1(input):
    boards = convertToBoards(input)
    min_called_to_solve = len(called_numbers) # index of the number that solved the bingo board
    sum_unmarked = 0
    for i in range(len(boards)):
        index_called = 0
        #solve each board, and put how mant iterations it took into the list
        board = markBoard(boards[i], called_numbers[index_called])
        while not checkRows(board) and not checkCols(board):
            index_called += 1
            board = markBoard(board, called_numbers[index_called])
        if min_called_to_solve >= index_called:
            min_called_to_solve = index_called
            sum_unmarked = sumUnmarked(board)
    return sum_unmarked * int(called_numbers[min_called_to_solve])

def checkBingoP2(input):
    boards = convertToBoards(input)
    max_called_to_solve = 0 # index of the number that solved the bingo board
    sum_unmarked = 0
    for i in range(len(boards)):
        index_called = 0
        board = markBoard(boards[i], called_numbers[index_called])
        while not checkRows(board) and not checkCols(board):
            index_called += 1
            board = markBoard(board, called_numbers[index_called])
        if max_called_to_solve < index_called:
            max_called_to_solve = index_called
            sum_unmarked = sumUnmarked(board)
    return sum_unmarked * int(called_numbers[max_called_to_solve])
    
# cant run both, input is mutated from part 1 to part 2
# print(checkBingoP1(mod_input))
print(checkBingoP2(mod_input))