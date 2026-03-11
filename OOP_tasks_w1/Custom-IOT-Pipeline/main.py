import csv

from pipeline.data_pipeline import DataPipeline

    def serialize(self, filename="iot_data.csv"):

        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)

                for device in self.devices:
                    writer.writerow(device.to_list())

            print("Data serialized to CSV successfully.")

        except Exception as e:
            print("Serialization error:", e)

    # ---------------------------
    # Deserialize from CSV
    # ---------------------------

    def deserialize(self, filename="iot_data.csv"):

        try:
            self.devices.clear()

            with open(filename, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    dtype, device_id, location, data = row

                    if dtype == "Temperature":
                        device = TemperatureSensor(device_id, location, data)

                    elif dtype == "Humidity":
                        device = HumiditySensor(device_id, location, data)

                    elif dtype == "Motion":
                        device = MotionSensor(device_id, location, data)

                    else:
                        device = IoTDevice(device_id, location, data)

                    self.devices.append(device)

            print("Data deserialized successfully.")

        except FileNotFoundError:
            print("CSV file not found.")

        except Exception as e:
            print("Deserialization error:", e)

    # ---------------------------
    # Encrypt File
    # ---------------------------

    def encrypt(self, filename="iot_data.csv", encrypted_file="iot_data.enc"):

        try:
            with open(filename, "rb") as f:
                data = f.read()

            encrypted = self.cipher.encrypt(data)

            with open(encrypted_file, "wb") as f:
                f.write(encrypted)

            print("File encrypted successfully.")

        except Exception as e:
            print("Encryption error:", e)

    # ---------------------------
    # Decrypt File
    # ---------------------------

    def decrypt(self, encrypted_file="iot_data.enc", output_file="iot_data_decrypted.csv"):

        try:
            with open(encrypted_file, "rb") as f:
                encrypted = f.read()

            decrypted = self.cipher.decrypt(encrypted)

            with open(output_file, "wb") as f:
                f.write(decrypted)

            print("File decrypted successfully.")

        except Exception as e:
            print("Decryption error:", e)


# ===============================
# Menu System
# ===============================

def menu():

    pipeline = DataPipeline()

    while True:

        print("\nIoT Data Pipeline")
        print("1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("4 - Encrypt Data")
        print("5 - Decrypt Data")
        print("0 - Exit")

        choice = input("Select option: ")

        try:

            if choice == "1":
                pipeline.add_device()

            elif choice == "2":
                pipeline.serialize()

            elif choice == "3":
                pipeline.deserialize()

            elif choice == "4":
                pipeline.encrypt()

            elif choice == "5":
                pipeline.decrypt()

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid menu choice.")

        except Exception as e:
            print("Unexpected error:", e)


# ===============================
# Run Program
# ===============================

if __name__ == "__main__":
    menu()