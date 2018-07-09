

import copy
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from functools import partial


class App( QWidget ):

    def __init__(self):
        super().__init__()
        self.title = 'TIC TAC TOE'
        self.left = 10
        self.top = 10
        self.width = 280
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle( self.title )
        self.setGeometry( self.left, self.top, self.width, self.height )
        self.label = QLabel("Test", self)
        #self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.resize(110,30)
        self.label.move(90, 40)
        global counter
        global board
        global player
        global opponent
        self.button1 = QPushButton( self )
        self.button1.resize( 42, 32 )
        self.button1.setToolTip( 'This is an example button' )
        self.button1.move( 80, 70 )

        if not self.button1.text() == '0' and not self.button1.text() == 'X':
            if counter % 2 == 0:
                self.button1.clicked.connect( partial( self.labeltext, "button1", self.button1) )

            else:
                self.button1.clicked.connect( partial( self.labeltext, "button1", self.button1) )


        self.button2 = QPushButton(self )
        self.button2.resize( 42, 32 )
        self.button2.setToolTip( 'This is an example button' )
        self.button2.move( 120, 70 )
        #print( counter )
        if not self.button2.text() == '0' and not self.button2.text() == 'X':
            if counter % 2 == 0:
                self.button2.clicked.connect( partial( self.labeltext, "button2", self.button2) )

            else:

                self.button2.clicked.connect( partial( self.labeltext, "button2", self.button2) )


        self.button3 = QPushButton( self )
        self.button3.resize( 42, 32 )
        self.button3.setToolTip( 'This is an example button' )
        self.button3.move( 160, 70 )
        #print( counter )
        if not self.button3.text() == '0' and not self.button3.text() == 'X':
            if counter % 2 == 0:
                self.button3.clicked.connect( partial( self.labeltext, "button3", self.button3 ) )

            else:
                self.button3.clicked.connect( partial( self.labeltext, "button3", self.button3 ) )


        self.button4 = QPushButton(  self )
        self.button4.resize( 42, 32 )
        self.button4.setToolTip( 'This is an example button' )
        self.button4.move( 80, 100 )
        # self.button2.clicked.connect(self.on_click)
        #print( counter )
        if not self.button4.text() == '0' and not self.button4.text() == 'X':
            if counter % 2 == 0:
                self.button4.clicked.connect( partial( self.labeltext, "button4", self.button4) )

            else:
                self.button4.clicked.connect( partial( self.labeltext, "button4", self.button4) )


        self.button5 = QPushButton(  self )
        self.button5.resize( 42, 32 )
        self.button5.setToolTip( 'This is an example button' )
        self.button5.move( 120, 100 )
        # self.button2.clicked.connect(self.on_click)
        #print( counter )
        if not self.button5.text() == '0' and not self.button5.text() == 'X':
            if counter % 2 == 0:
                self.button5.clicked.connect( partial( self.labeltext, "button5", self.button5 ) )

            else:
                self.button5.clicked.connect( partial( self.labeltext, "button5", self.button5) )


        self.button6 = QPushButton(  self )
        self.button6.resize( 42, 32 )
        self.button6.setToolTip( 'This is an example button' )
        self.button6.move( 160, 100 )
        #print( counter )
        if not self.button6.text() == '0' and not self.button6.text() == 'X':
            if counter % 2 == 0:
                self.button6.clicked.connect( partial( self.labeltext, "button6", self.button6 ) )

            else:
                self.button6.clicked.connect( partial( self.labeltext, "button6", self.button6 ) )


        self.button7 = QPushButton( self )
        self.button7.resize( 42, 32 )
        self.button7.setToolTip( 'This is an example button' )
        self.button7.move( 80, 130 )
        #print( counter )
        if not self.button7.text() == '0' and not self.button7.text() == 'X':
            if counter % 2 == 0:
                self.button7.clicked.connect( partial( self.labeltext, "button7", self.button7 ) )

            else:
                self.button7.clicked.connect( partial( self.labeltext, "button7", self.button7 ) )


        self.button8 = QPushButton(  self )
        self.button8.resize( 42, 32 )
        self.button8.setToolTip( 'This is an example button' )
        self.button8.move( 120, 130 )
        #print( counter )
        if not self.button8.text() == '0' and not self.button8.text() == 'X':
            if counter % 2 == 0:
                self.button8.clicked.connect( partial( self.labeltext, "button8", self.button8 ) )

            else:
                self.button8.clicked.connect( partial( self.labeltext, "button8", self.button8) )


        self.button9 = QPushButton(  self )
        self.button9.resize(42, 32)
        self.button9.setToolTip( 'This is an example button' )
        self.button9.move( 160, 130 )
        #print( counter )
        if not self.button9.text() == '0' and not self.button6.text() == 'X':
            if counter % 2 == 0:
                self.button9.clicked.connect( partial( self.labeltext, "button9", self.button9 ) )

            else:
                self.button9.clicked.connect( partial( self.labeltext, "button9", self.button9 ) )


        self.show()

    # @pyqtSlot()
    # def on_click(self):
    #     print( "DADD" )
    #     self.setText( "Sdd" )

    def labeltext(self, text, button):
        global counter
        if not button.text() == 'X' and not button.text() =="0":
            if counter%2 ==0:
                button.setText( 'X' )
                counter += 1
                global board
                if text[-1]=="1":
                    board[0][0] = 2
                elif text[-1]=="2":
                    board[0][1] = 2
                elif text[-1]=="3":
                    board[0][2] = 2
                elif text[-1]=="4":
                    board[1][0] = 2
                elif text[-1]=="5":
                    board[1][1] = 2
                elif text[-1]=="6":
                    board[1][2] = 2
                elif text[-1]=="7":
                    board[2][0] = 2
                elif text[-1]=="8":
                    board[2][1] = 2
                elif text[-1] == "9":
                    board[2][2] = 2
                boardcopy = copy.deepcopy(board)
                x, y = self.findbestmove(boardcopy)
                global won
                if won == "C":
                    self.label.setText("Computer Won")
                    print("Computer Won")
                    return
                if won == "H":
                    self.label.setText( "Human Won" )
                    print( "Human Won" )
                    return

                board[x][y]=1
                #button.setText( '0' )
                if x == 0 and y == 0:
                    self.button1.setText('0')
                elif x == 0 and y == 1:
                    self.button2.setText('0')
                elif x == 0 and y == 2:
                    self.button3.setText('0')
                elif x == 1 and y == 0:
                    self.button4.setText('0')
                elif x == 1 and y == 1:
                    self.button5.setText('0')
                elif x == 1 and y == 2:
                    self.button6.setText('0')
                elif x == 2 and y == 0:
                    self.button7.setText('0')
                elif x == 2 and y == 1:
                    self.button8.setText('0')
                elif x == 2 and y == 2:
                    self.button9.setText('0')
                counter +=1

    def isMovesLeft(self, board):
        for i in range( 3 ):
            for j in range( 3 ):
                if board[i][j] == 0:
                    return True
        return False

    def evaluate(self, board):
        global player
        global opponent
        for i in range( 3 ):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                if board[i][0] == player:
                    return +10
                elif board[i][0] == opponent:
                    return -10
        for j in range( 3 ):
            if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
                if board[0][j] == player:
                    return +10
                elif board[0][j] == opponent:
                    return -10
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == player:
                return +10
            elif board[0][0] == opponent:
                return -10
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == player:
                return +10
            elif board[0][2] == opponent:
                return -10
        return 0

    def minimax(self, board, depth, maxmin):
        score = self.evaluate( board )
        # print(player)
        if score == 10:
            return 10
        if score == -10:
            return -10
        if self.isMovesLeft( board ) == False:
            return 0
        if maxmin:
            best = -100000
            for i in range( 3 ):
                for j in range( 3 ):
                    if board[i][j] == 0:
                        board[i][j] = player
                        best = max( best, self.minimax( board, depth + 1, not maxmin ) )
                        board[i][j] = 0
            return best
        else:
            best = 100000
            for i in range( 3 ):
                for j in range( 3 ):
                    if board[i][j] == 0:
                        board[i][j] = opponent
                        # print("Here")
                        best = min( best, self.minimax( board, depth + 1, not maxmin ) )
                        board[i][j] = 0
            return best

    def findbestmove(self, board):
        best_val = -100000
        # print("Board")
        print( board )
        x = -1
        y = -1
        global won
        for i in range( 3 ):
            for j in range( 3 ):
                if board[i][j] == 0:
                    board[i][j] = player
                    best = self.minimax( board, 0, False )
                    # print(best)
                    board[i][j] = 0
                    if best > best_val:
                        x = i
                        y = j
                        best_val = best
                    # if best_val ==10:
                    #     print("Computer Won")
                    #     #exit()
                    #     won = "C"
                    #     return (9,9)
                    # elif best_val == -10:
                    #     print("Human Won")
                    #
                    #     won = "H"
                    #     return (9,9)
                    #     exit()
        print( x, y )
        return (x, y)



# board = [[2,1,2],[1,1,2],[0,0,0]]
counter = 0
player = 2
opponent = 1
app = QApplication( sys.argv )
ex = App()
sys.exit( app.exec_() )

# bestMove = findbestmove(board)
# print(bestMove)