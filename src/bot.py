# random_mover_bot game not the actual bot that can (maybe) be deployed to lichess

import cgame 
import time
import sys # for quitting
import copy

import eval_position as ceval


def clear():
    print('\033[2J\033[H')
    return 


clear()

# print("Would you like to play as White or Black?")
# player_color_in = input("> ").strip().lower()
# player_color_in = 'w'

# player_color = -1
# if player_color_in[0] == 'w':
#     player_color = 0

# # if player_color_in[0] == 'b':
# #    player_color = 1

# if player_color_in[0] not in ['w', 'b']:
#     sys.exit(f"'{player_color_in}' is not a valid color")


# manual
player_color = 0

game = cgame.ChessGame()
evaluator_object = ceval.EvalPosition() # i hate this oop
suppress = True # suppress long engine output

game_finished = False
while not game_finished:

    # check if game is finished
    if game.white_turn and len(game.generate_white_candidate_moves()) == 0:
        # game is over
        game_finished = True

        clear()

        if game.is_white_king_in_check() and player_color == 0:
            # ok white is checkmated
            # player loses

            game.printboard()
            print()
            print("seems like you lost (you were checkmated) :(")
            continue


        if game.is_white_king_in_check() and player_color == 1:
            # ok you checkmated white as black.

            game.printboard_blackpov()
            print()
            print("woo congrats on winning!")
            print("you checkmated the white king.")
            continue


        if not game.is_white_king_in_check() and player_color == 0:
            # white is stalemated
            game.printboard()
            print()
            print("seems like you got stalemated :/")
            print("it's a draw")
            continue

        if not game.is_white_king_in_check() and player_color == 1:
            # player as black has stalemated white
            game.printboard_blackpov()
            print()
            print("dang you stalemated the white king")
            print("it's a draw now :///")
    if not game.white_turn and len(game.generate_black_candidate_moves()) == 0:
        # game is once again over
        game_finished = True

        clear()
        

        if game.is_black_king_in_check() and player_color == 0:
            # black is checkmated, player is white
            # player loses
            game.printboard()
            print()
            print("congrats on checkmating the black king!")
            print("you win!")
            continue

        if game.is_black_king_in_check() and player_color == 1:
            # ok you (the player) got checkmated
            game.printboard_blackpov()
            print()
            print('seems like you got checkmated :(')
            continue


        if not game.is_black_king_in_check() and player_color == 1:
            # black is stalemated, player is black
            game.printboard_blackpov()
            print()
            print("seems like you got stalemated :/")
            print("it's a draw for both sides")
            continue

        if not game.is_black_king_in_check() and player_color == 0:
            # player as white has stalemated black
            game.printboard()
            print()
            print("dang you stalemated the black king")
            print("it's a draw now :///")



    clear()
    if player_color == 0:
        # player is white
        game.printboard() # print board
    
    # if player_color == 1:
    #    game.printboard_blackpov()

    if (game.white_turn and not player_color) or (not game.white_turn and player_color):
        # is player's turn!
        pass
    else:
        time.sleep(1.5) # delay before computer moves





    # prompt move from player
    if game.white_turn and player_color == 0:
        # player is white
        # query for move, it is player's turn
        # query in the form [start_sq] [end_sq] [promotion]
        print()
        print("Please enter your move in the form '[starting square] [ending square] [promotion]'. If you're move does not need promotion, leave it blank.")
        print("For example, entering in 'e2 e4' will move a piece (if it exists) from e2 to e4. Similarly, 'a7 a8 N' will move a piece from a7 to a8 and attempt to promote it to a knight.")
        print()
        print("If you want to castle, use 0-0 or 0-0-0 respectively (use zeroes).")
    

        move = input("> ")
        move_components = move.strip().split()


        # we castlign
        if move == '0-0' or move == '0-0-0':
            if move == '0-0':
                # kingside castling
                status = game.send_white_move('e1', 'g1')
                if status == 0:
                    continue
                
                # status is bad
                print("uh castling doesn't work try something else sorry")
                time.sleep(1)
                continue
            
            # move = 0-0-0
            status = game.send_white_move('e1', 'c1')
            if status == 0:
                continue
            
            print("uh queenside castling doesn't work rigth now sorry")
            time.sleep(1.1)
            continue



        if len(move_components) == 2:
            status = game.send_white_move(move_components[0], move_components[1])
            if status == 0:
                continue
            
            # status is bad
            print("That move didn't send for some reason. Please try again.")
            time.sleep(1)
            continue
        

        if len(move_components) == 3:
            status = game.send_white_move(move_components[0], move_components[1], move_components[2])
            if status == 0:
                continue
            
            print("That move didn't send for some reason. Please try again.")
            time.sleep(1)
            continue
        
        print("Your input is off somehow. Please try again.")
        time.sleep(1)
        continue
    

    # bot generates move (as black)
    if not game.white_turn and player_color == 0:
        _possible_moves = game.generate_black_candidate_moves()
        _board = game.get_board_state()
        # _potential_board = copy.deepcopy(_board) # will be overriden every iteration to save memory


        
        # generate max evales
        # _max_bcentipawns = -99999999999999
        # _best_move = (None, None)

        ## this is a one-ply search
        # for _pair in _possible_moves:
        #     # generate position + evaluate it
        #     _potential_board = copy.deepcopy(_board)
        #     # deep copied board

        #     # move, assuming no promotion
        #     if len(_pair) != 2:
        #         print('promotion not supported for eval yet')
        #         quit()

        #     _potential_board.send_move(_pair[0], _pair[1])
        #     _eval = -1 * (ceval.EvalPosition().eval_position(_potential_board)[2])

        #     print(_pair, _eval)

        #     if _eval > _max_bcentipawns:
        #         _max_bcentipawns = _eval
        #         _best_move = _pair
            
        #     continue




        # check two plys ahead 
        _one_ply_ahead_game = copy.deepcopy(game)
        _min_wcentipawns = 99999999999999
        _best_move = (None, None)

        for _pair in _possible_moves:
            # make sample black move
            _one_ply_ahead_game = copy.deepcopy(game)
            if len(_pair) != 2:
                _one_ply_ahead_game.send_black_move(_pair[0], _pair[1], _pair[2])
            else:
                _one_ply_ahead_game.send_black_move(_pair[0], _pair[1])

            # evaluate all white moves
            _possible_white_moves = _one_ply_ahead_game.generate_white_candidate_moves()
            _board = _one_ply_ahead_game.get_board_state()
            _potential_board = copy.deepcopy(_board)


            _max_wcentipawn_response = -9999999999

            for _pairt in _possible_white_moves: # comeback moves
                _potential_board = copy.deepcopy(_board)

                if len(_pairt) != 2:
                    _potential_board.send_move(_pairt[0], _pairt[1], _pairt[2])
                else:
                    _potential_board.send_move(_pairt[0], _pairt[1])

                _eval = (ceval.EvalPosition().eval_position(_potential_board)[2]) 

                if not suppress:
                    print(_pair, _pairt, _eval)

                if _eval > _max_wcentipawn_response:
                    _max_wcentipawn_response = _eval

            if _max_wcentipawn_response < _min_wcentipawns:
                _min_wcentipawns = _max_wcentipawn_response
                _best_move = _pair 

        
        # print('best move', _best_move, _max_bcentipawns)
        print('best move', _best_move, _min_wcentipawns)

        # play move
        if len(_best_move) == 2:
            game.send_black_move(_best_move[0], _best_move[1])
            continue 
        
        game.send_black_move(_best_move[0], _best_move[1], _best_move[2])
        continue
        # end black eval
    

    continue 