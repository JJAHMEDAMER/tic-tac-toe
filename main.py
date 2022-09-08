tiles = {'1':1, '2':2, '3':3, 
         '4':4, '5':5, '6':6,
         '7':7, '8':8, '9':9}

class Tic_Tac_Toe:
    def __init__(self):
        print(f" {tiles['1']} | {tiles['2']} | {tiles['3']} "\
                "\n___________\n"\
                f" {tiles['4']} | {tiles['5']} | {tiles['6']} "\
                "\n___________\n"\
                f" {tiles['7']} | {tiles['8']} | {tiles['9']} \n")

class Players:
    def __init__(self, mark):
        self.mark = mark
    
    def move(self,spot):
        if tiles[spot] == "X" or tiles[spot] == "O":
            print("Invalid Move\n")
        else:
            tiles[spot] = self.mark
        Tic_Tac_Toe()


Tic_Tac_Toe()

player1 = Players("X")
player2 = Players("O")

while True:         
    player1.move(input("Player 1: "))
    player2.move(input("Plater 2: "))
