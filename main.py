import time
import random
import inquirer


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)


def intro():
    print_pause("\nYou are training to be a powerful warrior.\n")
    print_pause("There are many paths open to you in your journey.\n\n")


def first_choice():
    question = inquirer.List('ability',
                             message='What do you want to specialize in:\n',
                             choices=['Magic', 'Strength'])
    input = inquirer.prompt([question])
    choice = input['ability']
    if choice == 'Magic':
        print_pause("\nYou have decided to train to become a "
                    "powerful mage.\n"
                    "You will travel north to train at the magic academy.")

    else:
        print_pause("\nYou have decided to train to become a "
                    "powerful fighter.\n"
                    "You will travel south to learn with the pirates.\n\n")
    return choice


def play_game():
    intro()
    your_choice = first_choice()


if __name__ == '__main__':
    print('running')

    play_game()
