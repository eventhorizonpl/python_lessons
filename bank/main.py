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

class Currency:
    code = ''
    name = ''

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

class Country:
    name = ''
    code = ''
    currency = None

    def __init__(self, name: str, code: str, currency: Currency):
        self.currency = currency
        self.name = name
        self.code = code

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
    def create(self, first_name: str, last_name: str, birth_date: str, street: str, post_code: str, city: str) -> Benefactor:
        address = Address(city, post_code, street)
        benefactor = Benefactor(address, birth_date, first_name, last_name)

        return benefactor

class BeneficiaryService():
    def create(self, first_name: str, last_name: str, birth_date: str, street: str, post_code: str, city: str) -> Beneficiary:
        address = Address(city, post_code, street)
        beneficiary = Beneficiary(address, birth_date, first_name, last_name)

        return beneficiary

class CurrencyService():
    def create(self, code: str, name: str) -> Currency:
        currency = Currency(code, name)

        return currency

class CountryService():
    def create(self, code: str, name: str, currency: Currency) -> Country:
        country = Country(name, code, currency)

        return country

class Bank():
    benefactor_service = BenefactorService()
    benefactors = []
    beneficiaries = []
    beneficiary_service = BeneficiaryService()
    country_service = CountryService()
    countries = []
    currencies = []
    currency_service = CurrencyService()
    name = ''

    def __init__(self, name):
        self.name = name

class BankUi():
    bank = None
    surface = None

    def __init__(self):
        self.bank = Bank('MyBank')
        self.surface = create_example_window('Bank', (1200, 600))

    def benefactors_create_action(self, menu: pygame_menu.Menu) -> None:
        input_data = menu.get_input_data()
        benefactor = self.bank.benefactor_service.create(input_data['first_name'], input_data['last_name'], input_data['birth_date'], input_data['street'], input_data['post_code'], input_data['city'])
        self.bank.benefactors.append(benefactor)
        self.benefactors_list_view()

    def benefactors_create_view(self) -> None:
        menu = self.get_menu('Create benefactor')
        menu.add.text_input('First name: ', default='', input_underline='_', textinput_id='first_name')
        menu.add.text_input('Last name: ', default='', input_underline='_', textinput_id='last_name')
        menu.add.text_input('Birth date: ', default='', input_underline='_', textinput_id='birth_date')
        menu.add.text_input('Street: ', default='', input_underline='_', textinput_id='street')
        menu.add.text_input('Post code: ', default='', input_underline='_', textinput_id='post_code')
        menu.add.text_input('City: ', default='', input_underline='_', textinput_id='city')
        menu.add.button('Create', self.benefactors_create_action, menu)
        menu.add.button('Back to Benefactors', self.benefactors_list_view)
        menu.mainloop(self.surface)

    def benefactors_list_view(self) -> None:
        menu = self.get_menu('Benefactors')
        menu.add.button('Create', self.benefactors_create_view)
        table = menu.add.table('table', background_color=(239, 231, 211))
        row = table.add_row(['First name', 'Last name', 'Street', 'Post code', 'City'], row_background_color=(239, 231, 211), cell_align=pygame_menu.locals.ALIGN_CENTER, cell_padding=[10, 10, 10, 10])
        for benefactor in self.bank.benefactors:
            row = table.add_row([benefactor.first_name, benefactor.last_name, benefactor.address.street, benefactor.address.post_code, benefactor.address.city], row_background_color=(239, 231, 211), cell_align=pygame_menu.locals.ALIGN_CENTER, cell_padding=[10, 10, 10, 10])
        menu.add.button('Back to main menu', self.main_menu)
        menu.mainloop(self.surface)

    def beneficiary_create_action(self, menu: pygame_menu.Menu) -> None:
        input_data = menu.get_input_data()
        beneficiary = self.bank.beneficiary_service.create(input_data['first_name'], input_data['last_name'], input_data['birth_date'], input_data['street'], input_data['post_code'], input_data['city'])
        self.bank.beneficiaries.append(beneficiary)
        self.beneficiaries_list_view()

    def beneficiaries_create_view(self) -> None:
        menu = self.get_menu('Create beneficiary')
        menu.add.text_input('First name: ', default='', input_underline='_', textinput_id='first_name')
        menu.add.text_input('Last name: ', default='', input_underline='_', textinput_id='last_name')
        menu.add.text_input('Birth date: ', default='', input_underline='_', textinput_id='birth_date')
        menu.add.text_input('Street: ', default='', input_underline='_', textinput_id='street')
        menu.add.text_input('Post code: ', default='', input_underline='_', textinput_id='post_code')
        menu.add.text_input('City: ', default='', input_underline='_', textinput_id='city')
        menu.add.button('Create', self.beneficiary_create_action, menu)
        menu.add.button('Back to Benefactors', self.beneficiaries_list_view)
        menu.mainloop(self.surface)

    def beneficiaries_list_view(self) -> None:
        menu = self.get_menu('Beneficiaries')
        menu.add.button('Create', self.beneficiaries_create_view)
        table = menu.add.table('table', background_color=(239, 231, 211))
        row = table.add_row(['First name', 'Last name', 'Street', 'Post code', 'City'], row_background_color=(239, 231, 211), cell_align=pygame_menu.locals.ALIGN_CENTER, cell_padding=[10, 10, 10, 10])
        for beneficiary in self.bank.beneficiaries:
            row = table.add_row([beneficiary.first_name, beneficiary.last_name, beneficiary.address.street, beneficiary.address.post_code, beneficiary.address.city], row_background_color=(239, 231, 211), cell_align=pygame_menu.locals.ALIGN_CENTER, cell_padding=[10, 10, 10, 10])
        menu.add.button('Back to main menu', self.main_menu)
        menu.mainloop(self.surface)

    def currency_create_action(self, menu: pygame_menu.Menu) -> None:
        input_data = menu.get_input_data()
        currency = self.bank.currency_service.create(input_data['code'], input_data['name'])
        self.bank.currencies.append(currency)
        self.currencies_list_view()

    def currencies_create_view(self) -> None:
        menu = self.get_menu('Create currency')
        menu.add.text_input('Code: ', default='', input_underline='_', textinput_id='code')
        menu.add.text_input('Name: ', default='', input_underline='_', textinput_id='name')
        menu.add.button('Create', self.currency_create_action, menu)
        menu.add.button('Back to Currencies', self.currencies_list_view)
        menu.mainloop(self.surface)

    def currencies_list_view(self) -> None:
        menu = self.get_menu('Currencies')
        menu.add.button('Create', self.currencies_create_view)
        table = menu.add.table('table', background_color=(239, 231, 211))
        row = table.add_row(['Code', 'Name'], row_background_color=(239, 231, 211), cell_align=pygame_menu.locals.ALIGN_CENTER, cell_padding=[10, 10, 10, 10])
        for currency in self.bank.currencies:
            row = table.add_row([currency.code, currency.name], row_background_color=(239, 231, 211), cell_align=pygame_menu.locals.ALIGN_CENTER, cell_padding=[10, 10, 10, 10])
        menu.add.button('Back to main menu', self.main_menu)
        menu.mainloop(self.surface)

    def get_menu(self, title: str) -> pygame_menu.Menu:
        menu = pygame_menu.Menu(
            height=600,
            theme=pygame_menu.themes.THEME_SOLARIZED,
            title=title,
            width=1200
        )

        return menu

    def main_menu(self) -> None:
        menu = self.get_menu(str('Welcome to ' + self.bank.name))
        menu.add.button('Benefactors', self.benefactors_list_view)
        menu.add.button('Beneficiary', self.beneficiaries_list_view)
        menu.add.button('Currency', self.currencies_list_view)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.surface)

    def run(self) -> None:
        self.main_menu()

if __name__ == '__main__':
    bank_ui = BankUi()
    bank_ui.run()
