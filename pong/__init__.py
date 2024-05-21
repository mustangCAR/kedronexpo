import pygame
from .enigma import *
import sys
from os import path as p
def main():
    pygame.init()
    screen = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Smiley Pong!!!")
    keep_going = True
    pic = pygame.image.load(p.join(p.dirname(__file__), "face.png"))
    picx = 0
    picy = 0
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    timer = pygame.time.Clock()
    speedx = 5
    speedy = 5
    PADDLEW = 200
    PADDLEH = 25
    paddlex = 300
    paddley = 550
    PICW = 100
    PICH = 95
    points = 0
    lives = 5
    font = pygame.font.SysFont("Times", 24)
    mystery = enigma()
    try:
        file = open(p.join(p.dirname(__file__), "HI.txt"),"r")
        hi = mystery.decrypt(file.read())
        filew = open(p.join(p.dirname(__file__), "HI.txt"),"w")
    except FileNotFoundError:
        filew = open(p.join(p.dirname(__file__), "HI.txt"),"w")
        hi = 0
    while keep_going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    points = 0
                    lives = 5
                    picx = 0
                    picy = 0
                    speedx = 5
                    speedy = 5
        picx += speedx
        picy += speedy
        if picx <= 0 or picx + PICW >= 800:
            speedx = -speedx * 1.1
        if picy <= 0:
            speedy = -speedy + 1
        if picy >= 500:
            lives -= 1
            speedy = -speedy
            speedy = -5
            speedx = 5
            picy = 499
        screen.fill(BLACK)
        screen.blit(pic, (picx,picy))
        paddlex = pygame.mouse.get_pos()[0]
        paddlex -= PADDLEW/2
        pygame.draw.rect(screen, WHITE, (paddlex, paddley, PADDLEW, PADDLEH))
        if picy + PICH >= paddley and picy + PICH <= paddley + PADDLEH and speedy > 0 :
            if picx + PICW / 2 >= paddlex and picx + PICW / 2 <= paddlex + PADDLEW:
                points += 1
                speedy = -speedy
        if int(points) >= int(hi):
            hi = points
        draw_string = "Lives: " + str(lives) + " Points: " + str(points) + " HI: " + str(hi)
        if lives < 1:
            speedx = speedy = 0
            draw_string = "Game Over. Your score was: " + str(points) + ". Press\"SPACEBAR\" to play again"
            screen.fill(BLACK)
        text = font.render(draw_string, True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 10
        screen.blit(text, text_rect)
        pygame.display.update()
        timer.tick(60)
    filew.write(mystery.encrypt(str(hi)))
    filew.close()
    pygame.quit()
    sys.exit()
