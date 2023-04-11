import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    player = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

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
        """
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
        """
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
        """
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
        """
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
        """
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
        """
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
