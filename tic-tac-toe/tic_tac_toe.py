def print_board(lst):
    st = '''
 {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}
'''.format(*lst)
    print(st)

choices = [' '] * 9
print('Welcome to Tic Tac Toe!')
print_board(choices)

name1 = input('Enter Player 1 name: ')
name2 = input('Enter Player 2 name: ')
turns = 'X'
name = name1

for i in range(9):
    try:
        mv = int(input(f"{name}'s turn ({turns}). Enter your move [0-8]: "))
        if mv < 0 or mv > 8 or choices[mv] != ' ':
            print("Invalid move! Please try again.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 8.")
        continue

    choices[mv] = turns
    print_board(choices)

    if (choices[0] == choices[1] == choices[2] != ' ' or  
        choices[3] == choices[4] == choices[5] != ' ' or  
        choices[6] == choices[7] == choices[8] != ' ' or  
        choices[0] == choices[3] == choices[6] != ' ' or  
        choices[1] == choices[4] == choices[7] != ' ' or  
        choices[2] == choices[5] == choices[8] != ' ' or  
        choices[0] == choices[4] == choices[8] != ' ' or  
        choices[2] == choices[4] == choices[6] != ' '):
        print(f"Congratulations {name}, you won!")
        break

    # Switch turns and player
    turns = 'X' if turns == '0' else '0'
    name = name1 if name == name2 else name2
else:
    print("It's a draw!")
