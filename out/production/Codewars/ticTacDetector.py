# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:

# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).


# first approach
def chklist(board):
    return len(set(board)) == 1

def is_solved(board):
    countI = 0
    countJ = 0
    countK = 0
    countL = 0
    countM = 0
    countN = 0
    
    flag = False
    for i in range(0, len(board)):
        print(board[i])
        if chklist(board[i]) and board[i][0]==1:
            flag = True
            return 1
        elif chklist(board[i]) and board[i][0]==2:
            flag = True
            return 2
        elif(board[i][0] == 1):
            countI+=1
        
        if(board[i][0] == 2):
            countJ+=1   
        if(board[i][1] == 1):
            countK+=1
        
        if(board[i][1] == 2):
            countL+=1    
        if(board[i][2] == 1):
            countM+=1
        
        if(board[i][2] == 2):
            countN+=1    
      
    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return 2
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return 1
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        return 2
    elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        return 1
    
    elif any(0 in sl for sl in board) and not flag:
        return -1
    
    if countI == 3:
        return 1
    elif countJ == 3:
        return 2
    elif countK == 3:
        return 1
    elif countL == 3:
        return 2
    elif countM == 3:
        return 1
    elif countN == 3:
        return 2
    else:
        return 0


#cleaned approach

def is_solved(board):
    countI = 0
    countJ = 0
    countK = 0
    countL = 0
    countM = 0
    countN = 0

    flag = False
    for i in range(0, len(board)):
        if (len(set(board[i])) == 1) and board[i][0]==1:
            return 1
        elif (len(set(board[i])) == 1) and board[i][0]==2:
            return 2
        
        elif(board[i][0] == 1):
            countI+=1
        
        if(board[i][0] == 2):
            countJ+=1   
        
        if(board[i][1] == 1):
            countK+=1
        
        if(board[i][1] == 2):
            countL+=1    
        
        if(board[i][2] == 1):
            countM+=1
        
        if(board[i][2] == 2):
            countN+=1    
    
    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return 2
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return 1
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        return 2
    elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        return 1
    
    elif any(0 in sl for sl in board) and not flag:
        return -1
    
    if countI == 3 or countK ==3 or countM==3:
        return 1
    elif countJ == 3 or countL==3 or countN==3:
        return 2

    return 0