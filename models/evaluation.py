
import classes.stringAnalyzer as StringAnalizer

class Evaluation:
    
    driver = None
    delivery = None
    isEven = False
    ssValue = 0

    def __init__(self, _delivery, _driver):
        self.delivery = _delivery
        self.driver = _driver

    def CheckIfEven(self):
        result = StringAnalizer.CountLetters(self.delivery.street, StringAnalizer.INGORE_CASE)
        if result%2 == 0 : self.isEven = True
    
    def CalculateBaseSSValue(self):
        result = 0

        if self.isEven:
            result = self.EvenSSValue()
        else:
            result = self.OddSSValue()

        self.ssValue = result

    def EvenSSValue (self):
        result = 0
        driverVowels = StringAnalizer.CountVowels(self.driver.name, StringAnalizer.INGORE_CASE)
        result = driverVowels * 1.5
        return result

    def OddSSValue (self):
        driverConsonants = StringAnalizer.CountConsonants(self.driver.name, StringAnalizer.INGORE_CASE)
        return driverConsonants

    def CalculateCommonFactors(self):
        result = 0
        result += self.SameLengthFactor()
        result += self.BothEvenFactor()
        result += self.BothOddFactor()

        if result > 1:
            self.ssValue = self.ssValue * 1.5
        
    def SameLengthFactor(self):
        result = 0
        deliveryStreetNameLength = StringAnalizer.CountLetters(self.delivery.street, StringAnalizer.INGORE_CASE)
        driverNameLength = StringAnalizer.CountLetters(self.delivery.street, StringAnalizer.INGORE_CASE)

        if deliveryStreetNameLength == driverNameLength:
            result = 1
        
        return result
    
    def BothEvenFactor(self):
        result = 0
        if self.isEven == False:
            return result

        driverNameLength = StringAnalizer.CountLetters(self.delivery.street, StringAnalizer.INGORE_CASE)

        if driverNameLength%2 == 0:
            result = 1

        return result

    def BothOddFactor(self):
        result = 0 
        if self.isEven == True:
            return result

        driverNameLength = StringAnalizer.CountLetters(self.delivery.street, StringAnalizer.INGORE_CASE)

        if driverNameLength%2 > 0:
            result = 1

        return result
    
    def Info(self):
        print("Evaluation Info: ")
        self.delivery.Info()
        self.driver.Info()
        print(f"SS Value: {self.ssValue}")