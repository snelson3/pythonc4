'''
the logic for checking for 4 in a 3D array is kind of complex,
 but I can just provide him with that function,
 and I think 3D arrays are simpleish otherwise.
 I should be able to do this without classes, code it as simply as I can using if's/for's/whiles

simple AI checks are to check if they can win with a move then check if they need to block an
opponents win then check which move gives them the most directions.

Also buy Amtrak ticket
'''

import random

def place(player,col):
    if player == 0:
        col.append('X')
    else:
        col.append('O')

def canPlace(col):
    return len(col) < 6

def printBoard(b):
    for j in range(6):
        st = ''
        for i in range(7):
            try:
                st += b[i][5-j] + " "
            except IndexError:
                st += "  "
        print st

def gameOver(board):
    #Search up each column and left to right
    placed = 0
    for i in range(7):
        length = len(board[i])
        placed += length
        for j in range(6):
            if length-1 >= j:
                piece = board[i][j]
                #check up for c4
                cu = random.randrange(0,4)
                #check right for c4
                cr = random.randrange(0,4)
                #check diag up/right for c4
                cd = random.randrange(0,4)
                #check diag down/right for c4
                cdr = random.randrange(0,4)
                if max(cu,cr,cd,cdr) == 4:
                    return 1 if piece == 'O' else 0
    if placed == 7*6:
        return -1
    return 0


def cpuTurn(board,player):
    while 1:
        #This has to terminate because of gameOver
        p = random.randrange(0,6)
        if canPlace(board[p]):
            place(player,board[p])
            return

def playerTurn(board,player):
    printBoard(board)
    cl = raw_input("Input the column where you want to play your piece\n")
    if cl not in ['1','2','3','4','5','6','7']:
        print("Invalid input, try again")
        playerTurn(board,player)
        return
    col = board[int(cl)-1]
    if not canPlace(col):
        print("That column is full, try again")
        playerTurn(board,player)
        return
    place(player,col)

def playGame(player2):
    players = ('cpu', player2)
    startingplayer = random.randrange(0,1)
    currentplayer = startingplayer
    '7x6 board, extension would be to make it able to be any size'
    board = [[],[],[],[],[],[],[]]
    print "The game is starting, player " + str(startingplayer+1) + " goes first."
    while not gameOver(board):
        print "Now it is player " + str(currentplayer+1) + "'s turn."
        if players[currentplayer] == 'cpu':
            cpuTurn(board,currentplayer)
        else:
            playerTurn(board,currentplayer)
        currentplayer = abs(currentplayer - 1)
    print "Congratulations player " + str(gameOver(board) + 1) + ", you win."


def main():
    pla = raw_input( "Hey this is connect 4, press 1 to play with a person, 2 for a computer, else quit\n" )
    if pla == '1':
        playGame("human")
    elif pla == '2':
        playGame("cpu")
    else:
        pass

'''
X
O O    O
O X    O
X O    X
O O  O X   O
X X  O X X X
'''

tst = [['X','O','X','O','X','X'],['X','O','O','X','O'],['X','X','X'],['O','X','O','O'],['X','X','X','O','O'],['X'],['X','O']]

printBoard(tst)
print gameOver(tst)