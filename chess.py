letters = 'ABCDEFGH'


class Piece(object):
    def __init__(self, color, position=None):
        self.type = ''
        self.color = color
        self.target = ''
        self.position = position

    def settarget(self, position):
        self.target = position

    def move(self):
        if self.target in self.moves:
            self.position = self.target
            self.moves = generate_moves(self)
            self.attacks = generate_attacks(self)
            return True
        else:
            return False


class Pawn(Piece):
    def __init__(self, color, position=None):
        super(Pawn, self).__init__(color, position)
        self.type = 'pawn'
        if position:
            self.moves = generate_moves(self)
            self.attacks = generate_attacks(self)

    def __str__(self):
        return 'P(' + self.color[0] + ')'


class Queen(Piece):
    def __init__(self, color, position=None):
        super(Queen, self).__init__(color, position)
        self.type = 'queen'
        if position:
            self.moves = generate_moves(self)
            self.attacks = generate_attacks(self)

    def __str__(self):
        return 'Q(' + self.color[0] + ')'


class Desk(object):
    def __init__(self):
 #конструктор класса доски формирует пустые клетки 8х8
        self.cells = {item: ['    '] * 8 for item in letters}

    def __str__(self):
        res = ''
        for row in letters:
            row_str = '|'.join([str(item) for item in self.cells[row]])
            res += row + '|' + row_str + '\n' + '-' * 41 + '\n'
        return res

    def insert(self, piece, position):
        row = self.cells[position[0]]
        row[int(position[1]) - 1] = piece

    def get(self, position):
        return self.cells[position[0]][int(position[1]) - 1]

    def remove(self, position):
        self.cells[position[0]][int(position[1]) - 1] = '    '


def generate_moves(piece):
    position = piece.position
    if piece.type == 'pawn':
        if piece.color == 'WHITE':
            if int(position[1]) + 2 > 8:
                return []
            else:
                return [position[0] + str(int(position[1]) + 2)]
        else:
            if int(position[1]) - 2 < 1:
                return []
            else:
                return [position[0] + str(int(position[1]) - 2)]
    else:
        res = []
        if piece.color == 'WHITE':
            for i in range(int(position[1]) + 1, 9):
                # ходы вперед
                res.append(position[0] + str(i))
                # ходы влево
                shift_left = letters.index(position[0]) + (i - int(position[1])) + 1
                if shift_left < 9:
                    res.append(letters[shift_left - 1] + str(i))
                # ходы вправо
                shift_right = letters.index(position[0]) - (i - int(position[1])) + 1
                if shift_right > 0:
                    res.append(letters[shift_right - 1] + str(i))
        else:
            for i in range(int(position[1]) - 1, 0, -1):
                # ходы вперед
                res.append(position[0] + str(i))
                # ходы влево
                shift_left = letters.index(position[0]) + (i - int(position[1])) + 1
                if shift_left > 0:
                     res.append(letters[shift_left - 1] + str(i))
                # ходы вправо
                shift_right = letters.index(position[0]) - (i - int(position[1])) + 1
                if shift_right < 9:
                    res.append(letters[shift_right - 1] + str(i))
        return res


def generate_attacks(piece):
    position = piece.position
    if piece.type == 'pawn':
        pos1 = letters.index(position[0])
        pos2 = int(position[1])
        res = []
        if piece.color == 'WHITE':
            if (pos1-1 > 0) & (pos2 + 1 > 0):
                res.append(letters[pos1-1] + str(pos2+1))
            if (pos1 + 1 < 9) & (pos2 + 1 < 9):
                res.append(letters[pos1 + 1] + str(pos2 + 1))
        else:
            if (pos1-1 > 0) & (pos2 + 1 > 0):
                res.append(letters[pos1-1] + str(pos2-1))
            if (pos1 + 1 < 9) & (pos2 + 1 < 9):
                res.append(letters[pos1 + 1] + str(pos2 - 1))
    else:
        res = generate_moves(piece)
    return res
