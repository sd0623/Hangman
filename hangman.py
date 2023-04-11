import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_complete = "_ " * len(word)
    right = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display(tries))
    print(word_complete)
    print("\n")
    while not right and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("ALREADY GUESSED LETTER!", guess)
            elif guess not in word:
                print(guess, "IS NOT IN THE WORD!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("NICE")
                print(guess, "in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
            if "_" not in word_complete:
                right = True
        elif len(guess) == len(word) and guess.isalnum():
            if guess in guessed_words:
                print("ALREADY GUESSED WORD!", guess)
            elif guess != word:
                print(guess, "IS NOT THE WORD!")
                tries -= 1
                guessed_words.append(guess)
            else:
                right = True
                word_complete = guess
        else:
            print("NOT A VALID GUESS!")
        print(display(tries))
        print(word_complete)
        print("\n")
    if right:
        print("!!!!!CONGRATS!!!!!")
        print("You have guessed the word!")
    else:
        print("OOPS")
        print("You ran out of tries. The word was " + word + " Try again!")

def display(tries):
    stages = [
        # final stage: head, body, both arms, both legs
        """
            ------------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            |
            ------------
        """,
        # head, body, both arms, one leg
        """
            ------------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            |
            ------------
        """,
        # head, body, both arms
        """
            ------------
            |      |
            |      O
            |     \\|/
            |      |
            |     
            |
            ------------
        """,
        # head, body, one arm
        """
            ------------
            |      |
            |      O
            |     \\|
            |      |
            |     
            |
            ------------
        """,
        # head, body
        """
            ------------
            |      |
            |      O
            |      |
            |      |
            |     
            |
            ------------
        """,
        # head
        """
            ------------
            |      |
            |      O
            |     
            |      
            |     
            |
            ------------
        """,
        # empty
        """
            ------------
            |      |
            |      
            |     
            |      
            |     
            |
            ------------
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()