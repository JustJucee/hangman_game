print('Вы играете в игру hangman')
word = 'java'
# Create a list to store the correctly guessed letters
guessed_letters = ["_"] * len(word)
count = 6
while True:
    if count > 0:
        print(f'You have {count} tries left')
        print("Word:", " ".join(guessed_letters))
        a = input('Введите букву: ')
        if a in word:
            for i in range(len(word)):
                if word[i] == a:
                    guessed_letters[i] = a
            if "_" not in guessed_letters:
                print(f'You guessed the word {word}!')
                break
        else:
            print(f'You have {count} tries left')
            count -= 1
    else:
        print('You lose this game')
        break
    