# Polymorphism class for Smart Home devices

class SmartDevice:
    def __init__(self, device_name, status):
        self.device_name = device_name
        self.status = 0 
    def operate(self):
        print(f"{self.device_name} is operating.")

class SmartLight(SmartDevice):
    def __init__(self, device_name, status):
        super().__init__(device_name, status)
    
    def turn_on(self):
        self.status = 1
        print(f"{self.device_name} is now ON.")
    
    def turn_off(self):
        self.status = 0
        print(f"{self.device_name} is now OFF.")

class SmartThermostat(SmartDevice):
    def __init__(self, device_name, status):
        super().__init__(device_name, status)
        self.temperature = temperature  # type: ignore
    
    def operate(self):
        self.status = True
        print(f"{self.device_name} temperature set to {self.temperature}°C.")

class SmartLock(SmartDevice):
    def __init__(self, device_name, status):
        super().__init__(device_name, status)
    
    def operate(self):
        self.status = 1
        print(f"{self.device_name} is now LOCKED.")
    
    def unlock(self):
        self.status = 0
        print(f"{self.device_name} is now UNLOCKED.")