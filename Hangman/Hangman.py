import random
from colorama import Fore, Style, init
init()


# List of words for the Hangman game
words = ['python', 'challenge', 'hangman', 'programming', 'developer', 'pizza', 'guitar', 'university', 'adventure', 'mystery']

# Word categories (for hints)
word_categories = {
    'python': '🐍 Programming Language',
    'challenge': '🏆 Something difficult',
    'hangman': '🎮 The name of this game',
    'programming': '💻 Writing code',
    'developer': '👩‍💻 Someone who codes',
    'pizza': '🍕 A delicious food',
    'guitar': '🎸 A musical instrument',
    'university': '🎓 An institution of higher education',
    'adventure': '🎢 An exciting experience',
    'mystery': '🤫 Something unknown or unclear'
}




# Hangman ASCII art stages (from 6 attempts to 0)
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """
]
while True:
    name = input('Enter your name: ')
    print(f'Is your name {name}? (yes/no)')
    if input().lower() == 'yes':
        print(f'\nWelcome, {name}! Let\'s start the game!')
        break
    else:
        print('Please enter your name again.')
        continue

play_again = True

while play_again:
    
    secret_word = random.choice(words)
    category = word_categories.get(secret_word, 'General')

    # Create blanks for the secret word
    blanks = ['_'] * len(secret_word)

    print('Welcome to Hangman!')
    # Display the initial blanks
    print(' '.join(blanks))

    guessed_letters = []
    attempts = 6

    while attempts > 0 and '_' in blanks:
        print(f"\n📝 Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

    # Check if already guessed letters
        guess = input('\nGuess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print(f'{Fore.RED}Invalid input. Please enter a single letter.{Style.RESET_ALL}')
            continue

        if guess in guessed_letters:
            print(f'{Fore.RED}You already guessed that letter. Try again.{Style.RESET_ALL}')
            continue

        guessed_letters.append(guess)

    # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print(f'{Fore.GREEN}Good guess!{Style.RESET_ALL}')
       
        # Update the blanks with the guessed letter
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    blanks[i] = guess
            print(' '.join(blanks))
    
        else:
            print(f'{Fore.RED}Wrong guess!{Style.RESET_ALL}')
            attempts -= 1
            print(hangman_stages[6 - attempts])
            print(f'{Fore.YELLOW} You have {attempts} attempts left.{Style.RESET_ALL}')
            print(' '.join(blanks))
            print(f'📖 Hint: {category}')

        if '_' not in blanks:
            print(f"\n🎉 Congratulations {name}! You guessed the word: {secret_word}")
            break

    else:
        print(f"\n{Fore.RED}☠️ Game Over! The secret word was: {secret_word}{Style.RESET_ALL}")

    print('=' * 50)
    play_again = input('Do you want to play again? (yes/no): ').lower() 
    if play_again != 'yes'and play_again != 'y':
        play_again = False
        print('Thanks for playing! Goodbye!')

print('=' * 50)
print(Fore.GREEN + f'\n Thanks for playing, {name}! See you next time!' + Style.RESET_ALL)


    

