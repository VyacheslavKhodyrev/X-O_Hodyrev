#Игра "крестики-нолики" Ходырев В.В. FPW-164

#Игровое поле
playing_field = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]

#Выигрышные комбинации
win_combinations = [
                ((0, 0), (0, 1), (0, 2)), #Верхняя горизонталь
                ((1, 0), (1, 1), (1, 2)), #Средняя горизонталь
                ((2, 0), (2, 1), (2, 2)), #Нижняя горизонталь
                ((0, 0), (1, 0), (2, 0)), #Левая вертикаль
                ((0, 1), (1, 1), (2, 1)), #Средняя вертикаль
                ((0, 2), (1, 2), (2, 2)), #Правая вертикаль
                ((0, 0), (1, 1), (2, 2)), #Левая диагональ
                ((0, 2), (1, 1), (2, 0))  #Правая диагональ
]

#Лист координат ходов игроков
player_1 = []
player_2 = []

#Номера игроков
player_num_1 = 1
player_num_2 = 2

#Номер хода
num = 0

#Номера ходов игроков
num_move_X = list(range(1, 10, 2))
num_move_Y = list(range(2, 10, 2))

#Счетчик ходов
count_move = 1


#Функция для печати игрового поля
def print_playing_field(args):
    print(f'   0 1 2')
    n = 0
    for a in args:
        a = a
        print(f'{n} ', *a)
        n += 1


print('ДОБРО ПОЖАЛОВАТЬ В ИГРУ "КРЕСТИКИ-НОЛИКИ"!')
print('')

print_playing_field(playing_field)


#Функция определения номера игрока
def num_player(count_move):
    global num
    if count_move in num_move_X:
        num = player_num_1
    elif count_move in num_move_Y:
        num = player_num_2
    return num


#Функция одного хода игры
def play_func(num):
    print('')
    print(f'Ваш ход, игрок {num_player(num)}')
    print('')
    i = int(input(f'Введите координату ячейки по вертикали от 0 до 2: '))
    j = int(input(f'Введите координату ячейки по горизонтали от 0 до 2: '))
    if playing_field[i][j] == '-':
        if num % 2 != 0:
            playing_field[i][j] = 'X'
            player_1.append((i, j))
        else:
            playing_field[i][j] = 'O'
            player_2.append((i, j))
    else:
        playing_field[i][j] = playing_field[i][j]
        print(f'Ячейка с координатами: {i}, {j} занята, введите координаты повторно')
        print(' ')
        print(f'Ваш ход, игрок {num_player(num)}')
        print(' ')
        i = int(input(f'Введите координату ячейки по вертикали от 0 до 2: '))
        j = int(input(f'Введите координату ячейки по горизонтали от 0 до 2: '))
        if num % 2 != 0:
            playing_field[i][j] = 'X'
            player_1.append((i, j))
        else:
            playing_field[i][j] = 'O'
            player_2.append((i, j))
    print_playing_field(playing_field)
    return playing_field


#Функция для определения выигрышной комбинации
def stop_game():
    list_c = []
    list_d = []
    for combination in win_combinations:
        c = set(combination).intersection(set(player_1))
        d = set(combination).intersection(set(player_2))
        if len(c) == 3 or len(d) == 3:
            list_c.append(c)
            list_d.append(d)
    if len(list_c) or len(list_d):
        print(f'Поздравляем с выигрышем, игрок {num_player(num)}')
        return True
    else:
        return False


#Функция игры
def play(n):
    global count_move
    n = 1
    while n <= 9:
        play_func(count_move)
        n += 1
        count_move = n
        z = stop_game()
        if z:
            break
    return count_move

play(count_move)
