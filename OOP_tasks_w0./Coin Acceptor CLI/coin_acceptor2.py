# coin_acceptor2 (with CLI task done and changes added)
class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 0.0

    def insertCoin(self, coin_value: float) -> None:
        self.__amount += 1
        self.__value += coin_value

    def getAmount(self) -> int:
        return self.__amount

    def getValue(self) -> float:
        return self.__value

    def returnCoins(self) -> tuple[int, float]:        #Modified class with returnCoins(self) function 
        returned_amount = self.__amount
        returned_value = self.__value

        self.__amount = 0
        self.__value = 0.0

        return returned_amount, returned_value
