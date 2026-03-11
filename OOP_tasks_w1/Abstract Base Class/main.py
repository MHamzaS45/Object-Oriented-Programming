########
# main.py - Main program to create game characters and simulate battles using an abstract base class structure.
#########

from game_characters import GameCharacter, Shinigami, Hollow, Quincy 

characters = GameCharacter # Get all subclasses of GameCharacter for dynamic character creation

def simulate_battle(characters):

    if not characters:
        print("No characters available for battle.\n")
        return
    print("\n--- Battle Simulation ---")

    for character in characters:
        if isinstance(character, GameCharacter):
          character.attack()
          character.defend()
          print("---------------------")

    print("Battle simulation complete!\n")

################################################

def main():
    characters = []
    while True:

        print("\nGame Character Menu")
        print("1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":
                print("\Select Your Character Type")
                print("1 - Shinigami")
                print("2 - Hollow")
                print("3 - Quincy")
                char_type = input("Select type: ")
                name = input("Enter character name: ")

                if char_type == "1":
                    characters.append(Shinigami(name))

                elif char_type == "2":
                    characters.append(Hollow(name))

                elif char_type == "3":
                    characters.append(Quincy(name))

                else:
                    print("Invalid character type.\n")
                    continue

            elif choice == "2":
                simulate_battle(characters)

            elif choice == "0":
                print("\nExiting game.")
                break

            else:
                print("Invalid menu choice. Please try again.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__": # run program
    main()