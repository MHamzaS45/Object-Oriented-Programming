#main.py
from coin_acceptor import CoinAcceptor

def main():
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")
    coin_acceptor = CoinAcceptor()
    print("Program starting.")

    while True:
      try:  
        show_menu()
        choice = input("Your choice: ")
        if choice == "1":
            coin_acceptor.insertCoin()
        elif choice == "2":
            amount = coin_acceptor.getAmount()
            print(f"Currently '{amount}' coins in coin acceptor")
        elif choice == "3":
            returned = coin_acceptor.returnCoins()
            print(f"Coin acceptor returned '{returned}' coins.")
        elif choice == "0":
            print("Program ending.")
            break
        else:
            print("Invalid choice. Please try again.")
      except ValueError:
          print("Please enter a valid integer choice.\n")
      return None


if __name__ == "__main__":
    main()
