from clear import clear
from parts import parts


def printer(wrong, show, badLetters, goodLetters, guess):
    clear()
    print('')
    print(show)
    print('\n')
    print('Wrong guessed letters: ' + str(badLetters))
    print('Right guessed letters: ' + str(goodLetters))
    print('\n')
    if wrong:
        print('The letter "' + guess + '" is not in the secret word!')
    print('=====================\n')
    print(parts[len(badLetters)])
    print('\n=====================')
    print('\n#### Try again! #####')
    print('=====================')