# eval a board!!

class EvalPosition:

    # some basic evals

    # centipawns
    P = 100
    N = 320
    B = 330
    R = 500
    Q = 900
    K = 20000

    pawn_eval = [
        0,  0,  0,  0,  0,  0,  0,  0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5,  5, 10, 25, 25, 10,  5,  5,
        0,  0,  0, 20, 20,  0,  0,  0,
        5, -5,-10,  0,  0,-10, -5,  5,
        5, 10, 10,-20,-20, 10, 10,  5,
        0,  0,  0,  0,  0,  0,  0,  0
    ]

    knight_eval = [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50
    ]


    bishop_eval = [
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -20,-10,-10,-10,-10,-10,-10,-20
    ]

    rook_eval = [
        0,  0,  0,  0,  0,  0,  0,  0,
        5, 10, 10, 10, 10, 10, 10,  5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        0,  0,  0,  5,  5,  0,  0,  0
    ]

    queen_eval = [
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
        -5,  0,  5,  5,  5,  5,  0, -5,
        0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20
    ]

    # middle game only
    # we'll figure out endgame incorporations later
    king_eval = [
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -10,-20,-20,-20,-20,-20,-20,-10,
        20, 20,  0,  0,  0,  0, 20, 20,
        20, 30, 10,  0,  0, 10, 30, 20
    ]


    def __init__(self):
        pass # empty constructor


    def eval_position(self, position):
        # position should be a board object
        
        wcentipawns = 0
        bcentipawns = 0

        for i in range(64):
            # a8 = 0
            # b8 = 1
            # ...
            # a7 = 8

            _square = chr(ord('a') + i % 8) + chr(ord('8') - i // 8) # represented in chess notation

            _piece, _color = position.get_piece_at_sq(_square)

            if _color is None:
                continue
            
            if _color == 'w':
                # white piece
                if _piece == 'P':
                    wcentipawns += self.P 
                    wcentipawns += self.pawn_eval[i]

                if _piece == 'N':
                    wcentipawns += self.N
                    wcentipawns += self.knight_eval[i]

                if _piece == 'B':
                    wcentipawns += self.B
                    wcentipawns += self.bishop_eval[i]

                if _piece == 'R':
                    wcentipawns += self.R 
                    wcentipawns += self.rook_eval[i]

                if _piece == 'Q':
                    wcentipawns += self.Q 
                    wcentipawns += self.queen_eval[i]

                if _piece == 'K':
                    wcentipawns += self.K
                    wcentipawns += self.king_eval[i]

                continue
            
            # black piece
            # the eval function is flipped for black so:
            # a8 black --> a1 white (0 --> 56)
            # b7 black --> b2 white (9 --> 49)
            # i = 8*(7 - i // 8) + (i % 8)
            j = 8*(7 - i // 8) + (i % 8)
            if _color == 'b':
                if _piece == 'P':
                    bcentipawns += self.P 
                    bcentipawns += self.pawn_eval[j]

                if _piece == 'N':
                    bcentipawns += self.N
                    bcentipawns += self.knight_eval[j]

                if _piece == 'B':
                    bcentipawns += self.B
                    bcentipawns += self.bishop_eval[j]

                if _piece == 'R':
                    bcentipawns += self.R 
                    bcentipawns += self.rook_eval[j]

                if _piece == 'Q':
                    bcentipawns += self.Q 
                    bcentipawns += self.queen_eval[j]

                if _piece == 'K':
                    bcentipawns += self.K
                    bcentipawns += self.king_eval[j]

        return wcentipawns, bcentipawns, wcentipawns - bcentipawns

            


