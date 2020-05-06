import copy
from base_game import enemy_color, get_valid_moves, make_move

g_depth = None
g_move_num = None


def ai_init(depth):
    global g_depth
    g_depth = depth


def ai_start(move_num):
    global g_move_num
    g_move_num = move_num


# Returns the first available
def naive_ai(valid_moves):
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
                    return cur_score, None
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
                    return cur_score, None
            return beta, beta_move
    best_score, best_move = _minimax(copy.deepcopy(board), cur_minimax_color, g_move_num, True, float("-inf"),
                                     float("inf"), g_depth + g_move_num)
    return best_move


