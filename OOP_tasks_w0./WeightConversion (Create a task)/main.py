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
         Feed = 

     except ValueError:
       print("Invalid output. Please re-enter with a valid integer option")
