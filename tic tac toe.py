while True: #
    player1 = input('first move, do you want to be x or o : ').lower()
    if player1 == 'x' or player1 == 'o': #checks to see if player choose a valid letter
        if player1 == 'x': 
            player2 = 'o' #if one player is x, other player is o
        else:
            player2 = 'x'
        print(f'player 1 is {player1} \nplayer 2 is {player2}') #welcome the player
        break
    else:
        print('not option') #they chose an invalid option; not x or o

   
test_board = ['| 1 |',' 2 |',' 3 | \n','| 4 |',' 5 | ','6 | \n','| 7 |',' 8 |',' 9 |'] #showing the player the possible options
test_board = (''.join(test_board)) #turns the board into a string
print(test_board, '\n------------------rules-------------------- \nchoose the number assossiated with the position \n------------------------------------------') #tells the player t he rules

positiondict = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '} #dictionnary to hold values and check for wins
def check_win():
    for x in range(1,8,3): #check rows
        if positiondict[x] == positiondict[x+1] and positiondict[x] == positiondict[x+2]: #check top horizontal row
            if positiondict[x] == ' ': #if position is empty, it doesn't win, it just passes because the initial positions are all empty and will trigger a win 
                pass
            else:
                print(f'{positiondict[x]} WINS by row') #if the position is not empty(meaning either X or O, then that means the other position are not empty because we're comparing the values, so it triggers a win
                exit()
    
    for x in range(1,4): #check columns
        if positiondict[x] == positiondict[x+3] and positiondict[x] == positiondict[x+6]: #check top horizontal row
            if positiondict[x] == ' ': #if position is empty, it doesn't win, it just passes because the initial positions are all empty and will trigger a win 
                pass
            else:
                print(f'{positiondict[x]} WINS by column') #if the position is not empty(meaning either X or O, then that means the other position are not empty because we're comparing the values, so it triggers a win
                exit()
    if positiondict[1] == positiondict[5] and positiondict[1] == positiondict[9]: #check diagonal from top left to bottom right
        if positiondict[1] == ' ':
            pass
        else:
            print(f'{positiondict[1]} WINS by diagonal')
            exit()
    elif positiondict[3] == positiondict[5] and positiondict[3] == positiondict[7]: #check diagonal from top right to bottom left
        if positiondict[3] == ' ':
            pass
        else:
            print(f'{positiondict[3]} WINS by diagonal')
            exit()
    elif len(already_played_moves) == 9: #if the there are 9 moves played without a win trigger, its a tie
        print('tie game')
        exit()
    else:
        pass
movecounter = 1 #counter moves
already_played_moves = [] #store played moves
while movecounter < 10: #only up to 9 moves
    if movecounter%2 != 0: #odd number, meaning first move 
        player1move = int(input(f'choose a position, player {player1} : ')) #choosing a position
        if player1move in already_played_moves: #check if move already played
            print('position already taken')
            continue #restart loop to ask for input again
        elif player1move not in range(1,10): #if they choose a number isnt in the board 
            print('not an available move on the board')
            continue
        else:
            positiondict[player1move] = player1 #changes the dictionary value of that position from empty to the players value; either x or o
            already_played_moves.append(player1move) #adds to the already played moves list
            print(f'| {positiondict[1]} | {positiondict[2]} | {positiondict[3]} | \n| {positiondict[4]} | {positiondict[5]} | {positiondict[6]} | \n| {positiondict[7]} | {positiondict[8]} | {positiondict[9]} |')
            check_win() #check win function
    else: #even number, meaning second move
        player2move = int(input(f'choose a position, player {player2} : '))
        if player2move in already_played_moves:
            print('position already taken')
            continue
        elif player2move not in range(1,10):
            print('not an available move on the board')
            continue
        else:
            positiondict[player2move] = player2
            already_played_moves.append(player2move)
            print(f'| {positiondict[1]} | {positiondict[2]} | {positiondict[3]} | \n| {positiondict[4]} | {positiondict[5]} | {positiondict[6]} | \n| {positiondict[7]} | {positiondict[8]} | {positiondict[9]} |')
            check_win()        
    movecounter+= 1 #adds one to the counter whenever a move is played so it alternated between even and odd numbers
