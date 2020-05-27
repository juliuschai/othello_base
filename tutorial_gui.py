from tkinter import *  # <-- Use Tkinter in Python 2.x
import os

wkDir = os.path.dirname(__file__)
g_canvas = None
g_root = Tk()


def init():
    global g_canvas
    # Start canvas initialization
    g_root.title("How To Play")  # Your screen size may be different from 1270 x 780.
    frame = Frame(g_root, width=200, height=200)
    frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
    g_canvas = Canvas(frame, bg='#FFFFFF', width=450, height=690)
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=g_canvas.xview)
    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=g_canvas.yview)
    g_canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    g_canvas.pack(side=LEFT, expand=True, fill=BOTH)

    # Create content in canvas
    lastYPos = 0
    g_canvas.create_text(
        5, lastYPos,
        fill="black", font="Times 12", anchor=NW,
        text="Berikut adalah default starting point dari game othello.\n"
             "Masing-masing lingkaran menampilkan piece othello.")
    img = PhotoImage(master=g_canvas, file=os.path.join(wkDir, 'assets/tutorial/default_start_othello_board_state.png'))
    g_canvas.img1 = img
    lastYPos += 40
    g_canvas.create_image(0, lastYPos, anchor=NW, image=img)

    lastYPos += 80
    g_canvas.create_text(
        5, lastYPos,
        fill="black", font="Times 12", anchor=NW,
        text="Berikut adalah tampilan pertama untuk game othello,\n"
             "jika human player adalah warna putih")
    img = PhotoImage(master=g_canvas, file=os.path.join(wkDir, 'assets/tutorial/start_board_state.png'))
    g_canvas.img2 = img
    lastYPos += 40
    g_canvas.create_image(0, lastYPos, anchor=NW, image=img)

    lastYPos += 150
    g_canvas.create_text(
        5, lastYPos,
        fill="black", font="Times 12", anchor=NW,
        text="Lingkaran semi-transparant menandakan possible move human player.")
    img = PhotoImage(master=g_canvas, file=os.path.join(wkDir, 'assets/tutorial/white_possible_move_othello_piece.png'))
    g_canvas.img3 = img
    lastYPos += 20
    g_canvas.create_image(0, lastYPos, anchor=NW, image=img)
    img = PhotoImage(master=g_canvas, file=os.path.join(wkDir, 'assets/tutorial/black_possible_move_othello_piece.png'))
    g_canvas.img4 = img
    g_canvas.create_image(100, lastYPos, anchor=NW, image=img)

    lastYPos += 120
    g_canvas.create_text(
        5, lastYPos,
        fill="black", font="Times 12", anchor=NW,
        text="Terdapat Minimax AI GUI display yang menampilkan\n"
             "tahap decision-making dari minimax AI dengan\n"
             "alpha-beta pruning. board yang berwarna hijau\n"
             "adalah state board dikalkulasi dan dilalui oleh AI\n"
             "Setiap board memiliki score, menampilkan score\n"
             "dari board state tersebut, terkalkulasi oleh minimax.")
    img = PhotoImage(master=g_canvas, file=os.path.join(wkDir, 'assets/tutorial/minimax_board_state.png'))
    g_canvas.img5 = img
    lastYPos += 120
    g_canvas.create_image(0, lastYPos, anchor=NW, image=img)

    lastYPos += 140
    g_canvas.create_text(
        5, lastYPos,
        fill="black", font="Times 12", anchor=NW,
        text="Board yang berwarna merah adalah\n"
             "state board yang di prune oleh alpha-beta pruning.")
    img = PhotoImage(master=g_canvas, file=os.path.join(wkDir, 'assets/tutorial/minimax_pruned_state.png'))
    g_canvas.img6 = img
    lastYPos += 40
    g_canvas.create_image(0, lastYPos, anchor=NW, image=img)

    lastYPos += 170
    g_canvas.create_text(
        5, lastYPos,
        fill="black", font="Times 12", anchor=NW,
        text="Setting Human player atau AI player dapat dilakukan di main.\n"
             "- Untuk human player gunakan kata \"Player\".\n"
             "- Untuk minimax AI gunakan \"Minimax\"\n"
             "- Terdapat AI \"Naive\" yang memilih possible move\n"
             "	pertama disortir per baris terkiri.")
    img = PhotoImage(master=g_canvas, file=os.path.join(wkDir, 'assets/tutorial/agent_option_main_py.png'))
    g_canvas.img7 = img
    lastYPos += 80
    g_canvas.create_image(0, lastYPos, anchor=NW, image=img)

    lastYPos += 120
    g_canvas.create_text(
        250, lastYPos,
        fill="black", font="Times 12",
        text="Selamat bermain!\n\n\n\n\n")

    # points = g_canvas.bbox("all")
    # g_canvas.config(width=points[2] - points[0], height=points[3] - points[1])
    g_canvas.config(scrollregion=g_canvas.bbox("all"))
    # g_root.call('wm', 'attributes', '.', '-topmost', True)
