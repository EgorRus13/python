intro = """
   ▓▀▀▀▀▄   ▐█    ██   ▄▓▀▀▀▀▄   █▒▀▀▀▒      ▓▀▓      ▐█    ██                  ▓▀▓
   ▒▌▄▄▄▀   ▐█  ▄█▀█  ▓▌         █▌         ▓▌ ▐▓     ▐█  ▄█▀█                 ▓▌ ▐▓ 
   ▒▌  ▀█▄  ▐█╔▓▀ ▐█  █          █▌█▌█▌    ▓▌   ▐▓    ▐█╔▓▀ ▐█                ▓▌▄▄▄▐▓ 
   ▒▌  ▄█▀  ▐██   ▐█  ▀▓▄    ▄   █▌       ▓▌     ▐▓   ▐██   ▐█               ▓▌     ▐▓
   ▀▀▀▀     ▀▀     ▀     ▀▀▀▀    ▓▒▄▄▄▒  ▐█       █▌  ▀▀     ▀  ▄▄▄▄▄▄▄▄▄▄  ▐█       █▌
"""

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
print(intro)

vocabulary = ['Egor', 'Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty',
              'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
word_answer = random.choice(vocabulary).lower()
word_display = []
for i in range(len(word_answer)):
    word_display.append("_")
counter = 0
life = 6
print(word_display)
while counter != len(word_answer) and life > 0:
    print(stages[life])
    letter = input("Bukva:")
    lib = False
    for i in range(len(word_answer)):
        if letter == word_answer[i]:
            if word_display[i] != "_":
                lib = True
            else:
                word_display[i] = letter
                counter += 1
                lib = True
    if not lib:
        life = life - 1
    print(word_display)
if counter == len(word_answer):
    print("You win! Celebrations!")
else:
    print(stages[life])
    print("Otvet", word_answer)
    print("You lose!")
