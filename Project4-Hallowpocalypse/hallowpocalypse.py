#!/usr/bin/env python3

from game import Game

if __name__ == "__main__":

    commands = ["m", "a", "s", "q"]

    print("Welcome to Hallowpocalypse.")
    print("A Zork-Like game that is made in python3 and probably isn't balanced!")
    print("The goal of the game is to clear each house before you die! Good Luck!")
    print("\nWhat size neighborhood would you like to play?")
    size = int(input("A square neighborhood with a length of: "))
    game = Game()

    while True:
        if not game.getStatus():
            break

        print("Current location: {}".format(game.getPlayerLoc()))
        print("Commands:")
        print("m: Move")
        print("a: Attack")
        print("s: Spy")
        print("q: Quit")
        command = input("")
        if command in commands:
            if command is commands[0]:
                print("Pick a direction: (north, south, east, west)")
                direction = input("Direction: ")
                if not game.move((direction)):
                    print("That was an Invalid Move!")

            if command is commands[1]:
                print("Choose weapon: \n")
                game.getPlayer().printWeapons()

                try:
                    choice = int(input("Choose: "))
                except ValueError:
                    print("Not a valid number!")
                else:
                    game.attackHouse(game.getPlayerLoc(), choice)

            if command is commands[2]:
                game.getNeighborhood().peekHouse(game.getPlayerLoc())

            if command is commands[3]:
                print("Thanks for playing!")
                exit()

        else:
            print("invalid command")
    if game.getNeighborhood().isClear():
        print("You won!")
    else:
        print("You lost!")
