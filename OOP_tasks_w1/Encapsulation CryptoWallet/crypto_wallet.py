
class CryptoWallet:
    def __init__(self, owner):                   # Initializer with owner name
        self._walletId = str[]   # private
        self._balance = 0.0                      # private
        self._transactions = []                  # private
        self.owner = owner                       # public

    # Public method to deposit
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self._balance += amount
        self._transactions.append(f"Deposit: +{amount}")
        print(f"{amount} deposited successfully.")

    # Public method to withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if amount > self._balance:
            print("Insufficient balance.")
            return

        self._balance -= amount
        self._transactions.append(f"Withdraw: -{amount}")
        print(f"{amount} withdrawn successfully.")

    # Public method to check balance
    def check_balance(self):
        print(f"Wallet {self._walletId} Balance: {self._balance}")

    # Public method to show transactions
    def transaction_history(self):
        if not self._transactions:
            print("No transactions yet.")
            return

        print("Transaction History:")
        for t in self._transactions:
            print(t)

    # Read-only access to wallet ID
    def get_wallet_id(self):
        return self._walletId