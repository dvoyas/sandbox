"""
This is Tic Toc game
"""
import random


def display_board(board):
    from IPython.display import clear_output
    clear_output()
    print('   |   |')
    print(' ' +board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])    
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')


test_board = 10*[' ']
# print(test_board)
# display_board(test_board)


def user_choice(game_list):
    
    # VARIABLES
    #Initials
    choice = 'WRONG'
    acceptable_range = range(1,10)
    within_range = False
    unique_input = False
    
    # TWO CONDITIONS TO CHECK
    # DIGIT OR WHITHIN_RANGE==FALSE
    
    while choice.isdigit() == False or within_range == False or unique_input == False:
        
        choice = input("Please enter a number (1-9): ")
        
        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are our of acceptable range (1-10)")
                within_range = False
        
        # UNIQUE CHECK - check if choice not been before
        if within_range:
            if game_list[int(choice)] == ' ':
                unique_input = True
            else:
                print( 'Please choose another field!')

    return int(choice)


def replacement_choice(game_list,position,user_placement):
    from IPython.display import clear_output
    #user_placement = input("Type a string to place at position: ")
    
    game_list[position] = user_placement
    clear_output()    
    return game_list


def gameon_choice():
    from IPython.display import clear_output
    # This is original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    
    # While choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Keep playing a position (Y or N): ")
        
        if choice not in ['Y','N']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()
            
            print("Sorry, I don't understand, please choose Y or N  ")
            
    if choice == "Y":
        return True
    else:
        return False


def check_if_win(game_list, marker):
    return (game_list[1] == game_list[4] == game_list[7] == marker or game_list[2] == game_list[5] == game_list[8] == marker or
    game_list[3] == game_list[6] == game_list[9] == marker or game_list[1] == game_list[2] == game_list[3] == marker or
    game_list[4] == game_list[5] == game_list[6] == marker or game_list[7] == game_list[8] == game_list[9] == marker or
    game_list[1] == game_list[5] == game_list[9] == marker or game_list[3] == game_list[5] == game_list[7] == marker)


def player_input():
    """
    OUTPUT = (Player 1 marker, Player 2 marker)
    """
    
    marker = ''
    
    # KEEP ASKING PLAYER 1 to shoose X or 0
    while marker not in ['X','O']:
        marker = input("Player 1, Choose X or O: ").upper() 
    
    # ASSING PLAYER 2, the opposite marker
    player1 = marker
    if player1 == 'X':
        return ('X', 'O')
    else:
        return ('O','X')


player1_marker, player2_marker = player_input()


def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board,'&',7)
display_board(test_board)


def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    
    for i in range (1,10):
        if space_check(board,i):
            return False
    # BOARD IS FULL IF WE RETURN TRUE
    return True


board = ['X']*10
full_board_check(board)


def player_choice(board):
    
    position = 0
    choice = 'WRONG'
    
    while choice.isdigit() == False  or position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        choice = input('Player, choose your next position: (1-9)' ) 
        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        if choice.isdigit():
            position = int(choice)
    
    return position        


def replay():
    choice = input("Play again? Enter Yes or No ")
    
    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')


# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe!')

while True:
    
    #PLAY THE GAME
    
    ## SET EVERYTING UP (BOARD, WHOS FIRST, CHOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
        
    play_game = input('Ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    ## GAME PLAY
    
    while game_on:
        
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # Check if they won
            if check_if_win(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'
            # Or check if there is a tie
            
            #No tie and no win? Then nextplayer's turn
            
            ### PLAYER ONE TURN
        
        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if check_if_win(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break
    #BREAK OUT OF THE WHILE LOOP ON replay()


