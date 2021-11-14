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
        self.birth_date = date.fromisoformat(birth_date)
        self.first_name = first_name
        self.last_name = last_name

class Benefactor(Person):
    kyc_pass = False

class Beneficiary(Person):
    high_risk = False

class Bank():
    benefactors = []
    beneficiaries = []
    name = ''

    def __init__(self, name):
        self.name = name

    def list_actions(self):
        print('Welcome to', self.name)
        print('1 - List/create benefactors')
        print('2 - List/create beneficiaries')
        try:
            menu_option = int(input())

            if menu_option == 1:
                self.list_benefactors()
        except ValueError:
            print('Wrong option')

    def create_benefactor(self):
        print('=== Create benefactor ===')
        print('First name:')
        first_name = input()
        print('Last name:')
        last_name = input()
        print('Birth date:')
        birth_date = input()
        print('Street:')
        street = input()
        print('Post code:')
        post_code = input()
        print('City:')
        city = input()
        address = Address(city, post_code, street)
        benefactor = Benefactor(address, birth_date, first_name, last_name)
        self.benefactors.append(benefactor)
        self.list_benefactors()

    def list_benefactors(self):
        print('=== List benefactors ===')
        print('c - create, b - back')
        for benefactor in self.benefactors:
            print(benefactor.first_name, benefactor.last_name, '-', benefactor.address.street, ',', benefactor.address.post_code, ',', benefactor.address.city)
        try:
            menu_option = input()

            if menu_option == 'b':
                self.list_actions()
            elif menu_option == 'c':
                self.create_benefactor()
            else:
                self.list_benefactors()
        except ValueError:
            print('Wrong option')

    def run(self):
        while True:
            self.list_actions()

if __name__ == '__main__':
    bank = Bank('MyBank')
    bank.run()
