import random
import string
from words import words
import requests
import re
from lxml import html
import csv,os,json

def get_valid_word():
    url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1"
    resposta = requests.get(url)
    elemento = html.fromstring(resposta.content)
    word = elemento.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
    word = word[0].strip()
    return word.upper()


lives_visual_dict = {

        0: """
                ___________
               | /        | 
               |/        ( )
               |         /|\\
               |         / \\
               |
               ========
            """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |         /|
               |         / \\
               |
               ========
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
               ========
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
               ========
            """,
        4: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
               ========
            """,
        5: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
               ========
            """,
        6: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
               ========
            """,
        7: """
                ___________
               | /        
               |/        
               |          
               |          
               |
               ========
            """,
        8: """
               |
               |
               |
               |
               |
               ========
            """,
        9: """





                ========
        """,
    }
def hangman():
    word = get_valid_word()
    word_letters = set(word) #letters that are in the word
    alphabet = set(string.ascii_uppercase) #alphabet (uppercase)
    used_letters = set() #to put the letters guessed

    lives = 9

    while len(word_letters) > 0 and lives > 0:
        print('Você tem', lives, 'vidas restantes e você já usou as seguintes letras: ', ' '.join(used_letters)) #user keeps track of guessed letters
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Palavra: ", " ".join(word_list))

        user_guess = input("Chute uma letra: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print("")
            elif user_guess in used_letters:
                lives = lives - 1
                print("Você já usou essa letra. Tente de novo")
        else:
            print("Símbolo inválido. Tente de novo")
    if lives == 0:
        print(lives_visual_dict[lives])
        print("Desculpa, mas você morreu. A palavra era", word)

    else:
        print("Uhuuuu! Você acertou", word, "!")

while True:
    hangman()
    again = input("Jogar de novo?").lower()
    if again.startswith("n"):
        print("Valeu entäo")
        break
    print("Bora lá!")



#if __name__ == '__main__':
#    hangman()