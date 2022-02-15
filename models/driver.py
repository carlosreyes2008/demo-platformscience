class Driver:

    name = ""
    lastName = ""
    
    def __init__(self, data):
        result = data.split(',')
        self.name = result[0]
        self.lastName = result[1]

    def Info(self):
        print(f"Driver is {self.name} {self.lastName}")