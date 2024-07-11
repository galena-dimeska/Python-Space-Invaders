import pygame, sys, random
from game import Game
from button import Button

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50
GREY = (29, 29, 27)
YELLOW = (243, 216, 63)

font = pygame.font.Font("Font/monogram.ttf", 40)
level_surface = font.render("LEVEL 01", False, YELLOW)
game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
high_score_text_surface = font.render("HIGH SCORE", False, YELLOW)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))
pygame.display.set_caption("Python Space Invaders")

background = pygame.image.load("Graphics/menu_background.png").convert()

dummy_button = Button("Graphics/start_button.png", (0, 0), 0.60)

BUTTON_HEIGHT = dummy_button.image.get_height()
BUTTON_WIDTH = dummy_button.image.get_width()

start_button = Button("Graphics/start_button.png", (SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2 +20, 315), 0.60)
exit_button = Button("Graphics/exit_button.png", (SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2 +20, 400), 0.60)
retry_button = Button("Graphics/retry_button.png", (SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2 +20, 315), 0.60)

def draw_main_menu():
    screen.fill(GREY)
    screen.blit(background, (0, 0))
    start_button.draw(screen)
    exit_button.draw(screen)

def play():
    screen.fill(GREY)
    pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)
    screen.blit(level_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 45, 50, 50))

    screen.blit(high_score_text_surface, (600, 15, 50, 50))
    formatted_high_score = str(game.high_score).zfill(5)
    high_score_surface = font.render(formatted_high_score, False, YELLOW)
    screen.blit(high_score_surface, (675, 45, 50, 50))

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)


main_menu = True #main menu is True so we can go to the main menu at the start of the game
clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

#we need a timed userevent for the lasers shot by the aliens, otherwise there will be a flood of lasers
SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

#timed event for the mystery ship to spawn at random time intervals
MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

    if main_menu:
        draw_main_menu()
        if start_button.is_pressed():
            print("Start button pressed")  # Debugging print
            main_menu = False
            game.run = True
        elif exit_button.is_pressed():
            pygame.quit()
            sys.exit()
    else:
        if game.run:
            game.spaceship_group.update()
            game.move_aliens()
            game.alien_lasers_group.update()
            game.mystery_ship_group.update()
            game.check_for_collisions()
            play()
        else:
            retry_button.draw(screen)
            exit_button.draw(screen)
            if retry_button.is_pressed():
                game.reset()
            if exit_button.is_pressed():
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)
