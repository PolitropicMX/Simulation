#ok banda hoy hare un vaso, un recipiente en python
import pygame, sys
import numpy as np
import math
from button import Button
from scroll_menu import Scrollmenu
# Initialize the pygame
pygame.init()

#Create the screen
HEIGHT, WIDTH = 600,700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pygame project")
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#Create the clock
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf',32)


# variables
segundero = 0
cur_vel_x = 0
cur_vel_y = 0
cur_x = 100
cur_y = 100

# Funciones de dibujo
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("f", size)
def dot(xi,yi,r):
    pygame.draw.circle(screen,(255,255,0),(xi,yi),r)
def line(xi,yi,xf,yf):
    pygame.draw.line(screen,(255,255,255),(xi,yi),(xf,yf),1)
def rect(xi,yi,w,h,blacktowhite):
    pygame.draw.rect(screen,(blacktowhite,blacktowhite,blacktowhite),(xi,yi,w,h))
def text(string,xi,yi):
    textsurface = font.render(string,False,(10,100,100))
    screen.blit(textsurface,(xi,yi))
def panel(xi,yi,string):
    w,h = 250,40
    pygame.draw.rect(screen,(25,25,255),(xi,yi,w,h))
    textsurface = font.render(string,False,(255,255,255))
    screen.blit(textsurface,(xi,yi))
def cursor(xi,yi):
    ri,re = 10,12
    pygame.draw.circle(screen,(0,0,0),(xi,yi),re)
    pygame.draw.circle(screen,(255,255,255),(xi,yi),ri)
def vaso(xi,yi,w,h,e):
    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
    pygame.draw.rect(screen,(0,0,0),(xi+e,yi,w-2*e,h-e))

scrollmenu = Scrollmenu(screen,210)

#### INICIALIZADORES ####
clicked = False
#### THE IMPORTANT STUFF OF DRAG AND DROP
class Key(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,size,image,id):
        super(Key, self).__init__()
        self.image = pygame.image.load('images/'+image).convert()
        self.image = pygame.transform.scale(self.image,(size,size))
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos 
        self.rect.y = ypos
        self.id = id
        self.linkready = False
        self.links = []
####


####
while True:
    tiempo = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel_y = -10
            if event.key == pygame.K_a:
                cur_vel_x = -10
            if event.key == pygame.K_x:
                pass
            if event.key == pygame.K_d:
                cur_vel_x = 10
            if event.key == pygame.K_s:
                cur_vel_y = 10
            if event.key == pygame.K_n:
                pass
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel_y = 0
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                cur_vel_x = 0
            if event.key == pygame.K_s:
                cur_vel_y = 0
            if event.key == pygame.K_d:
                cur_vel_x = 0
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if event.button == 1:
                scrollmenu.controlspressed(pos)
            elif event.button == 2:
                scrollmenu.for_button_2(pos)

        if event.type == pygame.MOUSEBUTTONUP:
            scrollmenu.controlsreleased(pos)
    screen.fill((0,0,0))
    # A partir de aqui dibujas
    #print(segundero)
    pos = pygame.mouse.get_pos()

    scrollmenu.update(pos)

    



    #cursor
    cur_x += cur_vel_x
    cur_y += cur_vel_y

    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)
