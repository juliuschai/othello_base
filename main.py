BLACK = 1
WHITE = 2


def enemy_color(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def print_board():
    for val in board:
        print(val)


# check if cell is a valid move or not
def check_valid_move(color, cell):
    def check_line(i, j, diffI, diffJ):
        def move_over(i, j):
            i += diffI
            j += diffJ
            return i, j

        def is_in_range(i, j):
            return 8 > i >= 0 and 8 > j >= 0

        i, j = move_over(i, j)
        print("start: " , i , ":" , j)
        # If neighbor is in range and is enemy piece
        if is_in_range(i, j) and board[i][j] == enemy_color(color):
            # find same colored piece
            print(i, j)
            i, j = move_over(i, j)
            while is_in_range(i, j):
                print(i, j)
                if board[i][j] == color:
                    return True
                i, j = move_over(i, j)
        else:
            return False

    iStart, jStart = cell
    # up
    if check_line(iStart, jStart, 0, 1) is True:
        return True
    # right up
    elif check_line(iStart, jStart, 1, 1) is True:
        return True
    # right
    elif check_line(iStart, jStart, 1, 0) is True:
        return True
    # right down
    elif check_line(iStart, jStart, 1, 1) is True:
        return True
    # down
    elif check_line(iStart, jStart, 0, -1) is True:
        return True
    # left down
    elif check_line(iStart, jStart, -1, 1) is True:
        return True
    # left
    elif check_line(iStart, jStart, 1, 0) is True:
        return True
    # left up
    elif check_line(iStart, jStart, -1, -1) is True:
        return True
    else:
        return False


def get_valid_moves(color):
    valid_moves = []
    for iRow, row in enumerate(board):
        for iCol, cell in enumerate(row):
            if check_valid_move(color, (iRow, iCol)):
                valid_moves.append((iRow, iCol))
    return valid_moves


board = [[0 for i in range(8)] for j in range(8)]
board[3][3] = BLACK
board[4][4] = BLACK
board[3][4] = WHITE
board[4][3] = WHITE

# print(board[0][1])
print_board()
valid_moves = get_valid_moves(WHITE)
print(valid_moves)
