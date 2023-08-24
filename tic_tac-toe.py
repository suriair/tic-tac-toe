import random


print('Use this template to play the tic-tac-toe.')
print('| 0 | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |')
print('\nNOTE: First player by default get the \'X\' tag.\n')

# Considering the tic-tac-toe game template as 6 x 6 matrix and each cell of the matix is represented by a dict key i.e s_index number.
s_dict = {
            's_0' : ' ',
            's_1' : ' ',
            's_2' : ' ',
            's_3' : ' ',
            's_4' : ' ',
            's_5' : ' ',
            's_6' : ' ',
            's_7' : ' ',
            's_8' : ' '
                        }


# Printing func to display the final output on screen.
def print_plc_hld():
    place_holder = f"| {s_dict.get('s_0')} | {s_dict.get('s_1')} | {s_dict.get('s_2')} |\n| {s_dict.get('s_3')} | {s_dict.get('s_4')} | {s_dict.get('s_5')} |\n| {s_dict.get('s_6')} | {s_dict.get('s_7')} | {s_dict.get('s_8')} |"
    print(place_holder)

# A user input saver in order to avoid repeatation whenever a user repeat the cell which is already taken. 
inp_saver = []

# Player 'X' or player one func, all the necessary code for playing the game inside here.
def player_X():
    while True:
        print('\n')
        inp = input('Enter a place between 0-8: ')
        # Stopping player to populate 's_dict' with new key other than 's_0' to 's_8'.
        if inp == '0' or inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6' or inp == '7' or inp == '8':
            if inp not in inp_saver:
                inp_saver.append(inp)
                var_gen = 's_' + inp
                s_dict[var_gen] = 'X'
                break
            elif inp in inp_saver:
                print('Place already taken. Choose another place.')
        else:
            print('\nWrong input, Only number between 0-8 allowed.')
            continue

# Player 'O' or player two func, all the necessary code for playing the game inside here.
def player_O():
    while True:
        print('\n')
        inp = input('Enter a place between 0-8: ')
        if inp not in inp_saver:
            inp_saver.append(inp)
            var_gen = 's_' + inp
            s_dict[var_gen] = 'O'
            break
        elif inp in inp_saver:
            print('Place already taken. Choose another place.')

# A condition checker func, work as a judge to decide who wins the game.
def winner_decider():
    if s_dict.get('s_0') == s_dict.get('s_1') == s_dict.get('s_2') == 'X' or s_dict.get('s_0') == s_dict.get('s_1') == s_dict.get('s_2') == 'O':
        return True
    elif s_dict.get('s_3') == s_dict.get('s_4') == s_dict.get('s_5') == 'X' or s_dict.get('s_3') == s_dict.get('s_4') == s_dict.get('s_5') == 'O':
        return True
    elif s_dict.get('s_6') == s_dict.get('s_7') == s_dict.get('s_8') == 'X' or s_dict.get('s_6') == s_dict.get('s_7') == s_dict.get('s_8') == 'O':
        return True
    elif s_dict.get('s_0') == s_dict.get('s_3') == s_dict.get('s_6') == 'X' or s_dict.get('s_0') == s_dict.get('s_3') == s_dict.get('s_6') == 'O':
        return True
    elif s_dict.get('s_1') == s_dict.get('s_4') == s_dict.get('s_7') == 'X' or s_dict.get('s_1') == s_dict.get('s_4') == s_dict.get('s_7') == 'O':
        return True
    elif s_dict.get('s_2') == s_dict.get('s_5') == s_dict.get('s_8') == 'X' or s_dict.get('s_2') == s_dict.get('s_5') == s_dict.get('s_8') == 'O':
        return True
    elif s_dict.get('s_0') == s_dict.get('s_4') == s_dict.get('s_8') == 'X' or s_dict.get('s_0') == s_dict.get('s_4') == s_dict.get('s_8') == 'O':
        return True
    elif s_dict.get('s_2') == s_dict.get('s_4') == s_dict.get('s_6') == 'X' or s_dict.get('s_2') == s_dict.get('s_4') == s_dict.get('s_6') == 'O':
        return True


def player_comp():
    
    while True:
        # Ultimate defense code able to thwart strategies.
        if s_dict.get('s_4') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_1') == ' ' and s_dict.get('s_2') == ' ' and s_dict.get('s_3') == 'X' and s_dict.get('s_5') == ' ' and s_dict.get('s_6') == ' ' and s_dict.get('s_7') == ' ' and s_dict.get('s_8') == ' ' and '4' not in inp_saver:
            print('\nComputer turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_1') == 'X' and s_dict.get('s_2') == ' ' and s_dict.get('s_3') == ' ' and s_dict.get('s_5') == ' ' and s_dict.get('s_6') == ' ' and s_dict.get('s_7') == ' ' and s_dict.get('s_8') == ' ' and '4' not in inp_saver:
            print('\nComputer turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_1') == ' ' and s_dict.get('s_2') == ' ' and s_dict.get('s_3') == ' ' and s_dict.get('s_5') == 'X' and s_dict.get('s_6') == ' ' and s_dict.get('s_7') == ' ' and s_dict.get('s_8') == ' ' and '4' not in inp_saver:
            print('\nComputer turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_1') == ' ' and s_dict.get('s_2') == ' ' and s_dict.get('s_3') == ' ' and s_dict.get('s_5') == ' ' and s_dict.get('s_6') == ' ' and s_dict.get('s_7') == 'X' and s_dict.get('s_8') == ' ' and '4' not in inp_saver:
            print('\nComputer turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_0') == 'X' and '4' not in inp_saver or s_dict.get('s_2') == 'X' and '4' not in inp_saver or s_dict.get('s_6') == 'X' and '4' not in inp_saver or s_dict.get('s_8') == 'X' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_0') == 'X' and s_dict.get('s_4') == 'O' and s_dict.get('s_8') == 'X' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and '7' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('7')
            s_dict['s_7'] = 'O'
            break
        elif s_dict.get('s_2') == 'X' and s_dict.get('s_4') == 'O' and s_dict.get('s_6') == 'X' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and '7' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('7')
            s_dict['s_7'] = 'O'
            break
        elif s_dict.get('s_4') == 'X' and s_dict.get('s_0') == ' ' and s_dict.get('s_1') == ' ' and s_dict.get('s_2') == ' ' and s_dict.get('s_3') == ' ' and s_dict.get('s_5') == ' ' and s_dict.get('s_6') == ' ' and s_dict.get('s_7') == ' ' and s_dict.get('s_8') == ' ' and '8' not in inp_saver:
            print('\nComputer turn')
            inp_saver.append('8')
            s_dict['s_8'] = 'O'
            break
        elif s_dict.get('s_0') == 'X' and s_dict.get('s_4') == 'X' and s_dict.get('s_8') == 'O' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and s_dict.get('s_0') == ' ' and '6' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('6')
            s_dict['s_6'] = 'O'
            break
        # Winner logic for all the rows of the matrix.
        # Code for first row.
        elif s_dict.get('s_0')  == s_dict.get('s_1') == 'O' and '2' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('2')
            s_dict['s_2'] = 'O'
            break
        elif s_dict.get('s_0') == s_dict.get('s_2') == 'O' and '1' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('1')
            s_dict['s_1'] = 'O'
            break
        elif s_dict.get('s_1') == s_dict.get('s_2') == 'O' and '0' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('0')
            s_dict['s_0'] = 'O'
            break
        # Code for second row.
        elif s_dict.get('s_3') == s_dict.get('s_4') == 'O' and '5' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('5')
            s_dict['s_5'] = 'O'
            break
        elif s_dict.get('s_3') == s_dict.get('s_5') == 'O' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == s_dict.get('s_5') == 'O' and '3' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('3')
            s_dict['s_3'] = 'O'
            break
        # Code for third row.
        elif s_dict.get('s_6')  == s_dict.get('s_7') == 'O' and '8' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('8')
            s_dict['s_8'] = 'O'
            break
        elif s_dict.get('s_6') == s_dict.get('s_8') == 'O' and '7' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('7')
            s_dict['s_7'] = 'O'
            break
        elif s_dict.get('s_7') == s_dict.get('s_8') == 'O' and '6' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('6')
            s_dict['s_6'] = 'O'
            break
        # Winner logic for all the columns of the matrix.
        # Code for first column.
        elif s_dict.get('s_0')  == s_dict.get('s_3') == 'O' and '6' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('6')
            s_dict['s_6'] = 'O'
            break
        elif s_dict.get('s_0') == s_dict.get('s_6') == 'O' and '3' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('3')
            s_dict['s_3'] = 'O'
            break
        elif s_dict.get('s_3') == s_dict.get('s_6') == 'O' and '0' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('0')
            s_dict['s_0'] = 'O'
            break
        # Code for second column.
        elif s_dict.get('s_1') == s_dict.get('s_4') == 'O' and '7' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('7')
            s_dict['s_7'] = 'O'
            break
        elif s_dict.get('s_1') == s_dict.get('s_7') == 'O' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == s_dict.get('s_7') == 'O' and '1' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('1')
            s_dict['s_1'] = 'O'
            break
        # Code for third column.
        elif s_dict.get('s_2')  == s_dict.get('s_5') == 'O' and '8' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('8')
            s_dict['s_8'] = 'O'
            break
        elif s_dict.get('s_2') == s_dict.get('s_8') == 'O' and '5' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('5')
            s_dict['s_5'] = 'O'
            break
        elif s_dict.get('s_5') == s_dict.get('s_8') == 'O' and '2' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('2')
            s_dict['s_2'] = 'O'
            break
        # Winner logic for all the diagonal of the matrix.
        # Code for left to right daignol.
        elif s_dict.get('s_0')  == s_dict.get('s_4') == 'O' and '8' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('8')
            s_dict['s_8'] = 'O'
            break
        elif s_dict.get('s_0') == s_dict.get('s_8') == 'O' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == s_dict.get('s_8') == 'O' and '0' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('0')
            s_dict['s_0'] = 'O'
            break
        # Code for right to left daigonal.
        elif s_dict.get('s_2')  == s_dict.get('s_4') == 'O' and '6' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('6')
            s_dict['s_6'] = 'O'
            break
        elif s_dict.get('s_2') == s_dict.get('s_6') == 'O' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == s_dict.get('s_6') == 'O' and '2' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('2')
            s_dict['s_2'] = 'O'
            break
        # Defensive logic for all the rows of the matrix.
        # Code for first row.
        elif s_dict.get('s_0')  == s_dict.get('s_1') == 'X' and '2' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('2')
            s_dict['s_2'] = 'O'
            break
        elif s_dict.get('s_0') == s_dict.get('s_2') == 'X' and '1' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('1')
            s_dict['s_1'] = 'O'
            break
        elif s_dict.get('s_1') == s_dict.get('s_2') == 'X' and '0' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('0')
            s_dict['s_0'] = 'O'
            break
        # Code for second row of the matrix.
        elif s_dict.get('s_3')  == s_dict.get('s_4') == 'X' and '5' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('5')
            s_dict['s_5'] = 'O'
            break
        elif s_dict.get('s_3') == s_dict.get('s_5') == 'X' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == s_dict.get('s_5') == 'X' and '3' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('3')
            s_dict['s_3'] = 'O'
            break
        # Code for third row of the matrix.    
        elif s_dict.get('s_6')  == s_dict.get('s_7') == 'X' and '8' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('8')
            s_dict['s_8'] = 'O'
            break
        elif s_dict.get('s_6') == s_dict.get('s_8') == 'X' and '7' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('7')
            s_dict['s_7'] = 'O'
            break
        elif s_dict.get('s_7') == s_dict.get('s_8') == 'X' and '6' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('6')
            s_dict['s_6'] = 'O'
            break
        # Defensive logic for all the columns of the matrix.
        # Code for first column.
        elif s_dict.get('s_0')  == s_dict.get('s_3') == 'X' and '6' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('6')
            s_dict['s_6'] = 'O'
            break
        elif s_dict.get('s_0') == s_dict.get('s_6') == 'X' and '3' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('3')
            s_dict['s_3'] = 'O'
            break
        elif s_dict.get('s_3') == s_dict.get('s_6') == 'X' and '0' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('0')
            s_dict['s_0'] = 'O'
            break
        # Code for second column.
        elif s_dict.get('s_1') == s_dict.get('s_4') == 'X' and '7' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('7')
            s_dict['s_7'] = 'O'
            break
        elif s_dict.get('s_1') == s_dict.get('s_7') == 'X' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == s_dict.get('s_7') == 'X' and '1' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('1')
            s_dict['s_1'] = 'O'
            break
        # Code for third column.
        elif s_dict.get('s_2')  == s_dict.get('s_5') == 'X' and '8' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('8')
            s_dict['s_8'] = 'O'
            break
        elif s_dict.get('s_2') == s_dict.get('s_8') == 'X' and '5' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('5')
            s_dict['s_5'] = 'O'
            break
        elif s_dict.get('s_5') == s_dict.get('s_8') == 'X' and '2' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('2')
            s_dict['s_2'] = 'O'
            break    
        # Defensive logic for all the diagonal of the matrix.
        # Code for left to right daignol.
        elif s_dict.get('s_0') == s_dict.get('s_4') == 'X' and '8' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('8')
            s_dict['s_8'] = 'O'
            break
        elif s_dict.get('s_0') == s_dict.get('s_8') == 'X' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == s_dict.get('s_8') == 'X' and '0' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('0')
            s_dict['s_0'] = 'O'
            break
        # Code for right to left daigonal.
        elif s_dict.get('s_2') == s_dict.get('s_4') == 'X' and '6' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('6')
            s_dict['s_6'] = 'O'
            break
        elif s_dict.get('s_2') == s_dict.get('s_6') == 'X' and '4' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('4')
            s_dict['s_4'] = 'O'
            break
        elif s_dict.get('s_4') == s_dict.get('s_6') == 'X' and '2' not in inp_saver:
            print('\nComputer Turn')
            inp_saver.append('2')
            s_dict['s_2'] = 'O'
            break
        else:
            ran = str(random.randint(0,8))
            if ran not in inp_saver:
                print('\nComputer turn.')
                inp_saver.append(ran)
                var_gen = 's_' + ran
                s_dict[var_gen] = 'O'
                break
            elif ran in inp_saver:
                continue

# Creating while loop so that by any chance if player puts an invalid input other than 'p' or 'c' program doesn't breakdown.
while True:

    nod = input('Press \'C\' to play against Computer Or Press \'P\' to play against player: ')

    if nod == 'P' or nod == 'p':
        while True:
            player_X()
            print_plc_hld()
            if winner_decider():
                print('\nHurry!!! \'X\' WON!')
                break
            elif len(inp_saver) == 9:
                print('\nIt\'s a TIE !!!')
                break
            player_O()
            print_plc_hld()
            if winner_decider():
                print('\nHurry!!! \'O\' WON')
                break
    elif nod == 'C' or nod == 'c':
        while True:
            player_X()
            print_plc_hld()
            if winner_decider():
                print('\nHurry!!! \'X\' WON!')
                break
            elif len(inp_saver) == 9:
                print('\nIt\'s a TIE !!!')
                break
            player_comp()
            print_plc_hld()
            if winner_decider():
                print('\nHurry!!! \'Computer\' WON')
                break
    else:
        print('\nOops, Wrong input!!! Press \'P\' for player or \'C\' for Computer.\n')
        continue
    break