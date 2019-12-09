from Life import Life
from word import Word


def start():
    word = Word('words.txt')
    life = Life()
    num_of_tries = 0
    while life.is_alive():
        print(life.display_life_state())
        print('Current:', word.current_status)
        print('Tries:', num_of_tries)
        print('Life:', life.remaining_life)

        entered_char = input('Select a letter: ')
        if len(entered_char) != 1:
            print('One character at a time!')
            continue

        if entered_char >= 'a' and entered_char <= 'z':
            print('Must enter alphabet')
            continue

        entered_char = entered_char.lower()
        if entered_char in word.get_guessed_characters():
            print('You already entered \"' + entered_char + '\"')
            continue

        result = word.guess(entered_char)

        if result == 1:
            print('Success')
            return
        if result == -1:
            num_of_tries += 1
            life.decrease()
            continue

    print(life.display_life_state())
    print('word [' + word.get_word() + ']')
    print('guess [' + word.current_status + ']')
    print('Fail')


if __name__ == '__main__':
    start()