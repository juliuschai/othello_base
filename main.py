from ai import *
from base_game import *


print("Input board size")
g_board_size = int(input())
g_board_size = g_board_size//2*2
base_game_init(g_board_size)
print("Input maximum depth for minimax value")
g_depth = int(input())
ai_init(g_depth)

# Print board state
g_board = [[0 for i in range(g_board_size)] for j in range(g_board_size)]
g_board[3][3] = BLACK
g_board[4][4] = BLACK
g_board[3][4] = WHITE
g_board[4][3] = WHITE

cur_color = WHITE
g_move_num = 0
agent = {WHITE: "Player", BLACK: "Minimax"} # Naive, Player, Minimax
while True:
    g_move_num += 1
    g_valid_moves = get_valid_moves(g_board, cur_color)
    moves = [valid_move["coordinate"] for valid_move in g_valid_moves]
    print_choices(g_board, moves)
    # Check if game is finished
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
        print("Naive AI Move")
        ai_start(g_move_num)
        valid_move = naive_ai(g_valid_moves)
    elif agent[cur_color] == "Minimax":
        print("Minimax AI Move")
        ai_start(g_move_num)
        valid_move = minimax(g_board, cur_color)
        # valid_move = naive_ai(g_valid_moves, cur_color)
    else:
        print("Player Move")
        valid_move = get_choice(moves, g_valid_moves, cur_color)
    make_move(g_board, valid_move, cur_color)
    cur_color = enemy_color(cur_color)

