import sys
import os
import classes.fileHandler as FileHandler
import classes.inputHandler as InputHandler

from classes.dataAnalyzer import DataAnalyzer

TEMPLATE_DELIVERIES = f"{os.path.dirname(__file__)}\\deliveries.csv"
TEMPLATE_DRIVERS = f"{os.path.dirname(__file__)}\\drivers.csv"

print("Executing Main Program: Platform Science Demo")

print("The system requires to use CSV files with the correct order. \nDeliveries: Street, City, State, Zip \nDrivers: Name, Last Name")
filesReady = InputHandler.BooleanInput("Do you have your files ready?")

if filesReady == False:
    print("The system includes file templeates")
    requireTemplates = InputHandler.BooleanInput("Do you want a copy?")

    if requireTemplates:
        targetDirectory = FileHandler.FilePath("Enter target directory to copy the templates:")
        FileHandler.CopyFile(TEMPLATE_DELIVERIES, targetDirectory + "\\deliveriesTemplate.csv")
        FileHandler.CopyFile(TEMPLATE_DRIVERS, targetDirectory + "\\driversTemplate.csv")
        print(f"Templates copied to: \n{targetDirectory}\\")
    
    print("Run the main program again when files ready. \nShuting down")
    sys.exit()

deliveriesFile = FileHandler.FilePath("Enter Deliveries CSV file path:")
deliveriesHeader = InputHandler.BooleanInput("CSV File has column headers? (Column Names)")

driversFile = FileHandler.FilePath("Enter Drivers CSV file path:")
driversHeader = InputHandler.BooleanInput("CSV File has column headers? (Column Names)")

deliveriesFileContent = FileHandler.ReadFileContent(deliveriesFile)
if deliveriesHeader == True:
    deliveriesFileContent.pop(0)

driversFileContent = FileHandler.ReadFileContent(driversFile)
if driversHeader == True:
    driversFileContent.pop(0)
    
analizer = DataAnalyzer(deliveriesFileContent, driversFileContent)
analizer.CreateEvaluations()
analizer.AnalizeEvaluations()
analizer.BestEvaluationsInfo()