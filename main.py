#Importing packages
import pygame
import math
import random

# Setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
BUTTON_FONT = pygame.font.SysFont('comicsans', 30)

# Load images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# Game variables
hangman_status = 0
words = ["VINUTHNA", "PALLAVI", "JYOTHSNA", "RENUSREE",
         "JAYANTHI", "DEVELOPER", "SOFTWARE", "TESTING",
         "GOOGLE", "RGUKT", "HELP", "ZERO", "CHILDREN"]
word = random.choice(words)
guessed = []
score=0

# Colors
WHITE = (115, 147, 179)
BLACK = (204, 204, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Drawing functions
def draw():
    win.fill(WHITE)
    # Draw title
    text = TITLE_FONT.render("HANGMAN GAME", 1, (255, 255, 255))
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "  # Separate each letter with a space
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, (0, 0, 0))
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message, color):
    
    pygame.init()  # Initialize Pygame
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, color)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    
    # Play Again button
    play_again_surf = BUTTON_FONT.render("Play Again", 1, (255, 255, 255))
    play_again_button = pygame.Rect(240, 350, 120, 30)
    pygame.draw.rect(win, (0, 0, 128), play_again_button)
    win.blit(play_again_surf, (play_again_button.x + 5, play_again_button.y + 5))
    
    # Quit button
    quit_surf = BUTTON_FONT.render("Quit", 1, (255, 255, 255))
    quit_button = pygame.Rect(440, 350, 120, 30)
    pygame.draw.rect(win, (0, 0, 128), quit_button)
    win.blit(quit_surf, (quit_button.x + 5, quit_button.y + 5))
    
    pygame.display.update()
    
    run = True
    while run:
        
        
        a,b=pygame.mouse.get_pos()
        if play_again_button.x<= a <= play_again_button.x+120 and play_again_button.y<= b <= play_again_button.y+30:
            pygame.draw.rect(win,(0,255,255),play_again_button)
        else:
            pygame.draw.rect(win, (0, 0, 128), play_again_button)
        win.blit(play_again_surf, (play_again_button.x + 5, play_again_button.y + 5))
            
            
        a,b=pygame.mouse.get_pos()
        if quit_button.x<= a <= quit_button.x+120 and quit_button.y<= b <= quit_button.y+30:
            pygame.draw.rect(win,(0,255,255),quit_button)
        else:
            pygame.draw.rect(win, (0, 0, 128), quit_button)
        win.blit(quit_surf, (quit_button.x+35, quit_button.y + 5))
        
        
        pygame.display.update()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    return True
                elif quit_button.collidepoint(event.pos):
                    run = False
                    pygame.quit()
    return False


# Setup game loop
def main():
    global hangman_status, word
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            if display_message("You WON!", GREEN):

                hangman_status = 0
                word = random.choice(words)
                guessed.clear()
                for letter in letters:
                    letter[3] = True
            else:
                run = False

        if hangman_status == 6:
            if display_message("You LOST!", RED):
                hangman_status = 0
                word = random.choice(words)
                guessed.clear()
                for letter in letters:
                    letter[3] = True
            else:
                run = False

    pygame.quit()

main()
