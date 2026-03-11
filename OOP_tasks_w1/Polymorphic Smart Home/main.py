from smart_home import SmartDevice, SmartLight, SmartThermostat, SmartLock

smart_homes = []
def operate_all_devices(devices):
    if not devices:
        print("No devices available.")
        return
    print("\n--- Operating Devices ---")
    for device in devices:
        device.operate()
    print("-------------------------\n")



def main():
    devices = []

    while True:
        print("Smart Home Menu")
        print("1 - Add Smart Device")
        print("2 - Operate Devices")
        print("0 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nDevice Types")
            print("1 - Light")
            print("2 - Thermostat")
            print("3 - Lock")
            device_type = input("Select device type: ")
            name = input("Enter device name: ")

            try:
                if device_type == "1":
                    brightness = int(input("Enter brightness (0-100): "))
                    devices.append(SmartLight(name, brightness=brightness))

                elif device_type == "2":
                    temp = int(input("Enter temperature (°C): "))
                    devices.append(SmartThermostat(name, temperature=temp))

                elif device_type == "3":
                    locked_input = input("Start locked? (y/n): ").lower()
                    locked = True if locked_input == "y" else False
                    devices.append(SmartLock(name, locked=locked))

                else:
                    print("Invalid device type.")

            except ValueError:
                print("Invalid input. Please enter numeric values where required.")

        elif choice == "2":
            operate_all_devices(devices)

        elif choice == "0":
            print("Exiting Smart Home System.")
            break

        else:
            print("Invalid menu choice. Try again.")


if __name__ == "__main__":
    main()