from abc import ABC, abstractmethod
from colorama import init, Fore, Style

init (autoreset=True) # Initialize colorama for colored output

class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name #initializes the name of the character
    @abstractmethod
    def attack(self):
        pass #abstract method for attack, to be implemented by subclasses
    def defend(self):
        pass #abstract method for defend to be implemented by subclasses

# Subclass for a Warrior character
class Shinigami(GameCharacter):      # Shinigami is synonymous with warrior in this context
    def attack(self):
        print (f"{self.name}  {Fore.RED}attacks{Style.RESET_ALL} with a swing from their Zanpakutou!")
    def defend(self):
        print(f"{self.name}  {Fore.GREEN}defends{Style.RESET_ALL} by countering with their sword!")

# Subclass for a Mage character
class Hollow(GameCharacter):      # Hollow is synonymous with mage in this context
    def attack(self):
        print(f"{self.name}  {Fore.BLUE}attacks{Style.RESET_ALL} with a Cero!")
    def defend(self):
        print(f"{self.name}  {Fore.YELLOW}defends{Style.RESET_ALL} by shielding with Hierro!")

# Subclass for an Archer character
class Quincy(GameCharacter):      # Uryu Ishida is synonymous with archer in this context
    def attack(self):
        print(f"{self.name}  {Fore.MAGENTA}attacks{Style.RESET_ALL} with a Quincy arrow!")
    def defend(self):
        print(f"{self.name}  {Fore.CYAN}defends{Style.RESET_ALL} by evading with HirenKyaku!")
    
