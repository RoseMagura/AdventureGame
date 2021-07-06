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


def field():
    print_pause('\nYou step out of your house and start on the path '
                'towards the field.\n')
    print_pause("It's a beautiful spring day and the birds are singing.\n\n")


def monster_encounter():
    monsters = ['giant rat', 'poison moth', 'dragon', 'mummy']
    enemy = random.choice(monsters)
    print_pause("Suddenly, you hear a loud noise and "
                "sense a hostile presence.")
    print_pause("A " + enemy + " has appeared!\n")
    return enemy


def magic_attack(enemy_HP, enemy):
    colors = ['pink', 'red', 'blue', 'green', 'black']
    damage = random.randint(0, 100)
    print_pause("You focus your pyschic energy and shoot out an orb of " +
                random.choice(colors) + ' sparks.\nIt collides with the '
                + enemy + " and does " + str(damage) + " damage.")
    enemy_HP = enemy_HP - damage
    print_pause("The " + enemy + " has " + str(enemy_HP) + " health left!")
    return enemy_HP


def strength_attack(enemy_HP, enemy):
    damage = random.randint(0, 100)
    print_pause("You jump forward and attack the " + enemy +
                " with your sword."
                "\nIt does " + str(damage) + " damage.")
    enemy_HP = enemy_HP - damage
    print_pause("The " + enemy + " has " + str(enemy_HP) + " health left!")
    return enemy_HP


def monster_attack(enemy):
    damage = random.randint(0, 50)
    print_pause("The " + enemy + " rushes forward and attacks you!\n"
                "It does " + str(damage) + " damage")
    player_HP = 100
    player_HP = player_HP - damage
    print_pause("You now have " + str(player_HP) + " health left.")
    return player_HP


def heal(player_HP, choice):
    player_HP = player_HP + 50
    if choice == 'Magic':
        print_pause("You use white magic to heal 50 health!")
    else:
        print_pause("You use some healing salve to heal 50 health!")


def action(choice, enemy_HP, enemy, player_HP):
    question = inquirer.List('action',
                             message='Do you want to attack or heal?\n',
                             choices=['Attack', 'Heal'])
    input = inquirer.prompt([question])
    next_move = input['action']
    if next_move == 'Attack':
        if choice == 'Magic':
            enemy_HP = magic_attack(enemy_HP, enemy)
        else:
            enemy_HP = strength_attack(enemy_HP, enemy)
    else:
        heal(player_HP, choice)
    return enemy_HP, player_HP


def fight(choice, enemy):
    player_HP = 100
    enemy_HP = 100
    while player_HP > 0:
        player_HP = monster_attack(enemy)
        if player_HP > 0:
            result = action(choice, enemy_HP, enemy, player_HP)
            enemy_HP, player_HP = result
            if enemy_HP <= 0:
                print_pause("You successfully defeated the " + enemy + "!\n"
                            "Now you can continue on your journey. "
                            "YOU WON (for now)")
                answer = play_again()
                return answer
        else:
            print_pause("You were defeated. GAME OVER")


def play_game():
    playing = True
    while playing:
        intro()
        your_choice = first_choice()
        field()
        enemy = monster_encounter()
        playing = fight(your_choice, enemy)
    print_pause('Thanks so much for playing my game. See you again next time!')


def play_again():
    confirm = {
        inquirer.Confirm('answer',
                         message='Do you want to play again?')}
    confirmation = inquirer.prompt(confirm)
    return confirmation['answer']


if __name__ == '__main__':
    play_game()
