import pygame, pygame_menu
from pygame_menu.examples import create_example_window
from datetime import date

class Address():
    city = ''
    post_code = ''
    street = ''

    def __init__(self, city: str, post_code: str, street: str):
        self.city = city
        self.post_code = post_code
        self.street = street

class Person():
    address = None
    birth_date = ''
    first_name = ''
    last_name = ''

    def __init__(self, address: Address, birth_date: str, first_name: str, last_name: str):
        self.address = address
        #self.birth_date = date.fromisoformat(birth_date)
        self.first_name = first_name
        self.last_name = last_name

class Benefactor(Person):
    kyc_pass = False

class Beneficiary(Person):
    high_risk = False

class BenefactorService():
    def create(self, first_name: str, last_name: str, birth_date: str, street: str, post_code: str, city: str):
        address = Address(city, post_code, street)
        benefactor = Benefactor(address, birth_date, first_name, last_name)

        return benefactor

class Bank():
    benefactor_service = BenefactorService()
    benefactors = []
    beneficiaries = []
    name = ''

    def __init__(self, name):
        self.name = name

class BankUi():
    bank = None
    surface = None

    def __init__(self):
        self.bank = Bank('MyBank')
        self.surface = create_example_window('Bank', (800, 600))

    def benefactors_create_action(self, first_name: str, last_name: str, birth_date: str, street: str, post_code: str, city: str) -> None:
        benefactor = self.bank.benefactor_service.create(first_name, last_name, birth_date, street, post_code, city)
        self.bank.benefactors.append(benefactor)
        self.benefactors_list_view()

    def benefactors_create_view(self) -> None:
        menu = pygame_menu.Menu(
            height=600,
            theme=pygame_menu.themes.THEME_SOLARIZED,
            title='Create benefactor',
            width=800
        )
        first_name = menu.add.text_input('First name: ', default='')
        last_name = menu.add.text_input('Last name: ', default='')
        birth_date = menu.add.text_input('Birth date: ', default='')
        street = menu.add.text_input('Street: ', default='')
        post_code = menu.add.text_input('Post code: ', default='')
        city = menu.add.text_input('City: ', default='')
        menu.add.button('Create', self.benefactors_create_action, first_name, last_name, birth_date, street, post_code, city)
        menu.add.button('Back to Benefactors', self.benefactors_list_view)
        menu.mainloop(self.surface)

    def benefactors_list_view(self) -> None:
        menu = pygame_menu.Menu(
            height=600,
            theme=pygame_menu.themes.THEME_SOLARIZED,
            title='Benefactors',
            width=800
        )
        menu.add.button('Create', self.benefactors_create_view)
        table = menu.add.table('table', background_color='white')
        row = table.add_row(['First name', 'Last name', 'Street', 'Post code', 'City'], row_background_color='white', cell_align=pygame_menu.locals.ALIGN_CENTER)
        for benefactor in self.bank.benefactors:
            row = table.add_row([benefactor.first_name, benefactor.last_name, benefactor.address.street, benefactor.address.post_code, benefactor.address.city], row_background_color='white', cell_align=pygame_menu.locals.ALIGN_CENTER)
        menu.add.button('Back to main menu', self.main_menu)
        menu.mainloop(self.surface)

    def main_menu(self) -> None:
        menu = pygame_menu.Menu(
            height=600,
            theme=pygame_menu.themes.THEME_SOLARIZED,
            title=str('Welcome to ' + self.bank.name),
            width=800
        )

        menu.add.button('Benefactors', self.benefactors_list_view)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.surface)

    def run(self) -> None:
        self.main_menu()

if __name__ == '__main__':
    bank_ui = BankUi()
    bank_ui.run()
