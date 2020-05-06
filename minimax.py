def maxMove(board, depth, alpha, beta, PW, PB, MAXDEPTH):
    # def tuple[:,:] moves_view
    # def boardCopy
    # def int i

    moves = getMoves(HUMAN,board)

    if(moves.ndim>1):
        moves_view=moves
    else:
        return boardScore(board,PW,PB)

    # def DTYPE_t[:] scores=np.zeros(moves.shape[0], dtype=DTYPE)
    scores =
    if len(moves)==0:
        if depth<MAXDEPTH:
            return minMove(board, depth+1, alpha, beta, PW, PB, MAXDEPTH)
        else: return boardScore(board, PW, PB)

    for i, move in enumerate(moves):
        boardCopy=board.copy()
        boardCopy= fakeMove(move[0], move[1], LocateTurnedPieces(move[0], move[1], COMPUTER, boardCopy) , COMPUTER, boardCopy)
        if depth>=MAXDEPTH:
            scores[i] = boardScore(boardCopy, PW, PB)
        else:
            scores[i] = minMove(boardCopy, depth+1, alpha, beta, PW, PB, MAXDEPTH)
            if scores[i] > alpha:
                alpha = scores[i]
            if beta <= alpha:
                return scores[i]


    return max(scores)

def minMove(board, depth, alpha, beta, PW, PB, MAXDEPTH):
    # def tuple[:,:] moves_view
    # def boardCopy
    # def int i

    moves = getMoves(HUMAN,board)

    if(moves.ndim>1):
        moves_view=moves
    else:
        return boardScore(board,PW,PB)

    # def DTYPE_t[:] scores=np.zeros(moves.shape[0], dtype=DTYPE)

    if moves.shape[0]==0:
        if depth<MAXDEPTH:
            return maxMove(board, depth+1, alpha, beta, PW, PB, MAXDEPTH)
        else:
            return boardScore(board, PW , PB)

    for i, move in enumerate(moves_view):
        boardCopy=board.copy()
        boardCopy = fakeMove(move[0], move[1], LocateTurnedPieces(move[0], move[1], HUMAN, boardCopy), HUMAN, boardCopy)
        if depth>=MAXDEPTH:
            scores[i] = boardScore(boardCopy, PW, PB)
        else:
            scores[i] = maxMove(boardCopy, depth+1, alpha, beta, PW, PB, MAXDEPTH)
            if beta > scores[i]:
                beta = scores[i]
            if beta <= alpha:
                return scores[i]

    return min(scores)
