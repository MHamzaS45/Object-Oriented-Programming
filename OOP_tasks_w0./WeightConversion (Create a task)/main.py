#main.py 

from weight_conversion import WeightConversion

def main():
   print("Program starting.")
   print("Initializing weight converter...")
   print("Weight converter initialized.")
   print("Greetings user...")
   weight_conversion = WeightConversion()
   print("Options:")
   print("1) Set weight")
   print("2) Convert to kilograms")
   print("3) Convert to milligrams")
   print("4) Convert to tons")
   print("0) Exit program")

   while True:
     try:
       choice = int(input("Enter your choice: "))
       if choice == 1:
         Feed = weight_conversion.setweight()
       elif choice == 2:
         Feed = weight_conversion.toKiloGram()
       elif choice == 3:
         Feed = weight_conversion.toMilliGram()
       elif choice == 4:
          Feed = weight_conversion.toTons()
       elif choice == "0":
            print("Program ending.")
            break
        else:
            print("Invalid choice. Please try again.")
     except ValueError:
       print("Invalid output. Please re-enter with a valid integer option")
