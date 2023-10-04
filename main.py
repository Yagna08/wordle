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

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75

pygame.font.init()
GUESSED_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 25)


pygame.display.set_caption("Wordle!")

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

current_word = ''
game_won = ''
words = []
bg_colors = []
current_letter_bg_x = 110
guesses = 0


def reset():
    print('reset')

def check_words():
    global current_word,guesses,CORRECT_WORD,current_letter_bg_x
    temp_list = []
    words.append(current_word)
    for i in range(len(current_word)):
        print(guesses,current_word[i],CORRECT_WORD[i])
        if current_word[i].lower() in CORRECT_WORD:
            print(CORRECT_WORD[i:])
            if current_word[i].lower() == CORRECT_WORD[i]:
                print('green')
                temp_list.append(GREEN)
            # elif current_word[i].lower() in CORRECT_WORD[i:]:
            else:
                print('yellow')
                temp_list.append(YELLOW)
            # else:
            #     print('grey')
            #     temp_list.append(GREY)
        else:
            print('grey')
            temp_list.append(GREY)
    bg_colors.append(temp_list)
    for colors in bg_colors:
        current_letter_bg_x = 110
        for i,j in zip(colors,words[guesses]):
            pygame.draw.rect(SCREEN, i, (current_letter_bg_x, guesses*100+LETTER_Y_SPACING, LETTER_SIZE, LETTER_SIZE))
            text = GUESSED_LETTER_FONT.render(j, True, pygame.Color('black'))
            SCREEN.blit(text,(current_letter_bg_x+15, guesses*100+LETTER_Y_SPACING))
            current_letter_bg_x += LETTER_X_SPACING
    guesses+=1
    current_word = ''
    print(words,bg_colors)


def create_word(key):
    global current_word,LETTER_X_SPACING,current_letter_bg_x,LETTER_SIZE
    current_word += key
    current_letter_bg_x = 110
    for i in current_word:
        pygame.draw.rect(SCREEN, (255,255,255), (current_letter_bg_x, guesses*100+LETTER_Y_SPACING, LETTER_SIZE, LETTER_SIZE))
        pygame.draw.rect(SCREEN, GREY, (current_letter_bg_x, guesses*100+LETTER_Y_SPACING, LETTER_SIZE, LETTER_SIZE),3)
        text = GUESSED_LETTER_FONT.render(i, True, pygame.Color('black'))
        SCREEN.blit(text,(current_letter_bg_x+15, guesses*100+LETTER_Y_SPACING))
        current_letter_bg_x += LETTER_X_SPACING
    print(current_word)

def delete_letter():
    global current_word,LETTER_X_SPACING,current_letter_bg_x
    current_letter_bg_x -= LETTER_X_SPACING
    pygame.draw.rect(SCREEN, (255,255,255), (current_letter_bg_x+1, guesses*100+LETTER_Y_SPACING+1, LETTER_SIZE-3, LETTER_SIZE-3))
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
    pygame.display.update()
    # draw_words()