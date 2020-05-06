import copy
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


def finish_game(board):
    print('No more moves is available. Game is finished')
    black_count = 0
    white_count = 0
    for row in board:
        for cell in row:
            if cell == BLACK:
                black_count += 1
            elif cell == WHITE:
                white_count += 1

    if black_count > white_count:
        print("Black player wins")
    elif white_count > black_count:
        print("White player wins")
    else:
        print("Draw")


def print_choices(board, move_coords):
    for i, rows in enumerate(board):
        for j, cell in enumerate(rows):
            if (i, j) in move_coords:
                print(g_board_choices[i][j], end='')
            elif cell == WHITE:
                print('WW ', end='')
            elif cell == BLACK:
                print('BB ', end='')
            elif cell == 0:
                print('-- ', end='')
            else:
                print(cell, end='')
        print()


def get_choice(move_coords, valid_moves, color):
    choice = input()
    j = ord(choice[0]) - ord('a')
    i = ord(choice[1]) - ord('0')
    print(i, j)
    if (i, j) in move_coords:
        return valid_moves[move_coords.index((i, j))]
    else:
        print("That is not a valid move")
        return get_choice(move_coords, valid_moves, color)


# Returns the first available
def naive_ai(valid_moves):
    return valid_moves[0]


def move_over(mv_i, mv_j, diffI, diffJ):
    mv_i += diffI
    mv_j += diffJ
    return mv_i, mv_j


def is_in_range(i, j):
    return g_board_size > i >= 0 and g_board_size > j >= 0


def make_move(board, valid_move, color):
    def flip_direction(i, j, dir_tuple, player_color):

        diffI, diffJ = dir_tuple
        # Filp  until finding the same colored piece
        while is_in_range(i, j):
            if board[i][j] == player_color:
                break
            board[i][j] = player_color
            i, j = move_over(i, j, diffI, diffJ)

    print(valid_move)
    directions = valid_move['direction']
    (tmpI, tmpJ) = valid_move['coordinate']
    for direction in directions:
        flip_direction(tmpI, tmpJ, direction, color)


# check if cell is a valid move or not
# returns None if coordinate is not a valid move
# else returns
# result = [
#   coordinate: (int, int) valid move
#   amount: int  amount of enemy piece taken if move was made
#   direction: [] list of directions of enemy piece taken if move was made
# ]
def check_valid_move(board, color, coordinate):
    result = {"coordinate": coordinate, "amount": 0, "direction": []}

    # Returns 0 if move is invalid
    # else returns the amount of enemy piece taken if move is valid
    def check_line(i, j, direction):
        diffI, diffJ = direction
        i, j = move_over(i, j, diffI, diffJ)
        # If neighbor is in range and is enemy piece
        if is_in_range(i, j) and board[i][j] == enemy_color(color):
            i, j = move_over(i, j, diffI, diffJ)  # move 1 step
            count = 1
            same_color_found = False
            # find same colored piece
            while is_in_range(i, j):
                if board[i][j] == color:
                    same_color_found = True
                    break
                i, j = move_over(i, j, diffI, diffJ)
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


def get_valid_moves(board, color):
    res_moves = []
    for iRow, row in enumerate(board):
        for iCol, cell in enumerate(row):
            if cell != 0:
                continue
            move = check_valid_move(board, color, (iRow, iCol))
            if move is not None:
                res_moves.append(move)
    return res_moves


def print_board_helper(board, color):
    valid_moves = get_valid_moves(board, color)
    moves = [valid_move["coordinate"] for valid_move in valid_moves]
    print_choices(board, moves)


def minimax(board, cur_minimax_color):
    def evaluator(board, color):
        cur_score = 0
        for row in board:
            for cell in row:
                if cell == color:
                    cur_score += 1
        return cur_score

    def _minimax(cur_board, cur_color, cur_depth, isMax, alpha, beta, max_depth):
        print("max_depth: ", max_depth, "cur_depth: ", cur_depth)
        if max_depth == cur_depth:
            score = evaluator(cur_board, cur_minimax_color)
            return score, None

        valid_moves = get_valid_moves(cur_board, cur_color)
        if len(valid_moves) == 0:
            score = evaluator(cur_board, cur_minimax_color)
            return score, None

        if isMax:
            # print("Before max move")
            # print_board_helper(cur_board, cur_color)
            alpha_move = valid_moves[0]
            for i, move in enumerate(valid_moves):
                board_copy = copy.deepcopy(cur_board)

                make_move(board_copy, move, cur_color)
                # print_board_helper(board_copy, cur_color)
                # print("After max move")

                cur_score, cur_move = _minimax(board_copy, enemy_color(cur_color), cur_depth + 1, False, alpha, beta, max_depth)
                # print_minimax_move(cur_move)
                if cur_score > alpha:
                    alpha = cur_score
                    alpha_move = move
                if beta <= alpha:
                    return cur_score, None
            # print("Returned move with max")
            # print(alpha_move)
            return alpha, alpha_move
        else:
            # print("Before min move")
            # print_board_helper(cur_board, cur_color)
            beta_move = valid_moves[0]
            for i, move in enumerate(valid_moves):
                board_copy = copy.deepcopy(cur_board)

                make_move(board_copy, move, cur_color)
                # print_board_helper(board_copy, cur_color)
                # print("After min move")

                cur_score, cur_move = _minimax(board_copy, enemy_color(cur_color), cur_depth + 1, True, alpha, beta, max_depth)
                # print_minimax_move(cur_move)
                if beta > cur_score:
                    beta = cur_score
                    beta_move = move
                if beta <= alpha:
                    return cur_score, None
            # print("Returned move with min")
            # print(beta_move)
            return beta, beta_move
    # node = {'board': board, 'color': color, 'score': score, 'move_num': 1, 'valid_moves': valid_moves}
    best_score, best_move = _minimax(copy.deepcopy(board), cur_minimax_color, g_move_num, True, float("-inf"),
                                     float("inf"), g_depth + g_move_num)
    print(best_score, best_move)
    return best_move


print("Input board size")
# g_board_size = int(input())
g_board_size = 8
print("Input maximum depth for minimax value")
# g_depth = int(input())
g_depth = 4
# Print board state
g_board = [[0 for i in range(g_board_size)] for j in range(g_board_size)]
g_alphabet_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
g_board_choices = [["%c%d " % (g_alphabet_list[i], j) for i in range(g_board_size)] for j in range(g_board_size)]
g_board[3][3] = BLACK
# g_board[2][3] = BLACK
# g_board[1][4] = WHITE
g_board[4][4] = BLACK
g_board[3][4] = WHITE
g_board[4][3] = WHITE

# print(g_board[0][1])
cur_color = WHITE
g_move_num = 0
agent = {WHITE: "Minimax", BLACK: "Naive"} # Naive, Player, Minimax
while True:
    g_move_num += 1
    g_valid_moves = get_valid_moves(g_board, cur_color)
    moves = [valid_move["coordinate"] for valid_move in g_valid_moves]
    print_choices(g_board, moves)
    if len(g_valid_moves) == 0:
        if len(get_valid_moves(g_board, enemy_color(cur_color))) == 0:
            finish_game(g_board)
            break
        else:
            print('Currnet player have no more moves available')
            cur_color = enemy_color(cur_color)
            continue

    # Get choice
    if agent[cur_color] == "Naive":
        valid_move = naive_ai(g_valid_moves)
    elif agent[cur_color] == "Minimax":
        valid_move = minimax(g_board, cur_color)
        print("Done minimax")
        print(valid_move)
        # valid_move = naive_ai(g_valid_moves, cur_color)
    else:
        valid_move = get_choice(moves, g_valid_moves, cur_color)
    print("before making move")
    print_board_helper(g_board, cur_color)
    make_move(g_board, valid_move, cur_color)
    print("after making move")
    print_board_helper(g_board, cur_color)
    cur_color = enemy_color(cur_color)

