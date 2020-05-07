# Show minimax steps
from tkinter import *  # <-- Use Tkinter in Python 2.x
from othello_constants import *

g_root = None
g_canvas = None

g_show_steps = False
g_cur_color = None
g_board_size = 0
g_tile_size = 20

minimax_coords = {}


# GUI for showing minimax ai path
def init():
    global g_root, g_canvas
    g_root = Tk()
    # Start canvas initialization
    g_root.title("Minimax AI Steps")  # Your screen size may be different from 1270 x 780.
    frame = Frame(g_root, width=20, height=20)
    frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
    g_canvas = Canvas(frame, bg='#FFFFFF', width=1280, height=600)
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=g_canvas.xview)
    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=g_canvas.yview)
    g_canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    g_canvas.pack(side=LEFT, expand=True, fill=BOTH)


debug_index = 0

def add_minimax_board(board, level, is_pruned):
    global g_board_size, debug_index
    debug_index += 1
    level += 1
    xOffset = (g_board_size+1) * g_tile_size
    yOffset = (g_board_size+1) * g_tile_size
    if level == 1:
        g_board_size = len(board)
        minimax_coords[level] = 0
        draw_board(board, 0, 0, is_pruned)
    # If index out of range
    elif len(minimax_coords) < level:
        minimax_coords[level] = minimax_coords[level-1]
        draw_board(board, minimax_coords[level], yOffset*(level-1), is_pruned)
    else:
        minimax_coords[level] = minimax_coords[level] + xOffset
        for i in range(level, 1, -1):
            minimax_coords[i-1] = minimax_coords[i]
        if is_pruned:
            for i in range(level, len(minimax_coords)+1):
                minimax_coords[i+1] = minimax_coords[i]
        draw_board(board, minimax_coords[level], yOffset*(level-1), is_pruned)


def draw_board(board, start_x, start_y, is_pruned):
    # Start drawing board
    board_color = 'DARKGREEN' if is_pruned is False else 'DARKRED'
    g_canvas.create_rectangle(
        start_x, start_y,
        start_x + g_tile_size * g_board_size, start_y + g_tile_size * g_board_size,
        width=1, fill=board_color)
    for i in range(1, g_board_size):  # draw vertical lines
        g_canvas.create_line(
            start_x + g_tile_size * i, start_y,
            start_x + g_tile_size * i, start_y + g_tile_size * g_board_size,
            width=1, fill='BLACK')
    for i in range(1, g_board_size):  # draw horizontal lines
        g_canvas.create_line(
            start_x, start_y + g_tile_size * i,
            start_x + g_tile_size * g_board_size, start_y + g_tile_size * i,
            width=1, fill='BLACK')

    # Start drawing othello piece
    for i in range(g_board_size):
        for j in range(g_board_size):
            sx = (j + 0.5) * g_tile_size + start_x
            sy = (i + 0.5) * g_tile_size + start_y
            if board[i][j] == BLACK:
                g_canvas.create_oval(
                    sx - g_tile_size/3, sy - g_tile_size/3,
                    sx + g_tile_size/3, sy + g_tile_size/3,
                    fill='BLACK')
            elif board[i][j] == WHITE:
                g_canvas.create_oval(
                    sx - g_tile_size/3, sy - g_tile_size/3,
                    sx + g_tile_size/3, sy + g_tile_size/3,
                    fill='WHITE')

    # g_canvas.update()


def finish_board():
    global minimax_coords
    g_canvas.config(scrollregion=g_canvas.bbox("all"))
    minimax_coords = {}
