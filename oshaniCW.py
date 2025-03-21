#importing built in modules
import random
from prettytable import PrettyTable

#importing customized module
import save_game 

#initializing variables
human_first_try = 0       
computer_first_try = 0
ttl_human_counts = 0
ttl_com_counts = 0
ttl_human_blackhole_hits = 0
ttl_com_blackhole_hits = 0


def play_game():
    human_pos = -1 
    com_pos = -1
    global save_game_file  #global variable
    global ttl_human_counts, ttl_com_counts  #global variable
    global ttl_human_blackhole_hits, ttl_com_blackhole_hits  #global variable
    hum_message = " "
    com_message = " "

    #Main loop
    while True:

        #Drawing the board
        board = [
            [" " for i in range(1, 21)],
            [" " for i in range(1, 21)]
        ]

        board[0][6] = board[0][13] = board[1][6] = board[1][13] = 'O'
        table = PrettyTable()
        table.field_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                             '17', '18', '19', '20']

        global human_first_try, computer_first_try #accessing global variables

        #Generating dice value for human and computer
        human_dice = random.randint(1, 6)
        com_dice = random.randint(1, 6)

        #Move counts of human and computer
        ttl_human_counts += human_dice // 2
        ttl_com_counts += com_dice // 2

        input(" Press enter to roll the dice ")

        
        if human_dice == 6 and human_first_try == 0:
            human_first_try = 1
            print("Human rolled 6. Game starts!")
            human_pos = 0

        if com_dice == 6 and computer_first_try == 0:
            computer_first_try = 1
            print("Computer rolled 6. Game starts!\n")
            com_pos = 0

        #check if human or computer lands on a black hole
        if human_first_try == 0:
            print(f"Human dice roll is {human_dice} cannot enter the game")

        if computer_first_try == 0:
            print(f"Computer dice roll is {com_dice}, cannot enter the game\n")

        
        if human_first_try == 1:
            human_dice = random.randint(1, 6)
            human_pos += human_dice // 2
            message = f"Human roll number is {human_dice} and current location is {human_pos} "
            print(message)

        if computer_first_try == 1:
            com_dice = random.randint(1, 6)
            com_pos += com_dice // 2
            message = f"Computer roll number is {com_dice} and current location is {com_pos}  "
            print(message)

        #Updating the positions of human and computer on the board
        for i in range(len(board[0])):
            if human_pos == i + 1:
                board[0][i] = "X"

        for i in range(len(board[1])):
            if com_pos == i + 1:
                board[1][i] = "X"

        if board[0][6] == 'X' or board[0][13] == 'X':
            human_pos = 0
            ttl_human_blackhole_hits +=1
            board[0][0] = 'X'
            board[0][6] = board[0][13] = 'O'
            message = "Human hit the blackhole!"
            print(message)

        if board[1][6] == 'X' or board[1][13] == 'X':
            com_pos = 0
            ttl_com_blackhole_hits +=1
            board[1][0] = 'X'
            board[1][6] = board[1][13] = 'O'
            message = "Computer hit the blackhole!"
            print(message)


        if "X" in board[0][19] or human_pos >= 20:
            hum_message = "You won the game!"
            print(hum_message)
            save_game_file()
            board[0][19] = "X"
            for row in board:
                table.add_row(row)
            print(table)
            table.clear_rows()
            

        if "X" in board[1][19] or com_pos >= 20:
            com_message = "Computer won the game!"
            print(com_message)
            save_game_file()
            board[1][19] = "X"
            for row in board:
                table.add_row(row)
            print(table)
            table.clear_rows()
            

        for row in board:
            table.add_row(row)
        print(table)
        table.clear_rows()

        #Save data of the game in a file
        def save_game_file():
            save_game.game_saver_human(ttl_human_counts, ttl_human_blackhole_hits, hum_message)
            save_game.game_saver_com(ttl_com_counts, ttl_com_blackhole_hits, com_message)

        board[0][human_pos - 1] = ' '
        board[1][com_pos - 1] = ' '
        table.clear_rows()

play_game()
