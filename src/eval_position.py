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
        # more of a eval selector
        return self.basic_position_eval(position)
        
    def basic_position_eval(self, position):  
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


    def space_eval_function(self, position):
        # each square attacked is worth [_empty_space_constant] centipawns
        _empty_space_constant = 3
        # each square controlled but also with a piece on it is worth [_controlled_space_constant] centipawns
        _controlled_space_constant = 10
        _attacked_space_constant = 6 

        
        wcentipawns = 0
        bcentipawns = 0

        def get_piece_at_sq_index(_ind):
            # follow convention a1 = 0, b1 = 1, a2 = 8, etc.
            return position.get_piece_at_sq(chr(ord('a') + _ind % 8) + chr(ord('1') + _ind // 8))

        for i in range(64):
            # a1 = 0
            # b1 = 1
            # c1 = 2
            # ...
            # a2 = 8
            # b2 = 9

            _piece, _color = get_piece_at_sq_index(i)


            if _color is None:
                continue
            
            if _color == 'w':
                # white piece
                if _piece == 'P':
                    wcentipawns += self.P

                    # check if pawn can move up, if so, grant it empty square
                    wcentipawns += _empty_space_constant*(get_piece_at_sq_index(i + 8)[1] is None)
                    # check NW
                    if i % 8 != 0:
                        # no switch statements i guess
                        if get_piece_at_sq_index(i + 7)[1] is None:
                            wcentipawns += _empty_space_constant
                        elif get_piece_at_sq_index(i + 7)[1] == 'w':
                            wcentipawns += _controlled_space_constant
                        elif get_piece_at_sq_index(i + 7)[1] == 'b':
                            wcentipawns += _attacked_space_constant
                    
                    continue
                    
                if _piece == 'N':
                    ## TODO -- finish later
                    wcentipawns += self.N
                    # check all 8 squares
                    # lots of if-statements :(
                    _knight_jumps = [10, 17, 15, 6, -10, -17, -15, -6]

                    for _j in _knight_jumps:
                        _new_i = i + _j 

                        if _new_i < 0 or _new_i > 63:
                            continue 

                        if ((_new_i // 8 - i // 8) in [1, 2, -1, -2]) ():
                            pass
                        

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

        return wcentipawns, bcentipawns, wcentipawns - bcentipawns
