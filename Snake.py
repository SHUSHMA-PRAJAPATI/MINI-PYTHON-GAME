import pygame
import random
import os

pygame.mixer.init()
pygame.mixer.music.load('snake_eater.mp3')
pygame.mixer.music.play()

pygame.init()

screen_width = 600
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")

pygame.display.update()
#background image

blue = (0,0,255)
yellow = (255,255,150)
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)


def welcome():
    exitgame = False
    while not exitgame:

        welcome = pygame.image.load("welcome.jpg")
        welcome = pygame.transform.scale(welcome, (screen_width, screen_height))
        gameWindow.blit(welcome, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()

def gameLoop():


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameLoop()
    bg = pygame.image.load("bg.jpg")
    bg = pygame.transform.scale(bg, (screen_width, screen_height))

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20,screen_width-20)
    food_y = random.randint(20,screen_height-20)
    snake_size = 10
    food_size = 10
    fps = 60
    init_velocity = 5
    score=0
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None,55)

    def text_screen(text , color , x , y):
        screen_text = font.render(text, True , color)
        gameWindow.blit(screen_text,[x,y])

    def plot_snake(gameWindow, color , snk_list , snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow , color , [x, y,snake_size , snake_size])

    snk_list = []
    snk_length = 1

    highscore = 0

    if (not os.path.exists("highScore.txt")):
        with open("highScore.txt","w") as f:
            f.write("0")

        with open("highScore.txt","r") as f:
            highscore = f.read()

    #Game Loop
    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            text_screen("       Game Over!  ",red , 50,200)
            text_screen("Press enter to continue",red , 50,300)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y =  init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score = score + 10
                    if snake_x>600 or snake_x<0 or snake_y>600 or snake_y<0:
                        game_over = True
            snake_x += velocity_x
            snake_y +=velocity_y


            if abs(snake_x-food_x)<6 and abs(snake_y - food_y)<6:
                score+=10
                food_x = random.randint(10, screen_width - 10)
                food_y = random.randint(10, screen_height - 10)
                snk_length +=5

            gameWindow.fill(yellow)
            gameWindow.blit(bg,(0, 0))
            pygame.draw.rect(gameWindow,blue, [0,0,600,50])
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

            text_screen("Score : " + str(score)+"    High Score : "+str(highscore), white, 10, 10)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
            plot_snake(gameWindow, black , snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()