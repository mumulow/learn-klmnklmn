
import pygame
import time



pygame.init() #инициализация pygame#
screen = pygame.display.set_mode ((1000, 500)) #открытие окна#
pygame.display.set_caption('ВНИМАНИЕ')
font = pygame.font.SysFont('Segoe UI', 50)
label = font.render('У тебя вирус, бро!', 1, (12, 140, 0, 1))

while True:
     for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            time.sleep(0.001)
            screen = pygame.display.set_mode((1000, 500))  # открытие окна#
            pygame.display.set_caption('ВНИМАНИЕ')


     screen.fill ((0, 0, 0)) #цвет экрана#
     screen.blit (label, (50, 50)) #выведение на экран#
     pygame.display.update() #обновление экрана#