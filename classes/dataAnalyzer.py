from models.delivery import Delivery
from models.driver import Driver
from models.evaluation import Evaluation

class DataAnalyzer:

    deliveries = []
    drivers = []
    evaluations = []
    bestEvaluations = []

    def __init__(self, deliveriesData, driversData):
        print("Initializing Data Analyzer")
        self.ProcessDeliveries(deliveriesData)
        self.ProcessDrivers(driversData)
        print("Analyzer Intialized")

    def ProcessDeliveries(self, deliveriesData):
        for rawDelivery in deliveriesData:
            delivery = Delivery(rawDelivery)
            self.deliveries.append(delivery)

    def ProcessDrivers(self, driversData):
        for rawDriver in driversData:
            driver = Driver(rawDriver)
            self.drivers.append(driver)

    def CreateEvaluations(self):
        print("Creating Evaluations")
        for delivery in self.deliveries:
            for driver in self.drivers:
                evaluation = Evaluation(delivery, driver)
                evaluation.CheckIfEven()
                evaluation.CalculateBaseSSValue()
                evaluation.CalculateCommonFactors()
                self.evaluations.append(evaluation)
        print("Evaluations Created")

    def AnalizeEvaluations(self):
        print("Analizing Evaluations")        
        
        while len(self.evaluations) > 0:
            greatestSsValue = 0
            bestEvaluation = None
            for evaluation in self.evaluations:
                if evaluation.ssValue > greatestSsValue:
                    greatestSsValue = evaluation.ssValue
                    bestEvaluation = evaluation
            
            self.evaluations = [x for x in self.evaluations if x.delivery != bestEvaluation.delivery]
            self.evaluations = [x for x in self.evaluations if x.driver != bestEvaluation.driver]
            self.bestEvaluations.append(bestEvaluation)
            
        print("Best evaluations finded")

    def BestEvaluationsInfo(self):
        print(f"{'Street'.ljust(25)}{'|| City'.ljust(25)}{'|| State'.ljust(25)}{'|| Zip'.ljust(25)}{'|| Driver Name'.ljust(25)}|| SS Score")
        print("".ljust(136,'-'))

        for evaluation in self.bestEvaluations:
            print("".ljust(136,'-'))
            delivery = evaluation.delivery
            driver = evaluation.driver
            row = f"{delivery.street.ljust(25)}"
            row += f"{('|| ' + delivery.city).ljust(25)}"
            row += f"{('|| ' + delivery.state).ljust(25)}"
            row += f"{('|| ' + delivery.zip).ljust(25)}"
            row += f"{('|| ' + driver.name + ' ' + driver.lastName).ljust(25)}"
            row += f"|| {evaluation.ssValue}"
            print(row)