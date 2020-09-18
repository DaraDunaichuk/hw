from chess import Desk, Pawn, Queen

colors = ['WHITE', 'BLACK']


def pieces():
    #метод тестирования классов фигур
    # пешки
    p = [Pawn(colors[0], position='D2'), Pawn(colors[1], position='D7'), Pawn(colors[0], position='A2'),
         Pawn(colors[1], position='A7')]
    print('Test pawns')
    for item in p:
        print('Pawn at ' + item.position + '. Moves: ' + str(item.moves) + ' Attacks: ' + str(item.attacks))

    # ферзи
    q = [Queen(colors[0], position='D1'), Queen(colors[1], position='D8')]
    print('Test queens')
    for item in q:
        print('Queen at ' + item.position + '. Moves: ' + str(item.moves) + '\nAttacks: ' + str(item.attacks))

    # цель ферзя клетка D2
    q[0].settarget('D2')
    if q[0].move():
        print('New position: ' + q[0].position)
    else:
        print("Position can't be changed")

    # цель ферзя клетка C4
    q[0].settarget('C4')
    if q[0].move():
        print('New position: ' + q[0].position)
    else:
        print("Position can't be changed")


def desk():
    #метод тестирования класса доски """
    mydesk = Desk()
    for i in 'ABCDEFGH':
        mydesk.insert(Pawn(colors[0]), i+'2')
        mydesk.insert(Pawn(colors[1]), i+'7')
    mydesk.insert(Queen(colors[0]), 'D1')
    mydesk.insert(Queen(colors[1]), 'D8')
    print(mydesk)
    mydesk.remove('A2')
    mydesk.remove('A7')
    print(mydesk)


if __name__ == '__main__':
    print('Pieces Class demo')
    pieces()
    print('\n\nDesk Class demo')
    desk()