# redoing this
# make it bare bones


class _color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    WARNING = '\033[93m'
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDCOLOR = '\033[0m'

    # these not used
    BOLD = '\033[1m'
    GRAY = '\033[2m'
    UNDERLINE = '\033[4m'


class Board:
    
    # various configs/settings
    # maybe make this changeable later
    neutral_square_value = "."
    neutral_color = _color.ENDCOLOR
    white_piece_color = _color.BLUE # white's pieces are blue
    black_piece_color = _color.FAIL # black's pieces are red

    board = []


    # makes the board

    # arguments taken: none

    # arguments returned: none
    def __init__(self):
        self.clear_board()
        return 



    # Auxiliary functions
    # dont use these in other files pls thanks
    ###########################

    def _cnv_sq_to_pair(self, square):
        sq_rank = 8 - int(square[1])
        sq_file = int(ord(square[0]) - ord('a'))

        return sq_rank, sq_file

    ###########################




    # given a square and a piece, set square to piece

    # args taken:
    # square: chess notation string (e.g. "a1", "f5", "e8")
    # piece: piece notation piece (e.g. "N", "Q", "P") -- lowercase is fine
    # color: "w"/"b" -- is piece white or black?

    # args returned: none
    def change_sq_to_piece(self, square, piece, color):
        _rank, _file = self._cnv_sq_to_pair(square)

        # piece validation
        if piece.upper() not in ['P', 'N', 'B', 'R', 'Q', 'K']:
            raise Exception(f"Cannot change square {square} to piece {piece} of color {color} because '{piece}' is not a valid type.")

        if color.lower() == 'w' or color.lower() == 'white':
            self.board[_rank][_file] = f'{self.white_piece_color}' + piece.upper() + f'{self.neutral_color}'
        elif color.lower() == 'b' or color.lower() == 'black':
            self.board[_rank][_file] = f'{self.black_piece_color}' + piece.upper() + f'{self.neutral_color}'
        else:
            raise Exception(f"Cannot change square {square} to piece {piece} of color {color} because color '{color}' is invalid.")


        return 


   

    # given a square, get the piece at that square, its type, and so on

    # args taken:
    # square: chess notation string (e.g. "e3", "b2")

    # args returned:
    # piece type at square (either "P", "N", "B", "R", "Q", "K", or None) and
    # piece color at square ("w"/"b" or None)
    def get_piece_at_sq(self, square):
        _rank, _file = self._cnv_sq_to_pair(square)

        if self.board[_rank][_file] == ".":
            return (None, None)

        return (self.board[_rank][_file][5], 'w' if self.board[_rank][_file][3] == self.white_piece_color[3] else 'b')



    # prints the board out 
    def printboard(self):
        # print the chess board
        print()
        print('  +-----------------+')
        c = 8
        for row in self.board:
            print(c, '|', end=' ')
            c -= 1
            for item in row:
                print(item, end=' ')
            
            print('|')
        
        print('  +-----------------+')
        print('    a b c d e f g h')
        return




    # prints the board out (from black's pov)
    def printboard_blackpov(self):
        # print from black's pov
        print()
        print('  +-----------------+')
        c = 1
        for row_ind in range(8):
            print(c, '|', end=' ')
            c += 1
            for col_ind in range(8):
                print(self.board[7 - row_ind][7 - col_ind], end=' ')
            
            print('|')
        
        print('  +-----------------+')
        print('    h g f e d c b a')
        return




    #####################
    ## OTHER UTILITIES ##
    #####################
    # (these follow from the commands listed above but are often simpler to do just in code and stuff so)


    def reset_board(self):
        # reset board to starting position of normal chess

        # add pieces
        _starting_ls = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

        for _i in range(8):
            _file = chr(ord('a') + _i)
            self.change_sq_to_piece(_file+'1', _starting_ls[_i], 'w')
            self.change_sq_to_piece(_file+'2', 'P', 'w')

            self.change_sq_to_piece(_file+'7', 'P', 'b')
            self.change_sq_to_piece(_file+'8', _starting_ls[_i], 'b')

        return


    def clear_board(self):
        self.board = [[self.neutral_square_value for _tempa in range(8)] for _tempb in range(8)] 
        return 



    # using chess notation, move a piece
    def move_piece(self, starting_sq, final_sq):
        # check that there is a piece at starting location

        if self.get_piece_at_sq(starting_sq)[0] is None:
            raise Exception(f"There is no piece at square {starting_sq}!")
        
        
        _start_row, _start_col = self._cnv_sq_to_pair(starting_sq)
        _end_row, _end_col = self._cnv_sq_to_pair(final_sq)

        self.board[_end_row][_end_col], self.board[_start_row][_start_col] = self.board[_start_row][_start_col], "."
        return 

    

    # use this to "officially" submit a move
    def send_move(self, start_sq, end_sq):
        self.move_piece(start_sq, end_sq)
        return
    
    # we done with this class

