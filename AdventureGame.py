# Import modules and use functions from those modules
import time
import random


def play():
    weapon = ""
    monster = random.choice(["vampire", "werewolf", "dragon", "zombie"])
    intro(weapon, monster)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# Use a conditional loop to handle invalid input.
def validinput(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        elif response == "exit":
            break
        else:
            print_pause("Sorry, I don't understand. Can you try again?\n")
    return response


# Output text to the console.
def intro(weapon, monster):
    print_pause(f"Rumor has it that a {monster} is somewhere around here,",
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty",
                " (but not very effective) dagger.")
    weapon = "dagger"
    enterthefield(weapon, monster)


def enterthefield(weapon, monster):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    # Use the input function in combination with conditional statements
    # (e.g., if and while) to create an interactive program.
    wheretogo = validinput("Please enter 1 or 2.\n", "1", "2")
    if wheretogo == "1":
        knockdoor(weapon, monster)
    elif wheretogo == "2":
        enterthecave(weapon, monster)


def enterthecave(weapon, monster):
    print_pause("You peer cautiously into the cave.")
    if "sword" in weapon:
        print_pause("You've been here before, and gotten all the good stuff. ",
                    "It's just an empty cave now.")
    elif "dagger" in weapon:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger ",
                    "and take the sword with you.")
        weapon = "sword"
    print_pause("You walk back out to the field.")
    enterthefield(weapon, monster)


def knockdoor(weapon, monster):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens ",
                "and out steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    if "dagger" in weapon:
        print_pause(f"You feel a bit under-prepared for this,",
                    f" what with only having a tiny {weapon}.")
    # Use the input function in combination with conditional statements
    # (e.g., if and while) to create an interactive program.
    fight_or_run = validinput("Would you like to (1) fight or (2) run away?\n",
                              "1", "2")
    if fight_or_run == "1":
        fight(weapon, monster)
    elif fight_or_run == "2":
        print_pause("You run back into the field. ",
                    "Luckily, you don't seem to have been followed.")
        enterthefield(weapon, monster)


def fight(weapon, monster):
    if "dagger" in weapon:
        fight_with_dagger(weapon, monster)
    elif "sword" in weapon:
        fight_with_sword(weapon, monster)


def fight_with_dagger(weapon, monster):
    print_pause("You do your best...")
    print_pause(f"but your {weapon} is no match for the {monster}.")
    print_pause("You have been defeated!")
    # Use the input function in combination with conditional statements
    # (e.g., if and while) to create an interactive program.
    playagain = validinput("Would you like to play again? (y/n)\n", "y", "n")
    if playagain == "y":
        print_pause("Excellent! Restarting the game ...")
        play(weapon, monster)
    elif playagain == "n":
        return("Thanks for playing! See you next time.")


def fight_with_sword(weapon, monster):
    print_pause(f"As the {monster} moves to attack, you unsheath ",
                "your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand ",
                "as you brace yourself for the attack.")
    print_pause(f"But the {monster} takes one look at your shiny new toy ",
                "and runs away!")
    print_pause(f"You have rid the town of the {monster}. You are victorious!")
    # Use the input function in combination with conditional statements
    # (e.g., if and while) to create an interactive program.
    playagain = validinput(f"Would you like to play again? (y/n)\n", "y", "n")
    if playagain == "y":
        print_pause("Excellent! Restarting the game ...")
        play()
    elif playagain == "n":
        return("Thanks for playing! See you next time.")


# Refactor code by defining and calling functions.
play()


# Write code that follows the standard Python style guide. DONE
