import pygame
from words import WORDS 
import random
import sys

# pygame.init()

WIDTH, HEIGHT = 633, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("Tiles.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

CORRECT_WORD = random.choice(WORDS)
print(CORRECT_WORD)
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

pygame.display.set_caption("Wordle!")

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

current_word = ''
game_won = ''
words = []
bg_colors = []

guesses = 0


def reset():
    print('reset')

def check_words():
    global current_word,guesses,CORRECT_WORD
    temp_list = []
    words.append(current_word)
    for i in range(len(current_word)):
        print(guesses,current_word[i],CORRECT_WORD[i])
        if current_word[i].lower() in CORRECT_WORD:
            print(CORRECT_WORD[i:])
            if current_word[i].lower() == CORRECT_WORD[i]:
                print('green')
                temp_list.append(GREEN)
            elif current_word[i].lower() in CORRECT_WORD[i:]:
                print('yellow')
                temp_list.append(YELLOW)
            else:
                print('grey')
                temp_list.append(GREY)
        else:
            print('grey')
            temp_list.append(GREY)
    bg_colors.append(temp_list)
    guesses+=1
    current_word = ''
    print(words,bg_colors)


def create_word(key):
    global current_word
    current_word += key
    print(current_word)

def delete_letter():
    global current_word
    current_word = current_word[:-1]
    print(current_word)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_pressed = event.unicode.upper()
            if event.key == pygame.K_RETURN:
                if game_won != '':
                    reset()
                else:
                    if len(current_word) == 5 and current_word.lower() in WORDS:
                        print('entered')
                        check_words()
            elif event.key == pygame.K_BACKSPACE:
                if len(current_word) > 0:
                    delete_letter()
            if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                if len(current_word)<5:
                    create_word(key_pressed)
    # draw_words()