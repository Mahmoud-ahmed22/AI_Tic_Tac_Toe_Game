board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print("\n")

printBoard(board)

def isSpaceFree(position):
    if (board[position] == ' '):
        return True
    else:
        return False
    

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
       
    return True
    
def checkWin():
     if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
     elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
     elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
     elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
     elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
     elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
     elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
     elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
     else:
        return False
     
def checkWhichPlayerWon(mark):
     if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
     elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
     elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
     elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
     elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
     elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
     elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
     elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
     else:
        return False

def playTurn(letter, position):

    if isSpaceFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw")
            exit()
        if (checkWin()):
            if letter == 'X':
                print('AI Won!')
                
            else:
                print("You Won!")
                
    else:
        print("This move is already done by opponent, please try another position")
        position = int(input("Enter new position: "))
        playTurn(letter, position)
        return
    
player = 'O'
bot  = 'X'

def playerMove():
    position = int(input("Enter Your Position For 'O': "))
    playTurn(player, position)
    return

def minimax(board, isMaximizing):

    if checkWhichPlayerWon(bot):
        return 100000
    
    elif checkWhichPlayerWon(player):
        return -100000
    
    elif checkDraw():
        return 0
    
    if isMaximizing:
       bestScore = -100000

       for key in board.keys():
         
         if (board[key] == ' '):
            board[key] = bot
            score = minimax(board,False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
        
       return bestScore
    else:
        bestScore = 100000

        for key in board.keys():
         
         if (board[key] == ' '):
            board[key] = player
            score = minimax(board,True)
            board[key] = ' '
            if (score < bestScore):
                bestScore = score
        
        return bestScore


def botMove():
    bestScore = -100000
    bestMove = 0

    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board,False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    playTurn(bot, bestMove)
    return

while not checkWin():
    botMove()
    playerMove()


