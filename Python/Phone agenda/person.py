class Contact:
    '''This is the superclass.'''

    def __init__(self, name):
        self.name = name

    def return_name(self):
        return(self.name)


class Person(Contact):
    ''' This class inherited from class Contact.'''

    def __init__(self, name):
        self.mobil = []
        self.fix = []
        self.home = []
        super(Person, self).__init__(name)

    def change_name(self, name):
        self.name = name

    def mobil_append(self, number):
        self.mobil.append(number)

    def fix_append(self, number):
        self.fix.append(number)

    def home_append(self, number):
        self.home.append(number)

    def change_number(self, number, replace):
        if number in self.mobil:
            self.mobil = \
                [replace if x == number else x for x in self.mobil]
        elif number in self.fix:
            self.fix = \
                [replace if x == number else x for x in self.fix]
        elif number in self.home:
            self.home = \
                [replace if x == number else x for x in self.home]

    def delete_number(self, number):
        if number in self.mobil:
            self.mobil.remove(number)
        elif number in self.fix:
            self.fix.remove(number)
        elif number in self.home:
            self.home.remove(number)
        else:
            print('Number does not exist.')

    def show_numbers(self):
        if len(self.mobil) != 0:
            print('Mobil: ')
            for n in self.mobil:
                print('->', n)
        if len(self.fix) != 0:
            print('Fix: ')
            for n in self.fix:
                print('->', n)
        if len(self.home) != 0:
            print('Home: ')
            for n in self.home:
                print('->', n)
