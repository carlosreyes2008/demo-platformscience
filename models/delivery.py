class Delivery:
    street = ""
    city = ""
    state = ""
    zip = ""

    def __init__(self, data):
        result = data.split(',')
        self.street = result[0]
        self.city = result[1]
        self.state = result[2]
        self.zip = result[3]

    def Info (self):
        print(f"Delivery at => \nStreet:{self.street} City:{self.city} State:{self.state} Zip:{self.zip}")