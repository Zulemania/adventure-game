import time
import random


grand_villians = ["dragon", "evil clown", "troll", "witch"]
villian = random.choice(grand_villians)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def field():
    print_pause("You find yourself standing in an open field "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that one {villian} "
                " lives somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your left is a cave.")
    print_pause("In your hand, you hold a silly little dagger")


def house(items):
    print_pause("you approach the door of the house")
    print_pause("you are about to knock when the door opens,")
    print_pause(f"and out steps the {villian} !")
    print_pause(f"it is the {villian} house!")
    action = input("would you like to (1) Fight or (2) Runaway?")
    if action == '1':
        if "sword" in items:
            print_pause(f"As the {villian} moves to attack,")
            print_pause("you unsheath your new sword.")
            print_pause("The sword of ogoroth shines brightly in your hand"
                        "as you brace yourself to attack")
            print_pause(f"But the {villian} takes one look at"
                        "the sword and runs away.")
            print_pause(f"you have rid the town of the {villian}")
            print_pause("You are victorious!!")
            print_pause("GAME OVER!")
            play_again(items)
        else:
            print_pause("you do your best...")
            print_pause(f"but your dagger is no match for the {villian}")
            print_pause("The dragon attacks you")
            print_pause("You have been defeated")
            print_pause("GAME OVER")
            play_again(items)
    elif action == '2':
        print_pause("you run back to the field")
        print_pause("Luckily, you don't seem to be followed.")
        game_moves(items)
    else:
        print_pause("Invalid input")
        house(items)


def cave(items):
    print_pause("you peer cautiously into the cave")
    print_pause("it turns out to be only avery small cave")
    print_pause("your eye catches a glint of metal behind a rock")
    print_pause("you have found the magical sword of Ogoroth!")
    print_pause("you discard you silly little dagger and take the sword")
    print_pause("you walk back out to the field")
    items.append("sword")
    game_moves(items)


def game_moves(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    move = input("please enter 1 or 2.")
    if move == '1':
        house(items)
    elif move == '2':
        cave(items)
    else:
        game_moves(items)


def play_again(items):
    response = input("Would you like to play again? "
                     "Please say 'yes' or 'no'.\n").lower()
    if "no" == response:
        print_pause("Thanks for playing, see you next time.")
        exit()
    elif "yes" == response:
        print_pause("Excellent! Restarting the game...")
        play_game()


def play_game():
    items = []
    field()
    game_moves(items)
    play_again(items)


play_game()
