# temperature_converter 

class TemperatureConverter:
    def __init__(self): # INIT method to initialize the class
        self.__temperature = 0.0

    def setTemperature(self, temperature: float) -> None:
        self.__temperature = temperature
        return self.__temperature

    def toCelsius(self) -> float:
        return self.__temperature
    
    def toFahrenheit(self) -> float:
        return ((self.__temperature * 9/5) + 32)
    
    def toKelvin(self) -> float:
        return (self.__temperature + 273.15)
    
