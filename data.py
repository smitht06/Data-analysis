"""
Anthony Smith
SDEV300
LAB 5
data
"""
#import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#use pandas to read files, format numbers to float .2
popData = pd.read_csv('PopChange.csv')
housingData = pd.read_csv('Housing.csv')
pd.options.display.float_format = "{:.2f}".format


#while statement with try block to catch value errors
while(True):
    try:
        #print menu and take input from user
        print("""
        1. Population Data
        2. Housing Data
        3. Exit the Program
        """)
        chooseFile = input("Please choose a file: ")
    except ValueError:
        print("Enter a numeric value")

    #if statement determines the choice of csv files to analyze    
    if chooseFile == '1':
        #print menu to user to choose the column to analyze
        while(True):
            print("You have entered population Data ")
            print("""Select the Column you want to analyze:
                        a. Pop Apr 1
                        b. Pop Jul 1
                        c. Change Pop
                        d. back""")
            popChoice = input()
            
            #if statment to determine which column was selected
            if(popChoice == 'a'):
                print("The statistics for this column are: ")
                print(popData["PopApr1"].describe())
                #create histogram and save to file
                plt.hist(popData["PopApr1"],bins = 30)
                plt.grid(True)
                fig1=plt
                fig1.savefig('display3.svg')
                print("The Histogram of this column can be downloaded now.")
            elif(popChoice == 'b'):
                print("The statistics for this column are: ")
                print(popData["PopJul1"].describe())
                #create histogram and save to file
                plt.hist(popData["PopJul1"],bins = 30)
                plt.grid(True)
                fig1=plt
                fig1.savefig('display4.svg')
                print("The Histogram of this column can be downloaded now.")
            elif(popChoice == 'c'):
                print("The statistics for this column are: ")
                print(popData["ChangePop"].describe())
                #create histogram and save to file
                plt.hist(popData["ChangePop"],bins = 30)
                fig1=plt
                fig1.savefig('display6.svg')
                print("The Histogram of this column can be downloaded now.")
            #break out of loop if choice is d
            elif(popChoice == 'd'):
                break 
    #loop for if user chooses housing data        
    elif chooseFile == '2':
        while(True):
            print("You have entered Housing Data ")
            print("""Select the Column you want to analyze:
                        a. Age
                        b. Bedrooms
                        c. Year Built
                        d. Rooms
                        e. Utility bill
                        f. back""")
            houseChoice = input()
            #if statment to determine which column was selected
            if houseChoice == 'a':
                print("The statistics for this column are: ")
                print(housingData["AGE"].describe())
                #create histogram and save to file
                plt.hist(housingData["AGE"],bins = 30)
                plt.grid(True)
                fig1=plt
                fig1.savefig('display7.svg')
                print("The Histogram of this column can be downloaded now.")
            elif(houseChoice == 'b'):
                print("The statistics for this column are: ")
                print(housingData["BEDRMS"].describe())
                #create histogram and save to file
                plt.hist(housingData["BEDRMS"],bins = 30)
                plt.grid(True)
                fig1=plt
                fig1.savefig('display8.svg')
                print("The Histogram of this column can be downloaded now.")
            elif(houseChoice == 'c'):
                print("The statistics for this column are: ")
                print(housingData["BUILT"].describe())
                plt.hist(housingData["BUILT"],bins = 30)
                plt.grid(True)
                fig1=plt
                fig1.savefig('display9.svg')
                print("The Histogram of this column can be downloaded now.")
            elif(houseChoice == 'd'):
                print("The statistics for this column are: ")
                print(housingData["ROOMS"].describe())  
                plt.hist(housingData["ROOMS"],bins = 30)
                plt.grid(True)
                fig1=plt
                fig1.savefig('display10.svg')
                print("The Histogram of this column can be downloaded now.")
            elif(houseChoice == 'e'):
                print("The statistics for this column are: ")
                print(housingData["UTILITY"].describe())       
                plt.hist(housingData["UTILITY"],bins = 30)
                plt.grid(True)
                fig1=plt
                fig1.savefig('display11.svg')
                print("The Histogram of this column can be downloaded now.")
            elif(houseChoice == 'f'):
                break        
    #exit program if user enters 3
    elif(chooseFile == '3'):
        exit(0)
    else:
        print("Select from the menu")