from phone_agenda import *
from time import sleep
from os import system as command_line

agenda = Phone_agenda()

Urgenta = 'Urgenta'
Urgenta = Person(Urgenta)
agenda.contacts.append(Urgenta)
Urgenta.fix.append('112')
Serv = 'Serviciu Client'
Serv = Person(Serv)
agenda.contacts.append(Serv)
Serv.fix.append('433')
Credit = 'Credit'
Credit = Person(Credit)
agenda.contacts.append(Credit)
Credit.fix.append('333')

while True:
    command_line('cls')
    agenda.main_menu()

    try:
        option = int(input('Your option: '))
        if option not in range(6):
            print('Input must be a number between 0 and 5!\n')
            sleep(2)
            continue
    except ValueError:
        print('Input must be a number!')
        sleep(2)
        command_line('cls')
        continue

    if option == 1:
        command_line('cls')
        add = input('Enter contact here : ')
        if add in [i for i in [c.return_name() for c in agenda.contacts]]:
            print('Contact already exist!')
            sleep(2)
            continue
        else:
            if not (add.replace(' ', '')).isalpha():
                print('A contact must contain only letters and spaces.')
                sleep(2)
                command_line('cls')
                continue

            nr_type = input('Number will be home(h)/fix(f)/mobile(m): ')
            if nr_type not in ['h', 'f', 'm']:
                print('Number type must be h, f or m!, not ', nr_type)
                sleep(2)
                command_line('cls')
                continue
            else:
                number = input('The number will be: ')
                if ' ' in number or \
                        (number.replace(' ', '')).isnumeric() is False:
                    print('Number must contain only digits!')
                    sleep(2)
                    command_line('cls')
                    continue

            add = Person(add)
            agenda.contacts.append(add)
            if nr_type is 'h':
                add.home_append(number)
                print('Contact added succesfully!')
                sleep(2)
            elif nr_type is 'f':
                add.fix_append(number)
                print('Contact added succesfully!')
                sleep(2)
            else:
                add.mobil_append(number)
                print('Contact added succesfully!')
                sleep(2)

    if option == 2:
        command_line('cls')
        if not agenda.find_contact():
            print('The contact does not exist.')
            sleep(2)
        else:
            a = input('Press Enter to return in main menu: ')
        continue

    if option == 3:
        command_line('cls')
        agenda.edit_contact()
        sleep(2)
        continue

    if option == 4:
        command_line('cls')
        if not agenda.delete_contact():
            print('The contact does not exist.')
        sleep(2)
        continue

    if option == 5:
        command_line('cls')
        agenda.show_agenda()
        a = input('Press Enter to return in main menu: ')
        continue

    if option == 0:
        command_line('cls')
        break
