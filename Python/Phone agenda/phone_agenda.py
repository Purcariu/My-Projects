from person import *
from os import system as command_line


class Phone_agenda(Person):
    '''This is the agenda class.'''

    def __init__(self):
        self.contacts = []

    def main_menu(self):
        print('*' * 15 + ' MENU ' + '*' * 15)
        print('1 - Add contact')
        print('2 - Find contact')
        print('3 - Edit contact')
        print('4 - Delete contact')
        print('5 - Show agenda')
        print('0 - Exit')
        print('*' * 36)

    def find_contact(self):
        contacts_list = \
            [i for i in [c.return_name() for c in self.contacts]]
        index = 0
        find = input('Enter contact name: ')
        command_line('cls')
        for person in contacts_list:
            if person == find:
                print('----> {}: '.format(self.contacts[index].return_name()))
                print(self.contacts[index].show_numbers())
                return 1
            index += 1

    def edit_contact(self):
        contact_object = None
        contacts_list = \
            [i for i in [c.return_name() for c in self.contacts]]
        index = 0
        contact = input('Enter contact name: ')
        command_line('cls')
        for person in contacts_list:
            if person == contact:
                contact_object = self.contacts[index]

            index += 1
        if contact_object is None:
            print('The contact does not exist!')
        else:
            print("Enter 'n' for change name")
            print("'nmb' for change number")
            print("'a' for add number")
            print("and 'd' for delete number: ")
            question = input()
            if question not in ['n', 'nmb', 'a', 'd']:
                print('Wrong input!')
            else:
                command_line('cls')
                if question is 'n':
                    name = input('Enter new name: ')
                    contact_object.change_name(name)
                if question == 'nmb':
                    old_number = input('Enter old number: ')
                    if old_number in contact_object.mobil:
                        new_number = input('Enter new number: ')
                        if new_number not in contact_object.mobil:
                            contact_object.mobil.remove(old_number)
                            contact_object.mobil.append(new_number)
                        else:
                            print('The new number already exist!')
                    elif old_number in contact_object.fix:
                        new_number = input('Enter new number: ')
                        if new_number not in contact_object.fix:
                            contact_object.fix.remove(old_number)
                            contact_object.fix.append(new_number)
                        else:
                            print('The new number already exist!')
                    elif old_number in contact_object.home:
                        new_number = input('Enter new number: ')
                        if new_number not in contact_object.home:
                            contact_object.home.remove(old_number)
                            contact_object.home.append(new_number)
                        else:
                            print('The new number already exist!')
                    else:
                        print('The number does not exist.')
                if question is 'a':
                    nr_type = input('Number will be home(h)/fix(f)/mobile(m):')
                    if nr_type not in ['h', 'f', 'm']:
                        print('Number type must be h, f or m!, not ', nr_type)
                    else:
                        if nr_type is 'h':
                            number = input('The number will be: ')
                            if number not in contact_object.home:
                                contact_object.home_append(number)
                            else:
                                print('Number already exist!')
                        if nr_type is 'f':
                            number = input('The number will be: ')
                            if number not in contact_object.fix:
                                contact_object.fix_append(number)
                            else:
                                print('Number already exist!')
                        if nr_type is 'm':
                            number = input('The number will be: ')
                            if number not in contact_object.mobil:
                                contact_object.mobil_append(number)
                            else:
                                print('The number already exist!')
                if question is 'd':
                    number = input('Enter the number: ')
                    contact_object.delete_number(number)

    def delete_contact(self):
        contacts_list = \
            [i for i in [c.return_name() for c in self.contacts]]
        contact = input('Enter the contact: ')
        index = 0
        for c in contacts_list:
            if c == contact:
                del self.contacts[index]
                return 1
            index += 1

    def show_agenda(self):
        if len(self.contacts) == 0:
            print("You don't have any contacts")
        else:
            iteration = 0
            for c in self.contacts:
                iteration += 1
                print('----> {}: '.format(c.return_name()))
                c.show_numbers()
                print('*' * 15)
                if not iteration % 5:
                    input('Press Enter to show the next contacts: ')
                    command_line('cls')
