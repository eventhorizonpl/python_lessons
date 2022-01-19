import pygame, pygame_menu, threading, time
from enum import auto, Enum
from pygame_menu.examples import create_example_window
from typing import Tuple, Any

class EducationalResource():
    price = 0
    title = ''
    skills = []

    def __init__(self, price: int, title: str, skills) -> None:
        self.price = price
        self.title = title
        self.skills = skills

class Book(EducationalResource):
    pass

class Course(EducationalResource):
    pass

class Bookstore():
    books = []

    def __init__(self) -> None:
        self.books.append(Book(120, 'Linux basics', [Skill(32, 1, SkillType.OS_LINUX)]))
        self.books.append(Book(300, 'Mac basics', [Skill(16, 1, SkillType.OS_MAC)]))
        self.books.append(Book(80, 'Windows basics', [Skill(16, 1, SkillType.OS_WINDOWS)]))
        self.books.append(Book(150, 'Linux intermediate topics', [Skill(40, 2, SkillType.OS_LINUX)]))
        self.books.append(Book(375, 'Mac intermediate topics', [Skill(20, 2, SkillType.OS_MAC)]))
        self.books.append(Book(100, 'Windows intermediate topics', [Skill(20, 2, SkillType.OS_WINDOWS)]))
        self.books.append(Book(240, 'Linux advanced', [Skill(64, 5, SkillType.OS_LINUX)]))
        self.books.append(Book(600, 'Mac advanced', [Skill(32, 5, SkillType.OS_MAC)]))
        self.books.append(Book(160, 'Windows advanced', [Skill(32, 5, SkillType.OS_WINDOWS)]))

class OnlineCourses():
    courses = []

    def __init__(self) -> None:
        self.courses.append(Course(99, 'Linux basics', [Skill(40, 1, SkillType.OS_LINUX)]))
        self.courses.append(Course(199, 'Mac basics', [Skill(20, 1, SkillType.OS_MAC)]))
        self.courses.append(Course(49, 'Windows basics', [Skill(20, 1, SkillType.OS_WINDOWS)]))
        self.courses.append(Course(199, 'Linux intermediate topics', [Skill(60, 2, SkillType.OS_LINUX)]))
        self.courses.append(Course(299, 'Mac intermediate topics', [Skill(30, 2, SkillType.OS_MAC)]))
        self.courses.append(Course(149, 'Windows intermediate topics', [Skill(30, 2, SkillType.OS_WINDOWS)]))
        self.courses.append(Course(299, 'Linux advanced', [Skill(100, 5, SkillType.OS_LINUX)]))
        self.courses.append(Course(399, 'Mac advanced', [Skill(60, 5, SkillType.OS_MAC)]))
        self.courses.append(Course(199, 'Windows advanced', [Skill(60, 5, SkillType.OS_WINDOWS)]))

class SchoolCourses():
    courses = []

    def __init__(self) -> None:
        self.courses.append(Course(50, 'Linux basics', [Skill(120, 1, SkillType.OS_LINUX)]))
        self.courses.append(Course(75, 'Mac basics', [Skill(120, 1, SkillType.OS_MAC)]))
        self.courses.append(Course(30, 'Windows basics', [Skill(120, 1, SkillType.OS_WINDOWS)]))
        self.courses.append(Course(55, 'Linux intermediate topics', [Skill(240, 2, SkillType.OS_LINUX)]))
        self.courses.append(Course(80, 'Mac intermediate topics', [Skill(240, 2, SkillType.OS_MAC)]))
        self.courses.append(Course(35, 'Windows intermediate topics', [Skill(240, 2, SkillType.OS_WINDOWS)]))
        self.courses.append(Course(60, 'Linux advanced', [Skill(360, 5, SkillType.OS_LINUX)]))
        self.courses.append(Course(85, 'Mac advanced', [Skill(360, 5, SkillType.OS_MAC)]))
        self.courses.append(Course(40, 'Windows advanced', [Skill(360, 5, SkillType.OS_WINDOWS)]))

class Player():
    age = 18
    money = 1000
    name = ''
    skills = []

    def __init__(self, name: str) -> None:
        self.name = name

class SkillType(Enum):
    OS_LINUX = auto()
    OS_MAC = auto()
    OS_WINDOWS = auto()

class Skill():
    hours = 0
    level = 0
    type = ''

    def __init__(self, hours: int, level: int, type: SkillType) -> None:
        self.hours = hours
        self.level = level
        self.type = type

class Game():
    bookstore = None
    online_courses = None
    player = None
    school_courses = None
    surface = None
    theme = None
    title = 'Freelancers life'

    def __init__(self) -> None:
        self.bookstore = Bookstore()
        self.online_courses = OnlineCourses()
        self.school_courses = SchoolCourses()
        self.surface = create_example_window(self.title, (800, 600))
        self.theme = pygame_menu.themes.THEME_BLUE.copy()
        self.theme.widget_font_size = 20

    def add_player_skills(self, skills) -> None:
        for skill in skills:
            skill_found = False
            for player_skill in self.player.skills:
                if player_skill.type == skill.type:
                    skill_found = True
                    player_skill.hours += skill.hours
                    if player_skill.level < skill.level:
                        player_skill.level = skill.level
            if not skill_found:
                self.player.skills.append(skill)

    def buy_and_read_book(self, book: Book) -> None:
        if book.price <= self.player.money:
            self.player.money -= book.price
            self.add_player_skills(book.skills)
            self.bookstore.books.remove(book)
            hours = 0
            for skill in book.skills:
                hours += skill.hours
            self.progress_screen(hours)

    def buy_book_menu(self) -> None:
        menu = self.get_menu()
        for book in self.bookstore.books:
            menu.add.button(str(book.title + ' (' + str(book.price) + ')'), self.buy_and_read_book, book)
        menu.add.button('Back', self.game_menu)
        menu.mainloop(self.surface)

    def game_menu(self) -> None:
        menu = self.get_menu()
        player_info = menu.add.table('table', background_color=(228, 230, 246))
        player_info.add_row(['Name:', self.player.name, 'Age:', str(self.player.age), 'Money:', str(self.player.money), 'Skills:', str(len(self.player.skills))], row_background_color=(228, 230, 246), cell_align=pygame_menu.locals.ALIGN_CENTER, cell_padding=[10, 10, 10, 10])
        menu.add.button('Learn', self.learn_menu)
        menu.add.button('Skills/practice', self.skills_menu)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.surface)

    def practice_skill(self, skill: Skill):
        pass

    def skills_menu(self) -> None:
        menu = self.get_menu('Skills/practice')
        for skill in self.player.skills:
            menu.add.button(str(skill.type.name + ' - Level: ' + str(skill.level) + ' Hours: ' + str(skill.hours)), self.practice_skill, skill)
        menu.add.button('Back', self.game_menu)
        menu.mainloop(self.surface)

    def get_menu(self, title: str = ''):
        if title == '':
            title = self.title

        theme_bg_image = self.theme.copy()
        theme_bg_image.background_color = pygame_menu.BaseImage(
            image_path='room.png'
        )
        menu = pygame_menu.Menu(
            height=600,
            theme=theme_bg_image,
            title=title,
            width=800
        )

        return menu

    def learn_menu(self) -> None:
        menu = self.get_menu()
        menu.add.button('Buy book', self.buy_book_menu)
        menu.add.button('Back', self.game_menu)
        menu.mainloop(self.surface)

    def new_game(self) -> None:
        menu = self.get_menu('New game')
        menu.add.text_input('Name: ', default='Michal', maxchar=10, textinput_id='name')
        menu.add.button('Start', self.start_game, menu)
        menu.add.button('Back', self.main_menu)
        menu.mainloop(self.surface)

    def main_menu(self) -> None:
        menu = self.get_menu()
        menu.add.button('New game', self.new_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.surface)

    def progress_screen(self, hours: int) -> None:
        menu = self.get_menu()
        progress_bar = menu.add.progress_bar('Learning')
        button = menu.add.button('Done', self.game_menu)
        button.hide()
        progress_thread = threading.Thread(target=self.progress_screen_motion, name="Progress", args=[button, hours, progress_bar])
        progress_thread.start()
        menu.mainloop(self.surface)

    def progress_screen_motion(self, button: pygame_menu.widgets.Button, hours: int, progress_bar: pygame_menu.widgets.ProgressBar) -> None:
        n = int(100 / hours)
        for i in range(0, 110, n):
            if i <= 100:
                progress_bar.set_value(i)
            else:
                progress_bar.set_value(100)
            time.sleep(1)
            if i >= 100:
                button.show()

    def run(self) -> None:
        self.main_menu()

    def start_game(self, menu: pygame_menu.Menu) -> None:
        input_data = menu.get_input_data()
        self.player = Player(input_data['name'])
        self.game_menu()

if __name__ == '__main__':
    game = Game()
    game.run()
