# For this create a task, we will use the example of weight machine conversion. A class for Weight Conversion is to be made, with the property "__weight: float" with the following methods
# 1. setWeight(weight:float) 
# 2. toKiloGram() -> float:
# 3. toMiliGram()  -> float:
# 4. toTons() -> float:
# 
# Standard weight is expected to be grams (g)

class WeightConversion:
    def __init__(self): 
        self.__weight = 0.0

    def setWeight(self, weight: float) -> None:
        self.__weight = weight
        return self.__weight

    def toKiloGram(self) -> float:
        return (self.__weight / 1000) 
    
    def toMilliGram(self) -> float:
        return (self.__weight * 1000)
    
    def toTons(self) -> float:
        return (self.__weight / 1000000)
