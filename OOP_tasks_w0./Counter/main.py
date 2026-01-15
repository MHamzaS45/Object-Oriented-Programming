#main.py

from counter import Counter

def main():
   print("Program starting.")
   counter = Counter()
   print("Options:")
   print("1 - Add count")
   print("2 - Get count")
   print("3 - Zero count")
   print("0 - Exit")

   while True:
    try: 
        choice = int(input("Choice: "))
        if choice == 1:
            counter.addCount()
            print(f"Count increased \n")
        elif choice == 2:
            print(f"Current Count - {counter.getCount()}\n")
        elif choice == 3:
            print("Cleared count!\n")
            counter.zeroCount()
        elif choice == 0:
            print("Exiting program.\n")
            break
        else:
            print("Unknown option!\n")
    except ValueError:
        print("Please enter a valid integer choice.\n")
   return None

if __name__ == "__main__":
    main()
    print("Program ending.")
