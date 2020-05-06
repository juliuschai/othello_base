from tkinter import *  # <-- Use Tkinter in Python 2.x
import time


def createMatrix():  # = the initial position, with Black = 1, and white = -1.
    global M
    M = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 1, 0, 0, 0],
        [0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return M


def createMatrix2():  # = the initial position, with Black = 1, and white = -1.
    global M
    M = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return M


def setUpCanvas(root):  # These are the REQUIRED magic lines to enter graphics mode.
    root.title("Othello")  # Your screen size may be different from 1270 x 780.
    canvas = Canvas(root, width=1400, height=780, bg='GREY30')
    canvas.pack(expand=YES, fill=BOTH)
    return canvas


def copyMatrixToScreen():
    canvas.create_text(30, 30, text="x", fill='BLACK', font=('Helvetica', 1))
    for r in range(8):
        for c in range(8):
            if M[r][c] == 1:
                sx = c * 70 + 85
                sy = r * 70 + 105
                canvas.create_oval(sx - 25, sy - 25, sx + 25, sy + 25, fill='BLACK')
            if M[r][c] == -1:
                sx = c * 70 + 85
                sy = r * 70 + 105
                canvas.create_oval(sx - 25, sy - 25, sx + 25, sy + 25, fill='WHITE')
    canvas.update()


def setUpInitialBoard(canvas):
    global M
    ch = chr(9679)

    # --print title
    canvas.create_text(330, 50, text="OTHELLO with AI",
                       fill='WHITE', font=('Helvetica', 20, 'bold'))
    # --print directions
    stng = "DIRECTIONS:\n1) Black (human) moves first. Click on any unoccupied cell.\n\
2) If a player cannot move, play passes to the opponent. \n3) Game ends when \
no legal move is possible.\n4) The player with the most colors on the board \
wins.\n5) A legal move MUST cause some pieces to turn color."
    canvas.create_text(810, 100, text=stng,
                       fill='WHITE', font=('Helvetica', 10, 'bold'))
    # --draw outer box, with red border
    canvas.create_rectangle(50, 70, 610, 630, width=1, fill='DARKGREEN')
    canvas.create_rectangle(47, 67, 612, 632, width=5, outline='RED')

    # --Draw 7 horizontal and 7 vertical lines to make the cells
    for n in range(1, 8):  # draw horizontal lines
        canvas.create_line(50, 70 + 70 * n, 610, 70 + 70 * n, width=2, fill='BLACK')
    for n in range(1, 8):  # draw vertical lines
        canvas.create_line(50 + 70 * n, 70, 50 + 70 * n, 630, width=2, fill='BLACK')

    # --Place gold lines to indicate dangerous area to play (optional).
    canvas.create_rectangle(47 + 73, 67 + 73, 612 - 73, 632 - 73, width=1, outline='GOLD')
    canvas.create_rectangle(47 + 2 * 71, 67 + 2 * 71, 612 - 2 * 71, 632 - 2 * 71, width=1, outline='GOLD')

    # --Place letters at bottom
    tab = " " * 7
    stng = 'a' + tab + 'b' + tab + 'c' + tab + 'd' + tab + 'e' + \
           tab + 'f' + tab + 'g' + tab + 'h'
    canvas.create_text(325, 647, text=stng, fill='DARKBLUE', font=('Helvetica', 20, 'bold'))

    # --Place digits on left side
    for n in range(1, 9):
        canvas.create_text(30, 35 + n * 70, text=str(n),
                           fill='DARKBLUE', font=('Helvetica', 20, 'bold'))
    # --copy matrix to screen.
    copyMatrixToScreen()

    # --Place score on screen
    (BLACK, WHITE) = (0, 0)
    stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
    canvas.create_text(800, 200, text=stng, fill='WHITE', font=('Helvetica', 20, 'bold'))
    stng = "Suggested reply (col, row): (c, 4)"
    canvas.create_text(755, 350, text=stng, fill='GREEN', font=('Helvetica', 10, 'bold'))


def click(evt):  # A legal move is guaranteed to exist.
    time.sleep(1)

root = Tk()
M = createMatrix()  # <-- No variable can be passed to the click function.
canvas = setUpCanvas(root)
setUpInitialBoard(canvas)
createMatrix2()
copyMatrixToScreen()
time.sleep(1)
root.mainloop()  # Now the graphics window waits for the click function to be called.
