import random
turns = ['rock','paper','scissors']

while (True):
    human_turn = input('Enter your turn:')
    computer_turn = random.choice(turns)

    if human_turn == 'exit':
        print('Thank you for playing!')
        break

    print(f'{human_turn} vs. {computer_turn}')
    if human_turn == computer_turn:
        print('Tie!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
    else:
        print('Computer wins!')