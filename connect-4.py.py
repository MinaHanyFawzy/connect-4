#my name is : mina hany fawzy
#my id is : 20210421
#my game is the game no.1 and its name is connect-4
#presented to : Dr. Mohammed El-Ramly

#//////////////////////////////////////////////////
#first step of the game is to define the board of the game where the board is 6 rows* 7 columns
board = [
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_'
]
# here i made a function to draw the board
def Draw_Board():
# the for loop to get the index and each element defined in the board above and the enumerate function that
# do for each element in the list also provides the element of that index and thats done by two temprory variables where
# they are the index and the space index is the index of each element in the board and the space is the spaces between the underscore
    for index, space in enumerate(board):
#this if conditional to change the first index from zero to start from 1 and doesnt exceed the last column
        if (index + 1) % 7 != 0:
            print(f'{space} |', end = ' ') # end= ' ' to be sure that all elements on the same level
        else:
            print(space)
#this function is done to watch the move of player 1
def The_Move_Of_Player_One(z, y, x):
    if z[y] == '_' or z[y - 7] == '_' or z[y - 14] == '_' or z[y - 21] == '_' or z[y - 28] == '_' or z[x] == '_': # here we see if all _ are empty with something like coordinates
        if z[y] == '_':
            z[y] = 'X'
        elif z[y - 7] == '_':
            z[y - 7] = 'X'
        elif z[y - 14] == '_':
            z[y - 14] = 'X'
        elif z[y - 21] == '_':
            z[y - 21] = 'X'
        elif z[y - 28] == '_':
            z[y - 28] = 'X'
        elif z[x] == '_':
            z[x] = 'X'
    else:
        if z[y] == 'O' or z[y] == 'X':
            z[y - 7] = 'X'
        elif z[y - 7] == 'O' or z[y - 7] == 'X':
            z[y - 14] = 'X'
        elif z[y - 14] == 'O' or z[y - 14] == 'X':
            z[y - 21] = 'X'
        elif z[y - 21] == 'O' or z[y - 21] == 'X':
            z[y - 28] = 'X'
        elif z[y - 28] == 'O' or z[y - 28] == 'X':
            z[x] = 'X'
    Draw_Board()
def The_Move_Of_player_Two(z, y, x):
    if z[y] == '_' or z[y - 7] == '_' or z[y - 14] == '_' or z[y - 21] == '_' or z[y - 28] == '_' or z[x] == '_':
        if z[y] == '_':
            z[y] = 'O'
        elif z[y - 7] == '_':
            z[y - 7] = 'O'
        elif z[y - 14] == '_':
            z[y - 14] = 'O'
        elif z[y - 21] == '_':
            z[y - 21] = 'O'
        elif z[y - 28] == '_':
            z[y - 28] = 'O'
        elif z[x] == '_':
            z[x] = 'O'
    else:
        if z[y] == 'O' or z[y] == 'X':
            z[y - 7] = 'O'
        elif z[y - 7] == 'O' or z[y - 7] == 'X':
            z[y - 14] = 'O'
        elif z[y - 14] == 'O' or z[y - 14] == 'X':
            z[y - 21] = 'O'
        elif z[y - 21] == 'O' or z[y - 21] == 'X':
            z[y - 28] = 'O'
        elif z[y - 28] == 'O' or z[y - 28] == 'X':
            z[x] = 'O'
    Draw_Board()
def Check_Columns(z, check): # this function to check the columns
    return ((z[0] == check and z[7] == check and z[14] == check and z[21] == check) or
            (z[7] == check and z[14] == check and z[21] == check and z[28] == check) or
            (z[14] == check and z[21] == check and z[28] == check and z[35] == check) or
            (z[1] == check and z[8] == check and z[15] == check and z[22] == check) or
            (z[8] == check and z[15] == check and z[22] == check and z[29] == check) or
            (z[15] == check and z[22] == check and z[29] == check and z[36] == check) or
            (z[2] == check and z[9] == check and z[16] == check and z[23] == check) or
            (z[9] == check and z[16] == check and z[23] == check and z[30] == check) or
            (z[16] == check and z[23] == check and z[30] == check and z[37] == check) or
            (z[3] == check and z[10] == check and z[17] == check and z[24] == check) or
            (z[10] == check and z[17] == check and z[24] == check and z[31] == check) or
            (z[17] == check and z[24] == check and z[31] == check and z[38] == check) or
            (z[4] == check and z[11] == check and z[18] == check and z[25] == check) or
            (z[11] == check and z[18] == check and z[25] == check and z[32] == check) or
            (z[18] == check and z[25] == check and z[32] == check and z[39] == check) or
            (z[5] == check and z[12] == check and z[19] == check and z[26] == check) or
            (z[12] == check and z[19] == check and z[26] == check and z[33] == check) or
            (z[19] == check and z[26] == check and z[33] == check and z[40] == check) or
            (z[6] == check and z[13] == check and z[20] == check and z[27] == check) or
            (z[13] == check and z[20] == check and z[27] == check and z[34] == check) or
            (z[20] == check and z[27] == check and z[34] == check and z[41] == check))
def Check_Diagonals(z, check): # this function to check the diagonals
    return ((z[14] == check and z[22] == check and z[30] == check and z[38] == check) or
            (z[7] == check and z[15] == check and z[23] == check and z[31] == check) or
            (z[15] == check and z[23] == check and z[31] == check and z[39] == check) or
            (z[0] == check and z[8] == check and z[16] == check and z[24] == check) or
            (z[8] == check and z[16] == check and z[24] == check and z[32] == check) or
            (z[16] == check and z[24] == check and z[32] == check and z[41] == check) or
            (z[1] == check and z[9] == check and z[17] == check and z[25] == check) or
            (z[9] == check and z[17] == check and z[25] == check and z[33] == check) or
            (z[17] == check and z[25] == check and z[33] == check and z[41] == check) or
            (z[2] == check and z[10] == check and z[18] == check and z[26] == check) or
            (z[10] == check and z[18] == check and z[26] == check and z[34] == check) or
            (z[3] == check and z[11] == check and z[19] == check and z[27] == check) or
            (z[20] == check and z[26] == check and z[32] == check and z[38] == check) or
            (z[13] == check and z[19] == check and z[25] == check and z[31] == check) or
            (z[19] == check and z[25] == check and z[31] == check and z[37] == check) or
            (z[6] == check and z[12] == check and z[18] == check and z[24] == check) or
            (z[12] == check and z[18] == check and z[24] == check and z[30] == check) or
            (z[18] == check and z[24] == check and z[30] == check and z[36] == check) or
            (z[5] == check and z[11] == check and z[17] == check and z[23] == check) or
            (z[11] == check and z[17] == check and z[23] == check and z[29] == check) or
            (z[17] == check and z[23] == check and z[29] == check and z[35] == check) or
            (z[4] == check and z[10] == check and z[16] == check and z[22] == check) or
            (z[10] == check and z[16] == check and z[22] == check and z[28] == check) or
            (z[3] == check and z[9] == check and z[15] == check and z[21] == check))
def Check_Rows(z, check): #this function is to check the rows
    return ((z[0] == check and z[1] == check and z[2] == check and z[3] == check) or
            (z[1] == check and z[2] == check and z[3] == check and z[4] == check) or
            (z[2] == check and z[3] == check and z[4] == check and z[5] == check) or
            (z[3] == check and z[4] == check and z[5] == check and z[6] == check) or
            (z[7] == check and z[8] == check and z[9] == check and z[10] == check) or
            (z[8] == check and z[9] == check and z[10] == check and z[11] == check) or
            (z[9] == check and z[10] == check and z[11] == check and z[12] == check) or
            (z[10] == check and z[11] == check and z[12] == check and z[13] == check) or
            (z[14] == check and z[15] == check and z[16] == check and z[17] == check) or
            (z[15] == check and z[16] == check and z[17] == check and z[18] == check) or
            (z[16] == check and z[17] == check and z[18] == check and z[19] == check) or
            (z[17] == check and z[18] == check and z[19] == check and z[20] == check) or
            (z[21] == check and z[22] == check and z[23] == check and z[24] == check) or
            (z[22] == check and z[23] == check and z[24] == check and z[25] == check) or
            (z[23] == check and z[24] == check and z[25] == check and z[26] == check) or
            (z[24] == check and z[25] == check and z[26] == check and z[27] == check) or
            (z[28] == check and z[29] == check and z[30] == check and z[31] == check) or
            (z[29] == check and z[30] == check and z[31] == check and z[32] == check) or
            (z[30] == check and z[31] == check and z[32] == check and z[33] == check) or
            (z[31] == check and z[32] == check and z[33] == check and z[34] == check) or
            (z[35] == check and z[36] == check and z[37] == check and z[38] == check) or
            (z[36] == check and z[37] == check and z[38] == check and z[39] == check) or
            (z[37] == check and z[38] == check and z[39] == check and z[40] == check) or
            (z[38] == check and z[39] == check and z[40] == check and z[41] == check))
def isFull(z): #this function see if the board and all indexes are full or not
    if z.count('_') == 0: #here we use count to count the number of underscores
        return False  #if it is equal zero it returns false which means the board is full
    else:
        return True   # if its not equal zero it returns true which means the board its not full and the game terminate
#here we make the main function
def main_function():
    Draw_Board() #we start by drawing the empty board
    player =  1 #assign that the variable player is one
    while True: #here the while loop continues untill there is a winner or the board is full
        try:
            if isFull(board): #this function where we defined above we will check it in the following lines
                move = int(input(f'Player {player}, enter the column (1-7): ')) #we created vari. named move it range between 1 and 7
                if 1 <= move <= 7: #this if condtion to be sure that the input ranged between 1 and 7
                    move -= 1 #move -= 1 : bec. the index start from [00] so i should -1 from the move to select the right column
                    bottom = move + 35 #to make the X or O to be slided down to the last underscore in the column
#the following lines to see if the the column is full and the player put its number
                    while board[move] == 'X' or board[move] == 'O':
                        move = int(input('Please choose another column because its full : '))
                        move -= 1
                        bottom = move + 35
                    if player == 1: #intialize that player one and he has X to play with
                        #if the player is one we call function of the player one
                        The_Move_Of_Player_One(board, bottom, move)
                        #if he find  check rows or check diagonals or check columns done
                        if Check_Rows(board, 'X') or Check_Columns(board, 'X') or Check_Diagonals(board, 'X'):
                            print(f'Player {player} has won.') #print player 1 has won
                            break
                        else:
                            player = 2 #if its not one we will call function of the player two and give him O
                    else:
#the following lines to see if the the column is full and the player put its number
                        while board[move] == 'X' or board[move] == 'O':
                            move = int(input('Please choose another column because its full :'))
                            move -= 1
                            bottom = move + 35
                        The_Move_Of_player_Two(board, bottom, move)
                        #here we check player 2 like player 1
                        if Check_Rows(board, 'O') or Check_Columns(board, 'O') or Check_Diagonals(board, 'O'):
                            print(f'Player {player} has won.')
                            break
                        else:
                            player = 1
                else:
                    print('Please enter a number between 1-7:')
            else:
                print('The Game Finished with Tie') #if the function isfull and no winner
                break
        except ValueError: #here we check if there is a value error like the user put string instead of a intger number
            print('Please enter a number not anything else.')
main_function()