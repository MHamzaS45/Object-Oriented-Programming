
from virtual_reality import Player, NPC, Object 

def interact_all_entities(entities):
    if not entities:
        print("No entities to interact with.\n")
        return

    print("\n--- Interacting with Entities ---")
    for entity in entities:
        entity.interact()
    print("-------------------------------\n")


def main():               # menu system for VR simulation
    entities = []

    while True:
        print("Virtual Reality Simulation Menu")
        print("1 - Add Entity")
        print("2 - Interact with Entities")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nEntity Types")
            print("1 - Player")
            print("2 - NPC")
            print("3 - Object")
            entity_type = input("Select entity type: ")
            name = input("Enter entity name: ")

            try:
                if entity_type == "1":
                    health = int(input("Enter player health: "))
                    entities.append(Player(name, health=health))

                elif entity_type == "2":
                    role = input("Enter NPC role (e.g., Villager, Merchant): ")
                    entities.append(NPC(name, role=role))

                elif entity_type == "3":
                    description = input("Enter object description: ")
                    entities.append(Object(name, description=description))

                else:
                    print("Invalid entity type.")

            except ValueError:
                print("Invalid input. Numeric values required where applicable.")

        elif choice == "2":
            interact_all_entities(entities)

        elif choice == "3":
            print("Exiting simulation.")
            break

        else:
            print("Invalid menu choice. Try again.")


if __name__ == "__main__":
    main()