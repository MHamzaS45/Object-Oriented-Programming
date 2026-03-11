# VR player class
class Player(Entity):
    def __init__(self, name, position=(0, 0, 0), health=100):
        super().__init__(name, position)
        self.health = health

    def interact(self):
        print(f"{self.name} explores the environment and checks status (Health: {self.health}).")


class NPC(Entity):
    def __init__(self, name, position=(0, 0, 0), role="Villager"):
        super().__init__(name, position)
        self.role = role

    def interact(self):
        print(f"{self.name} the {self.role} talks to the player or gives a quest.")


class Object(Entity):
    def __init__(self, name, position=(0, 0, 0), description=""):
        super().__init__(name, position)
        self.description = description

    def interact(self):
        print(f"You examine the {self.name}: {self.description}")
