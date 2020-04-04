# Constants for colors
BLACK = 1
WHITE = 2
# Constants for directions
UP = (-1, 0)
UP_RIGHT = (-1, 1)
RIGHT = (0, 1)
DOWN_RIGHT = (1, 1)
DOWN = (1, 0)
DOWN_LEFT = (1, -1)
LEFT = (0, -1)
UP_LEFT = (-1, -1)


def enemy_color(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def print_board():
    for val in board:
        print(val)


# check if cell is a valid move or not
# returns None if coordinate is not a valid move
# else returns
# result = [
#   coordinate: (int, int) valid move
#   amount: int  amount of enemy piece taken if move was made
#   direction: [] list of directions of enemy piece taken if move was made
# ]
def check_valid_move(color, coordinate):
    result = {"coordinate": coordinate, "amount": 0, "direction": []}

    # Returns 0 if move is invalid
    # else returns the amount of enemy piece taken if move is valid
    def check_line(i, j, direction):
        diffI, diffJ = direction

        def move_over(i, j):
            i += diffI
            j += diffJ
            return i, j

        def is_in_range(i, j):
            return 8 > i >= 0 and 8 > j >= 0

        i, j = move_over(i, j)
        # If neighbor is in range and is enemy piece
        if is_in_range(i, j) and board[i][j] == enemy_color(color):
            i, j = move_over(i, j)  # move 1 step
            count = 1
            same_color_found = False
            # find same colored piece
            while is_in_range(i, j):
                if board[i][j] == color:
                    same_color_found = True
                    break;
                i, j = move_over(i, j)
                count += 1
            # done looping
            if same_color_found:
                # If there was a same colored piece, return the count
                return count
            else:
                # If there was no same colored piece, move is invalid
                return 0
        else:
            # If neighbor is not enemy piece, move is invalid
            return 0

    iStart, jStart = coordinate
    check_line_results = [
        check_line(iStart, jStart, UP),
        check_line(iStart, jStart, UP_RIGHT),
        check_line(iStart, jStart, RIGHT),
        check_line(iStart, jStart, DOWN_RIGHT),
        check_line(iStart, jStart, DOWN),
        check_line(iStart, jStart, DOWN_LEFT),
        check_line(iStart, jStart, LEFT),
        check_line(iStart, jStart, UP_LEFT)
    ]
    # Check move for every directions
    if check_line_results[0] > 0:
        result["amount"] += check_line_results[0]
        result["direction"].append(UP)
    if check_line_results[1] > 0:
        result["amount"] += check_line_results[1]
        result["direction"].append(UP_RIGHT)
    if check_line_results[2] > 0:
        result["amount"] += check_line_results[2]
        result["direction"].append(RIGHT)
    if check_line_results[3] > 0:
        result["amount"] += check_line_results[3]
        result["direction"].append(DOWN_RIGHT)
    if check_line_results[4] > 0:
        result["amount"] += check_line_results[4]
        result["direction"].append(DOWN)
    if check_line_results[5] > 0:
        result["amount"] += check_line_results[5]
        result["direction"].append(DOWN_LEFT)
    if check_line_results[6] > 0:
        result["amount"] += check_line_results[6]
        result["direction"].append(LEFT)
    if check_line_results[7] > 0:
        result["amount"] += check_line_results[7]
        result["direction"].append(UP_LEFT)

    if result["amount"] == 0:
        return None
    return result


def get_valid_moves(color):
    res_moves = []
    for iRow, row in enumerate(board):
        for iCol, cell in enumerate(row):
            move = check_valid_move(color, (iRow, iCol))
            if move is not None:
                res_moves.append(move)
    return res_moves


board = [[0 for i in range(8)] for j in range(8)]
board[3][3] = BLACK
board[2][3] = BLACK
board[1][4] = WHITE
board[4][4] = BLACK
board[3][4] = WHITE
board[4][3] = WHITE

# print(board[0][1])
print_board()
valid_moves = get_valid_moves(WHITE)
print(valid_moves)
