# main.py

from temperature_converter import TemperatureConverter

def main():
   print("Program starting.")
   print("Initializing temperature converter...")
   print("Temperature converter initialized.")
   temperature_converter = TemperatureConverter()
   print("Options:")
   print("1) Set temperature")
   print("2) Convert to Celsius")
   print("3) Convert to Fahrenheit")
   print("4) Convert to Kelvin")
   print("0) Exit program")

   while True:
    try: 
        choice = int(input("Choice: "))
        if choice == 1:
            temperature = float(input("Enter temperature: "))
            temperature_converter2 = temperature_converter.setTemperature(temperature)
            print(f"Temperature set to {temperature_converter2}\n")
        elif choice == 2:
            print(f"Temperature in celsius - {temperature_converter.toCelsius()}\n")
        elif choice == 3:
            print(f"Temperature in fahrenheit - {temperature_converter.toFahrenheit()}\n")
        elif choice == 4:
            print(f"Temperature in kelvin - {temperature_converter.toKelvin()}\n")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!\n")
    except ValueError:
        print("Please enter a valid integer choice.\n")
   return None

if __name__ == "__main__":
    main()
    print("Program ending.")

