# Naive and Minimax AI for othello
import copy
from base_game import enemy_color, get_valid_moves, make_move
import ai_gui

g_depth = None
g_move_num = None
g_show_steps = False


def init(depth, show_steps):
    global g_depth, g_show_steps
    g_depth = depth
    g_show_steps = show_steps


def start(move_num):
    global g_move_num
    g_move_num = move_num


# Returns the first available
def naive(valid_moves):
    return valid_moves[0]


def minimax(board, cur_minimax_color):
    def evaluator(board, color):
        cur_score = 0
        for row in board:
            for cell in row:
                if cell == color:
                    cur_score += 1
        return cur_score

    def _minimax(cur_board, cur_color, cur_depth, isMax, alpha, beta, max_depth):
        if max_depth == cur_depth:
            score = evaluator(cur_board, cur_minimax_color)
            return score, None

        valid_moves = get_valid_moves(cur_board, cur_color)
        if len(valid_moves) == 0:
            score = evaluator(cur_board, cur_minimax_color)
            return score, None

        if g_show_steps:
            ai_gui.add_minimax_board(cur_board, cur_depth - g_move_num, False)

        if isMax:
            alpha_move = valid_moves[0]
            for i, move in enumerate(valid_moves):
                board_copy = copy.deepcopy(cur_board)
                make_move(board_copy, move, cur_color)

                cur_score, cur_move = _minimax(board_copy, enemy_color(cur_color), cur_depth + 1, False, alpha, beta, max_depth)
                # print_minimax_move(cur_move)
                if cur_score > alpha:
                    alpha = cur_score
                    alpha_move = move
                if beta <= alpha:
                    if g_show_steps and len(valid_moves)-1 > i:
                        board_copy2 = copy.deepcopy(cur_board)
                        make_move(board_copy2, valid_moves[i+1], cur_color)
                        ai_gui.add_minimax_board(board_copy2, cur_depth - g_move_num + 1, True)
                    return alpha, alpha_move
            return alpha, alpha_move
        else:
            beta_move = valid_moves[0]
            for i, move in enumerate(valid_moves):
                board_copy = copy.deepcopy(cur_board)
                make_move(board_copy, move, cur_color)

                cur_score, cur_move = _minimax(board_copy, enemy_color(cur_color), cur_depth + 1, True, alpha, beta, max_depth)
                # print_minimax_move(cur_move)
                if beta > cur_score:
                    beta = cur_score
                    beta_move = move
                if beta <= alpha:
                    # Go to next node
                    if g_show_steps and len(valid_moves)-1 > i:
                        board_copy2 = copy.deepcopy(cur_board)
                        make_move(board_copy2, valid_moves[i+1], cur_color)
                        ai_gui.add_minimax_board(board_copy2, cur_depth - g_move_num + 1, True)
                    return beta, beta_move
            return beta, beta_move

    if g_show_steps:
        ai_gui.init()

    best_score, best_move = _minimax(copy.deepcopy(board), cur_minimax_color, g_move_num, True, float("-inf"),
                                     float("inf"), g_depth + g_move_num)
    if g_show_steps:
        ai_gui.finish_board()
    return best_move


