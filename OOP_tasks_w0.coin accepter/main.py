from coin_acceptor import CoinAcceptor


def show_menu():
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")


def main():
    coin_acceptor = CoinAcceptor()
    print("Program starting.")

    while True:
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


if __name__ == "__main__":
    main()
