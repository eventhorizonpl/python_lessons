class Model():
    birth_date = ''
    first_name = ''
    last_name = ''

    def __init__(self, birth_date, first_name, last_name):
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name

class View():
    def get_data(self):
        print('Give your first name:')
        first_name = input()
        print('Give your last name:')
        last_name = input()
        print('Give your birth date:')
        birth_date = input()

        model = Model(birth_date, first_name, last_name)

        return model

    def show_data(self, model):
        print('Your name is', model.first_name, model.last_name, 'and your birth date is', model.birth_date)

class Controller():
    view = None

    def __init__(self):
        self.view = View()

    def run(self):
        model = self.view.get_data()
        self.view.show_data(model)

    def run2(self):
        model = Model('birth date', 'first name', 'last name')
        self.view.show_data(model)

if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.run2()
