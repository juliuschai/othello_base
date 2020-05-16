# GUI for othello boards
from tkinter import *  # <-- Use Tkinter in Python 2.x

# Constants for colors
BLACK = 1
WHITE = 2

g_is_listening = False
g_valid_moves = []
g_cur_color = None
g_board_size = 8
g_canvas = None
g_root = Tk()
g_valid_move = None
waitVar = IntVar()


def init(board):
    global g_board_size, g_canvas
    g_board_size = len(board)

    # Start canvas initialization
    g_root.title("Othello")  # Your screen size may be different from 1270 x 780.
    frame = Frame(g_root, width=200, height=200)
    frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
    g_canvas = Canvas(frame, bg='#FFFFFF', width=200, height=200)
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=g_canvas.xview)
    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=g_canvas.yview)
    g_canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    g_canvas.pack(side=LEFT, expand=True, fill=BOTH)

    # Create board in canvas
    g_canvas.create_rectangle(0, 0, 75 * g_board_size, 75 * g_board_size,
                              width=1, fill='DARKGREEN')
    for i in range(1, g_board_size):  # draw vertical lines
        g_canvas.create_line(75 * i, 0, 75 * i, 75 * g_board_size, width=2, fill='BLACK')
    for i in range(1, g_board_size):  # draw horizontal lines
        g_canvas.create_line(0, 75 * i, 75 * g_board_size, 75 * i, width=2, fill='BLACK')

    points = g_canvas.bbox("all")
    g_canvas.config(width=points[2]-points[0], height=points[3]-points[1])
    g_canvas.config(scrollregion=g_canvas.bbox("all"))
    g_root.bind('<Button-1>', click)  # 1 = LEFT  mouse button.
    g_root.bind('<Button-3>', click)  # 3 = RIGHT mouse button.
    g_root.call('wm', 'attributes', '.', '-topmost', True)



def refresh_board(board, valid_moves, cur_color):
    global g_cur_color
    g_cur_color = cur_color

    move_coords = [valid_move["coordinate"] for valid_move in valid_moves]
    for i in range(g_board_size):
        for j in range(g_board_size):
            sx = j * 75 + 37.5
            sy = i * 75 + 37.5
            if board[i][j] == BLACK:
                g_canvas.create_oval(sx - 25, sy - 25, sx + 25, sy + 25, fill='BLACK')
            elif board[i][j] == WHITE:
                g_canvas.create_oval(sx - 25, sy - 25, sx + 25, sy + 25, fill='WHITE')
            elif (i, j) in move_coords:
                if g_cur_color == BLACK:
                    color = "#242"
                else:
                    color = "#ada"
                g_canvas.create_oval(sx - 25, sy - 25, sx + 25, sy + 25, fill=color)
            else:
                g_canvas.create_rectangle(sx - 30, sy - 30, sx + 30, sy + 30, width=0, fill='DARKGREEN')

    g_canvas.update()


def click(evt):
    global g_is_listening, g_valid_move
    if not g_is_listening:
        return

    move_coords = [valid_move["coordinate"] for valid_move in g_valid_moves]
    i = evt.y // 75
    j = evt.x // 75
    if (i, j) in move_coords:
        g_valid_move = g_valid_moves[move_coords.index((i, j))]
    else:
        return

    # Done listening
    g_is_listening = False
    waitVar.set(1)
    return


def start_listening(valid_moves, cur_color):
    global g_is_listening, g_valid_moves, g_cur_color
    g_is_listening = True
    g_valid_moves = valid_moves
    g_cur_color = cur_color


def get_choice():
    g_canvas.wait_variable(waitVar)
    return g_valid_move


# canvas = setUpCanvas(root)
# setUpInitialBoard(canvas)
# createMatrix2()
# copyMatrixToScreen()
# time.sleep(1)
# Button(root, text="Quit", command=root.destroy).pack()
# root.mainloop()
# root.mainloop()  # Now the graphics window waits for the click function to be called.


# def createOthelloBoard():
# canvas = setUpCanvas(root)
# root.mainloop()  # Now the graphics window waits for the click function to be called.


# def updateOthelloBoard():
