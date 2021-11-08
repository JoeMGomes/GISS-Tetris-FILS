from enum import Enum

RHODEISLAND = [['.....',
                '......',
                '..00..',
                '.00...',
                '.....'],
                ['.....',
                 '..0..',
                 '..00.',
                 '...0.',
                 '.....']]

CLEVELAND = [['.....',
              '.....',
              '.00..',
              '..00.',
              '.....'],
              ['.....',
               '..0..',
               '.00..',
               '.0...',
               '.....']]

HERO = [['..0..',
         '..0..',
         '..0..',
         '..0..',
         '.....'],
         ['.....',
          '0000.',
          '.....',
          '.....',
          '.....']]

SMASHBOY = [['.....',
             '.....',
             '.00..',
             '.00..',
             '.....']]

BLUERICKY = [['.....',
              '.0...',
              '.000.',
              '.....',
              '.....'],
              ['.....',
               '..00.',
               '..0..',
               '..0..',
               '.....'],
              ['.....',
               '.....',
               '.000.',
               '...0.',
               '.....'],
               ['.....',
                '..0..',
                '..0..',
                '.00..',
                '.....']]

ORANGERICKY = [['.....',
                '...0.',
                '.000.',
                '.....',
                '.....'],
               ['.....',
                '..0..',
                '..0..',
                '..00.',
                '.....'],
               ['.....',
                '.....',
                '.000.',
                '.0...',
                '.....'],
               ['.....',
                '.00..',
                '..0..',
                '..0..',
                '.....']]

TEEWEE = [['.....',
           '..0..',
           '.000.',
           '.....',
           '.....'],
          ['.....',
           '..0..',
           '..00.',
           '..0..',
           '.....'],
          ['.....',
           '.....',
           '.000.',
           '..0..',
           '.....'],
          ['.....',
           '..0..',
           '.00..',
           '..0..',
           '.....']]

class PieceType(Enum):
    ORANGERICKY = 0
    BLUERICKY = 1
    CLEVELAND = 2
    RHODEISLAND = 3
    HERO = 4
    TEEWEE = 5
    SMASHBOY = 6


PieceDictionary = {
    PieceType.ORANGERICKY: ORANGERICKY,
    PieceType.BLUERICKY: BLUERICKY,
    PieceType.CLEVELAND: CLEVELAND,
    PieceType.RHODEISLAND: RHODEISLAND,
    PieceType.HERO: HERO,
    PieceType.TEEWEE: TEEWEE,
    PieceType.SMASHBOY: SMASHBOY,
}

PieceColors = [(255,200,0),#Orange
            (50,50,255), #Blue
            (255,0,0), #Red
            (230,230,250), # Purple
            (50,255,50), # Green
            (255,255,0), #Yellow
            (255,100,255) #pink
]

# returns the positions on the grid occupied by a piece
def occupied_positions(piece_type, position, rotation):
    occupied_positions = []
    textFormat = PieceDictionary[piece_type][rotation]

    for i in range(len(textFormat)):
        for j in range(len(textFormat[i])):
            if textFormat[i][j] == '0':
                occupied_positions.append((j+ position[0] - 2,i+ position[1] - 4))
    
    return occupied_positions