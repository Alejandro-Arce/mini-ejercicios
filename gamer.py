
import random
import os

def run():

    IMAGE = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']   

    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP",
    ]


    word=random.choice(DB)
    speces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("cls")
        for character in speces:
            print (character,end=" ")
        print (IMAGE[attemps])
        letra= input("elige una letra").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letra:
                speces[idx]= letra
                found= True

        if not found:
            attemps -=1

        if "_" not in speces:
            os .system("clear")
            print ("ganastes")
            break
            input()


        if attemps == 0:
            os .system("clear")
            print ("perdistes")
            break
            input()


    if __name__ == "__main__":
        run()

