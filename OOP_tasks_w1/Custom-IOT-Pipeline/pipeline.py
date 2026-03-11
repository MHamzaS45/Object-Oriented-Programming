#iotpipelines

class TemperatureSensor(deviceId, location, data, ):
    def __init__(self, deviceId, location, data): 
        self.deviceId = deviceId
        self.location = location    
        self.data = data             # initialized data attribute
  
    def serialize(self):
        columns: list[str] = [] # construct row from columns
        columns.append(self.deviceId)
        columns.append(self.location)   
        columns.append(self.data)
        row = self.SEPERATOR.join(columns)
        return row
    def set_value(self, new_value: float) -> None:
       if new_value < 0:
       print("Value can't be negative.")
else:
self.value = new_value
return None
