tiles = {1:1, 2:2, 3:3, 
         4:4, 5:5, 6:6,
         7:7, 8:8, 9:9}

class Tic_Tac_Toe:
    def __init__(self):
        print(f" {tiles[1]} | {tiles[2]} | {tiles[3]} "\
                "\n___________\n"\
                f" {tiles[4]} | {tiles[5]} | {tiles[6]} "\
                "\n___________\n"\
                f" {tiles[7]} | {tiles[8]} | {tiles[9]} ")

Tic_Tac_Toe()