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
    
    def move(self):
        while True:
            spot = input(f"Player {self.mark}: ") 
            if int(spot) > 9:
                print("Out Of Range\n")
            elif (tiles[spot] == "X" or tiles[spot] == "O"): 
                print("Invalid Move\n")
            else:
                break
        tiles[spot] = self.mark
        Tic_Tac_Toe()
        
    def winner(self):
        if tiles['1'] == self.mark and tiles['2'] == self.mark and tiles['3'] == self.mark or\
            tiles['4'] == self.mark and tiles['5'] == self.mark and tiles['6'] == self.mark or\
                tiles['7'] == self.mark and tiles['8'] == self.mark and tiles['9'] == self.mark or\
                    tiles['1'] == self.mark and tiles['4'] == self.mark and tiles['7'] == self.mark or\
                        tiles['2'] == self.mark and tiles['5'] == self.mark and tiles['8'] == self.mark or\
                            tiles['3'] == self.mark and tiles['6'] == self.mark and tiles['9'] == self.mark or\
                                tiles['1'] == self.mark and tiles['5'] == self.mark and tiles['9'] == self.mark or\
                                    tiles['3'] == self.mark and tiles['5'] == self.mark and tiles['7'] == self.mark:
            return "Winner"
        

Tic_Tac_Toe()

player1 = Players("X")
player2 = Players("O")

turns = 0
while turns < 9:   
    player1.move() 
    turns += 1
    if player1.winner():
        print(f"Player {player1.mark} is the winner")
        break
    
    if turns == 9:
        print("Draw")
        break 
    
    player2.move() 
    turns += 1
    if player2.winner():
        print(f"Player {player2.mark} is the winner")
        break  
    


