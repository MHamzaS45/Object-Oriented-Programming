#main.py
from coin_acceptor2 import CoinAcceptor


def main():
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    coin_acceptor2 = CoinAcceptor()
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")

    while True:
        try:
            coin = float(input("Insert coin(0 return, -1 exit): "))
            if coin == -1:
                print("Exiting program.")
                break
            elif coin == 0:
                print("Returning coins...")
                amount, value = coin_acceptor.returnCoins()       # return data type for both amount and value. A swifter approach
                print(f"{amount} coins with {value}€ value returned.")
                print(f"Inserted coins = {coin_acceptor.getAmount()}, value = {coin_acceptor.getValue()}€")
            else:
                print("Inserting...")
                coin_acceptor.insertCoin(coin)
                print(f"Inserted coins = {coin_acceptor.getAmount()}, "
                print(f"value = {coin_acceptor.getValue()}€" )
                      
        except ValueError:
            print("Please enter a valid coin value.")
     print("Program ending.")


if __name__ == "__main__":
    main()
