import pygame, pygame_menu
from pygame_menu.examples import create_example_window
from typing import Tuple, Any

class Game():
    surface = None

    def __init__(self):
        self.surface = create_example_window('Example - Simple', (800, 600))

    def set_difficulty(self, selected: Tuple, value: Any) -> None:
        print(f'Set difficulty to {selected[0]} ({value})')

    def button_test(self) -> None:
        menu = pygame_menu.Menu(
            height=600,
            theme=pygame_menu.themes.THEME_GREEN,
            title='Button test',
            width=800
        )
        menu.add.button('Back to main menu', self.main_menu)
        menu.mainloop(self.surface)

    def text_input_test(self) -> None:
        menu = pygame_menu.Menu(
            height=600,
            theme=pygame_menu.themes.THEME_DARK,
            title='Text input test',
            width=800
        )
        test = menu.add.text_input('Name: ', default='Test', maxchar=10)
        menu.add.button('Back to main menu', self.main_menu)
        menu.mainloop(self.surface)

    def selector_test(self) -> None:
        menu = pygame_menu.Menu(
            height=600,
            theme=pygame_menu.themes.THEME_DEFAULT,
            title='Selector test',
            width=800
        )
        menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty)
        menu.add.button('Back to main menu', self.main_menu)
        menu.mainloop(self.surface)

    def main_menu(self) -> None:
        menu = pygame_menu.Menu(
            height=600,
            theme=pygame_menu.themes.THEME_BLUE,
            title='Welcome',
            width=800
        )

        menu.add.button('Button test', self.button_test)
        menu.add.button('Text input test', self.text_input_test)
        menu.add.button('Selector test', self.selector_test)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.surface)

    def run(self) -> None:
        self.main_menu()

if __name__ == '__main__':
    game = Game()
    game.run()
