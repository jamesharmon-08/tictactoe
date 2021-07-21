# location on line where symbols go
#    (' 1 | 5 | 9 ')
import empty_board
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


player = ["X", "O"]
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def check_winners(board):
    winning_combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for i in range(len(winning_combos)):
        check1 = board[winning_combos[i][0]]
        check2 = board[winning_combos[i][1]]
        check3 = board[winning_combos[i][2]]
        if check1 != " " or check1 != " " or check1 != " ":
            if check1 == check2 == check3:
                return check1
    return False


def display_board(board):
    place = [1, 5, 9]
    
    line = [
        [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
        [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']
    ]
    separator = '---+---+---'

    for i in range(len(board)):
        if board[i] != ' ':
            line[i//3][place[i%3]] = board[i]
    cls()
    print(empty_board.empty_board)
    print("".join(line[0]))
    print(separator)
    print("".join(line[1]))
    print(separator)
    print("".join(line[2]))

print(empty_board.empty_board)
for i in range(9):
    location = int(input("Enter location "))
    board[location-1] = player[i % 2]
    display_board(board)
    winner = check_winners(board)
    if winner:
        print(f'The winner is {winner}')
        break

