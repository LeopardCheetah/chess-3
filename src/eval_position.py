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

        def _get_piece_at_sq_index(_ind):
            # follow convention a1 = 0, b1 = 1, a2 = 8, etc.
            return position.get_piece_at_sq(chr(ord('a') + _ind % 8) + chr(ord('1') + _ind // 8))

        # sq = square to check
        # color = original color of the piece (w/b -- used to check for controlled/attacked)
        def _switch(sq, _col='w'):
            if _get_piece_at_sq_index(sq)[1] is None:
                return _empty_space_constant
            elif _get_piece_at_sq_index(sq)[1] == _col:
                return _controlled_space_constant
            elif _get_piece_at_sq_index(sq)[1] != _col:
                return _attacked_space_constant
            
            return '????'
    
        # automate diagonal/row/file checker/addition
        def _centipawn_factory(start_i, increment_i, _col='w'):
            _f = True
            _i = start_i
            c = 0
            while _f:
                _i += increment_i
                if _i > 63 or _i < 0:
                    _f = False
                    continue 

                c += _switch(_i, _col)
                if _switch(_i, _col) != _empty_space_constant:
                    _f = False
                    continue 
                continue
                
            return c

        for i in range(64):
            # a1 = 0
            # b1 = 1
            # c1 = 2
            # ...
            # a2 = 8
            # b2 = 9

            _piece, _color = _get_piece_at_sq_index(i)


            if _color is None:
                continue
            
            if _color == 'w':
                # white piece
                if _piece == 'P':
                    wcentipawns += self.P

                    # check if pawn can move up, if so, grant it empty square
                    wcentipawns += _empty_space_constant*(_get_piece_at_sq_index(i + 8)[1] is None)
                    # check NW
                    if i % 8 != 0:
                        # no switch statements i guess
                        wcentipawns += _switch(i + 7)
                    
                    if i % 8 != 7:
                        wcentipawns += _switch(i + 9)
                    
                    continue
                    
                if _piece == 'N':
                    wcentipawns += self.N
                    # check all 8 squares
                    # lots of if-statements :(
                    # WNW
                    if i % 8 > 1 and i // 8 < 7:
                        wcentipawns += _switch(i + 6)
                    
                    if i % 8 > 0 and i // 8 < 6:
                        wcentipawns += _switch(i + 15)
                    
                    if i % 8 < 7 and i // 8 < 6:
                        wcentipawns += _switch(i + 17)
                    
                    if i % 8 < 6 and i // 8 < 7:
                        wcentipawns += _switch(i + 10)
                    
                    # ESE
                    if i % 8 < 6 and i // 8 > 0:
                        wcentipawns += _switch(i - 6)
                    
                    if i % 8 < 7 and i // 8 > 1:
                        wcentipawns += _switch(i - 15)
                    
                    if i % 8 > 0 and i // 8 > 1:
                        wcentipawns += _switch(i - 17)
                    
                    if i % 8 > 1 and i // 8 > 0:
                        wcentipawns += _switch(i - 10)
                    
                    continue
    
                if _piece == 'B':
                    wcentipawns += self.B
                    # diagonal check
                    wcentipawns += _centipawn_factory(i, 9)
                    wcentipawns += _centipawn_factory(i, -9)
                    wcentipawns += _centipawn_factory(i, 7)
                    wcentipawns += _centipawn_factory(i, -7)
                    continue 

                if _piece == 'R':
                    wcentipawns += self.R 
                    wcentipawns += _centipawn_factory(i, 8)
                    wcentipawns += _centipawn_factory(i, -8)
                    wcentipawns += _centipawn_factory(i, 1)
                    wcentipawns += _centipawn_factory(i, -1)

                if _piece == 'Q':
                    wcentipawns += self.Q 
                    wcentipawns += _centipawn_factory(i, 9)
                    wcentipawns += _centipawn_factory(i, -9)
                    wcentipawns += _centipawn_factory(i, 7)
                    wcentipawns += _centipawn_factory(i, -7)

                    wcentipawns += _centipawn_factory(i, 8)
                    wcentipawns += _centipawn_factory(i, -8)
                    wcentipawns += _centipawn_factory(i, 1)
                    wcentipawns += _centipawn_factory(i, -1)

                if _piece == 'K':
                    wcentipawns += self.K
                    _ksquares = [8, 9, 1, -7, -8, -9, -1, 7] # e3, f3, f2, f1, e1, d1, d2, d3 for king @e2
                    
                    for _k in _ksquares:
                        _i = i + _k 
                        if _i < 0 or _i > 63:
                            continue

                        wcentipawns += _switch(_i)

                continue
            

        return wcentipawns, bcentipawns, wcentipawns - bcentipawns
