import pygame
from words import WORDS 
import random
import sys

# pygame.init()

WIDTH, HEIGHT = 633, 800

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
indicator_x, indicator_y = 20, 590
green,yellow,grey = [],[],[]


def reset():
    global guesses,CORRECT_WORD,current_word,game_won,words,bg_colors,current_letter_bg_x,indicator_x,indicator_y,green,grey,yellow
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses = 0
    CORRECT_WORD = random.choice(WORDS)
    print(CORRECT_WORD)
    current_word = ''
    game_won = ''
    words = []
    bg_colors = []
    current_letter_bg_x = 110
    indicator_x, indicator_y = 20, 590
    green,yellow,grey = [],[],[]
    indicators()
    # print('reset')

def check_words():
    global current_word,guesses,CORRECT_WORD,current_letter_bg_x,game_won,grey,green,yellow
    temp_list = []
    if current_word.lower() == CORRECT_WORD:
        game_won = "W"
    if guesses == 5 and game_won == "":
        game_won = "L"
    
    words.append(current_word)
    for i in range(len(current_word)):
        # print(guesses,current_word[i],CORRECT_WORD[i])
        if current_word[i].lower() in CORRECT_WORD:
            # print(CORRECT_WORD[i:])
            if current_word[i].lower() == CORRECT_WORD[i]:
                # print('green')
                green.append(current_word[i].lower())
                temp_list.append(GREEN)
            # elif current_word[i].lower() in CORRECT_WORD[i:]:
            else:
                # print('yellow')
                yellow.append(current_word[i].lower())

                temp_list.append(YELLOW)
            # else:
            #     print('grey')
            #     temp_list.append(GREY)
        else:
            # print('grey')
            grey.append(current_word[i].lower())

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
    # print(words,bg_colors)
    # print(green,yellow,grey)
    # print(game_won)


def indicators():
    global grey,green,yellow,GREEN,YELLOW,GREY,game_won
    # print('indicators')
    indicator_x, indicator_y = 20, 590
    if game_won!='':
        pygame.draw.rect(SCREEN, "white", (10, 590, 1000, 600))
        play_again_font = pygame.font.Font("FreeSansBold.otf", 40)
        play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
        play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
        word_was_text = play_again_font.render(f"The word was {CORRECT_WORD}!", True, "black")
        word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 650))
        SCREEN.blit(word_was_text, word_was_rect)
        SCREEN.blit(play_again_text, play_again_rect)
    else:
        for i in range(3):
            for letter in ALPHABET[i]:
                if letter.lower() in green:
                    pygame.draw.rect(SCREEN, GREEN, (indicator_x, indicator_y, 57, 60))
                elif letter.lower() in yellow:
                    pygame.draw.rect(SCREEN, YELLOW, (indicator_x, indicator_y, 57, 60))
                elif letter.lower() in grey:
                    pygame.draw.rect(SCREEN, GREY, (indicator_x, indicator_y, 57, 60))
                else:
                    pygame.draw.rect(SCREEN, OUTLINE, (indicator_x, indicator_y, 57, 60))
                text_surface = AVAILABLE_LETTER_FONT.render(letter, True, "white")
                text_rect = text_surface.get_rect(center=(indicator_x+27, indicator_y+30))
                SCREEN.blit(text_surface, text_rect)
                indicator_x += 60
            indicator_y += 65
            if i == 0:
                indicator_x = 50
            elif i == 1:
                indicator_x = 105

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
    # print(current_word)

def delete_letter():
    global current_word,LETTER_X_SPACING,current_letter_bg_x
    current_letter_bg_x -= LETTER_X_SPACING
    pygame.draw.rect(SCREEN, (255,255,255), (current_letter_bg_x+1, guesses*100+LETTER_Y_SPACING+1, LETTER_SIZE-3, LETTER_SIZE-3))
    current_word = current_word[:-1]
    # print(current_word)

indicators()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game_won=='':
            key_pressed = event.unicode.upper()
            if event.key == pygame.K_RETURN:
                if len(current_word) == 5 and current_word.lower() in WORDS:
                    # print('entered')
                    check_words()
                    indicators()
            elif event.key == pygame.K_BACKSPACE:
                if len(current_word) > 0:
                    delete_letter()
            if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                if len(current_word)<5:
                    create_word(key_pressed)
        elif game_won!='' and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                reset()
    pygame.display.update()
    # draw_words()