#import streamlit as st
#import pandas as pd
#import numpy as np

#st.title("Blac jack game")

#PlayerName = st.text_input("Player Name", "Mc Damon")
#st.write("Player name is", PlayerName)
IR = 0.03 ## set the interest rate 3% as constant for time deposit option
M = 4 ## set 4 as constant for the number of compound occurance in a year for time deposit option
PROP_RATE = 0.05 ## Predicted annaul property price increase rate
INFLATION_RATE = 0.01 ## Predicted annual inflation rate


from os import stat
import streamlit as tk
from tkinter import IntVar, Label, OptionMenu, messagebox
from typing import Text


class guiApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuPage, TimeDepositPage, HoldCashPage, PropInvestPage):
            page = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPage")

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class MenuPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Investment Analysis")
        self.controller.geometry("1000x800")
        self.configure(bg = "#ffffff")
        
        title_Label = tk.Label(self, text = "Welcome to the program", 
                              font=("Arial", 40),
                              fg="#000000", bg="#ffffff")
        title_Label.grid(row = 0, column = 0)

        description_Label = tk.Label(self, text = "This program will calculate the profitability of investments using the data provided below. \nAn annual percentage yield (APY), will be output. \nThere are 3 types of investment available",
                              font=("Arial", 15),
                              fg="#000000", bg="#ffffff")
        description_Label.grid(row = 1, column = 0)


        def timeDeposit():
            controller.show_frame("TimeDepositPage")


        def holdCash():
            controller.show_frame("HoldCashPage")


        def PropInvest():
            controller.show_frame("PropInvestPage")


        fileText = {}
        try:
            f = open("guiWelcomeText.txt", 'r')
            try:
                fileText = eval(f.read())

                label1 = tk.Label(self, text = "1.Annual Interest Rate: ", 
                                  font=("Arial", 15),
                                  fg="#000000", bg="#ffffff")
                label1.grid(sticky="W", row = 2, column = 0)
                label4 = tk.Label(self, text = fileText["Annual Interest Rate"], 
                                  font=("Arial", 15),
                                  fg="#000000", bg="#ffffff")
                label4.grid(sticky="W", row = 2, column = 1)

                label2 = tk.Label(self, text = "2.Property Price Growth Rate: ", 
                                  font=("Arial", 15),
                                  fg="#000000", bg="#ffffff")
                label2.grid(sticky="W",row = 3, column = 0)
                label5 = tk.Label(self, text = fileText["Property Price Growth Rate"], 
                                  font=("Arial", 15),
                                  fg="#000000", bg="#ffffff")
                label5.grid(sticky="W", row = 3, column = 1)

                label3 = tk.Label(self, text = "3.Inflation Rate: ", 
                                  font=("Arial", 15),
                                  fg="#000000", bg="#ffffff")
                label3.grid(sticky="W",row = 4, column = 0)
                label6 = tk.Label(self, text = fileText["Inflation Rate"], 
                                  font=("Arial", 15),
                                  fg="#000000", bg="#ffffff")
                label6.grid(sticky="W", row = 4, column = 1)

                btn_A = tk.Button(self, text = "A. Time Deposit", command = timeDeposit,
                                  bg="#94f8ff", fg="#000000",
                                  width = 20, height = 3)
                btn_A.grid(row = 5, column = 0)

                btn_B = tk.Button(self, text = "B. Hold As Cash", command = holdCash,
                                  bg="#94f8ff", fg="#000000",
                                  width = 20, height = 3)
                btn_B.grid(row = 6, column = 0)

                btn_C = tk.Button(self, text = "C. Invest To Property", command = PropInvest,
                                  bg="#94f8ff", fg="#000000",
                                  width = 20, height = 3)
                btn_C.grid(row = 7, column = 0)

                btn_Ext = tk.Button(self, text = "Exit the Program", command = self.controller.destroy, ## exit button for exitting and closing the GUI
                                  bg="#94f8ff", fg="#000000",
                                  width = 20, height = 3)
                btn_Ext.grid(row = 8, column = 0)

            except KeyError: ## When no corresponding key was found in the dictionary stored in the text file, it indicates the file has been damaged
                err_L2 = tk.Label(self, text="Coresponding file is damaged. Please fix it",
                               font=("Arial", 20),
                               fg="#000000", bg="#ffffff")
                err_L2.grid(row = 1, column = 0)
        except FileNotFoundError: ## When no corresponding text file was found and opened. It returns a message of indicating the file was not found.
            err_L1 = tk.Label(self, text="Coresponding file not found, please make sure it was not removed",
                               font=("Arial", 20), 
                               fg="#000000", bg="#ffffff")
            err_L1.grid(row = 1, column = 0)



class TimeDepositPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        Label_1 = tk.Label(self, text="Investment type: ", font=("Arial", 15), 
                           fg="#000000", bg="#ffffff")
        Label_1.grid(row = 0, column = 0, sticky="e")

        Label_2 = tk.Label(self, text="Time deposit", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_2.grid(row = 0, column = 1)

        Label_3 = tk.Label(self, text="Please enter a value larger than 0 as principal", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_3.grid(row = 2, column = 0, columnspan = 2)


        Label_7 = tk.Label(self, text="Principal: ", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_7.grid(row = 3, column=0, sticky="e")

        Label_8 =  tk.Label(self, text="Years: ", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_8.grid(row = 5, column=0, sticky="e")


        iPrincipal = tk.StringVar()
        Ent_Principal = tk.Entry(self, textvariable = iPrincipal,
                            font = ("Arial", 12), width = 20)
        Ent_Principal.grid(row = 3, column = 1)

        Label_5 = tk.Label(self, text="Please enter a value larger than 0 for principal", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_5.grid(row = 4, column = 1)
        Label_6 = tk.Label(self, text="Please enter a integer number for principal", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_6.grid(row = 4, column = 1)

        Label_5.grid_remove()
        Label_6.grid_remove()
        

        iYear = tk.StringVar()
        Ent_Year = tk.Entry(self, textvariable = iYear,
                            font = ("Arial", 12), width = 20)
        Ent_Year.grid(row = 5, column=1)

        Label_9 = tk.Label(self, text="Please enter a value larger than 0 for year", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_9.grid(row = 6, column = 1)
        Label_10 = tk.Label(self, text="Please enter a integer number for year", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_10.grid(row = 6, column = 1)

        Label_9.grid_remove()
        Label_10.grid_remove()


        def recordResults (iPrinc, iYear, fBalance, fAPY):
            currentTime = datetime.datetime.now()
            year = currentTime.strftime("%Y")
            month = currentTime.strftime("%B")
            day = currentTime.strftime("%d")
            hour = currentTime.strftime("%H")
            mins = currentTime.strftime("%M")
            secs = currentTime.strftime("%S")
            reportTime = year + "-" + month + "-" + day + " " + hour + ":" + mins + ":" + secs

            sRent = iRent.get()
            ans = CheckRent(sRent)

            f = open("Report.txt", "a")
            f.write("---Value Report---\n")
            f.write("Generation time: " + reportTime + "\n")
            f.write("\nType of investmetn: " + type + "\n")
            f.write("Type : Property Investment\n")
            f.write("Property price: ", iPrinc)
            f.write("Rental income: ", ans[1])
            f.write("Year to be held: ", iYear)
            f.write("Final asset value: ", fBalance)
            f.write("APY: ", fAPY)
            f.write("\n\n\n")
            f.close()


        def Cal_TimeDeposit(iPrinc, iYear):
            fCompoundMultiplier = (1 + (IR / M)) ** M ## fCompoundMultiplier would be used to multiply with the principal and get the total amount directly.
            fFinalMultiplier = fCompoundMultiplier
            for x in range (iYear - 1): ## A for loop is used to do the calculation of comound interest.
                fFinalMultiplier *= fCompoundMultiplier
            fBalance = iPrinc * fFinalMultiplier ## fBalance is the total amount of money after iYear years.
            fAPY = ((1 + (IR / M)) ** M) - 1 ## fAPY is the annual precentage yield

            Output_Label1 = tk.Label(self, text = "Principal: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label1.grid(row = 10, column = 0, sticky = "e")
            Output_Label5 = tk.Label(self, text = iPrinc,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label5.grid(row = 10, column = 1, sticky = "w")

            Output_Label2 = tk.Label(self, text = "Years to be held: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label2.grid(row = 11, column = 0, sticky = "e")
            Output_Label6 = tk.Label(self, text = iYear,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label6.grid(row = 11, column = 1, sticky = "w")

            Output_Label3 = tk.Label(self, text = "Final Value: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label3.grid(row = 12, column = 0, sticky = "e")
            Output_Box7 = tk.Entry(self, text = fBalance, ## Output with entry widget
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Box7.grid(row = 12, column = 1, sticky = "w")
            Output_Box7.delete(0 , tk.END)
            Output_Box7.insert(0, fBalance)
            Output_Box7.config(state= "disabled") ## not allowing users to change the value of it

            Output_Label4 = tk.Label(self, text = "Annual Percentage Yield: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label4.grid(row = 13, column = 0, sticky = "e")
            Output_Label8 = tk.Label(self, text = fAPY,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label8.grid(row = 13, column = 1, sticky = "w")

            recordResults(iPrinc, iYear, fBalance, fAPY)


        def CheckP(sPrinc):
            flag1 = False
            try:
                iPrinc = int(sPrinc)
                assert iPrinc > 0
                flag1 = True
                return flag1
            except AssertionError: ## When the value of Principal is not larger than 0, it return a message to user to re-input
                Label_5.grid(row = 4, column = 1)

            except ValueError: ## When the value of Principal is not an integer number, it return a message to user to re-input
                Label_6.grid(row = 4, column = 1)


        def CheckY(sYear):
            flag2 = False
            try:
                iPrinc = int(sYear)
                assert iPrinc > 0
                flag2 = True
                return flag2
            except AssertionError: ## When the value of Year is not larger than 0, it return a message to user to re-input
                Label_9.grid(row = 6, column = 1)
            except ValueError: ## When the value of Year is not an integer number, it return a message to user to re-input
                Label_10.grid(row = 6, column = 1)


        def CheckValid():

            Label_5.grid_remove()
            Label_6.grid_remove()
            Label_9.grid_remove()
            Label_10.grid_remove()

            sYear = iYear.get() 
            sPrinc = iPrincipal.get()

            CheckP(sPrinc)
            CheckY(sYear)

            if CheckP(sPrinc) == True and CheckY(sYear) == True:
                Cal_TimeDeposit(int(sPrinc), int(sYear))


        def ReturnToMenu():
            controller.show_frame("MenuPage")

        Btn_Enter = tk.Button(self, text = "Calculate", command = CheckValid, ## Button for calculation
                                bg="#94f8ff", fg="#000000",
                                width = 12, height = 3)
        Btn_Enter.grid(row = 8, column = 1)

        Btn_Return = tk.Button(self, text = "Return To Menu", command = ReturnToMenu, ## Button for returning to the menu
                               bg="#94f8ff", fg="#000000",
                                width = 12, height = 3)
        Btn_Return.grid(row = 14, column = 1)

        



class HoldCashPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        Label_1 = tk.Label(self, text="Investment type: ", font=("Arial", 15), 
                           fg="#000000", bg="#ffffff")
        Label_1.grid(row = 0, column = 0, sticky="e")

        Label_2 = tk.Label(self, text="Holding as cash", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_2.grid(row = 0, column = 1)

        Label_3 = tk.Label(self, text="Please enter a value larger than 0 as the amount of cash", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_3.grid(row = 2, column = 0, columnspan = 2)

        Label_7 = tk.Label(self, text="Cash: ", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_7.grid(row = 3, column=0, sticky="e")

        Label_8 =  tk.Label(self, text="Years: ", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_8.grid(row = 5, column=0, sticky="e")


        iCash = tk.StringVar()
        Ent_Principal = tk.Entry(self, textvariable = iCash,
                            font = ("Arial", 12), width = 20)
        Ent_Principal.grid(row = 3, column = 1)

        Label_5 = tk.Label(self, text="Please enter a value larger than 0 for cash to be held", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_5.grid(row = 4, column = 1)
        Label_6 = tk.Label(self, text="Please enter a integer number for cash to be held", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_6.grid(row = 4, column = 1)

        Label_5.grid_remove()
        Label_6.grid_remove()
        

        iYear = tk.StringVar()
        Ent_Year = tk.Entry(self, textvariable = iYear,
                            font = ("Arial", 12), width = 20)
        Ent_Year.grid(row = 5, column=1)

        Label_9 = tk.Label(self, text="Please enter a value larger than 0 for year", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_9.grid(row = 6, column = 1)
        Label_10 = tk.Label(self, text="Please enter a integer number for year", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_10.grid(row = 6, column = 1)

        Label_9.grid_remove()
        Label_10.grid_remove()


        def recordResults (iCash, iYear, fRealValue, fAPY):
            currentTime = datetime.datetime.now()
            year = currentTime.strftime("%Y")
            month = currentTime.strftime("%B")
            day = currentTime.strftime("%d")
            hour = currentTime.strftime("%H")
            mins = currentTime.strftime("%M")
            secs = currentTime.strftime("%S")
            reportTime = year + "-" + month + "-" + day + " " + hour + ":" + mins + ":" + secs

            sRent = iRent.get()
            ans = CheckRent(sRent)

            f = open("Report.txt", "a")
            f.write("---Value Report---\n")
            f.write("Generation time: " + reportTime + "\n")
            f.write("\nType of investmetn: " + type + "\n")
            f.write("Type : Property Investment\n")
            f.write("Property price: ", iCash)
            f.write("Rental income: ", ans[1])
            f.write("Year to be held: ", iYear)
            f.write("Final asset value: ", fRealValue)
            f.write("APY: ", fAPY)
            f.write("\n\n\n")
            f.close()


        def Cal_HoldCash(iCash, iYear):
            fRealValue = iCash / ((1 + INFLATION_RATE) ** iYear)
            fAPY = (1 / (1 + INFLATION_RATE)) - 1
            Output_Label1 = tk.Label(self, text = "Principal: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label1.grid(row = 10, column = 0, sticky = "e")
            Output_Label5 = tk.Label(self, text = iCash,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label5.grid(row = 10, column = 1, sticky = "w")

            Output_Label2 = tk.Label(self, text = "Years to be held: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label2.grid(row = 11, column = 0, sticky = "e")
            Output_Label6 = tk.Label(self, text = iYear,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label6.grid(row = 11, column = 1, sticky = "w")

            Output_Label3 = tk.Label(self, text = "Final Value: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label3.grid(row = 12, column = 0, sticky = "e")
            Output_Box7 = tk.Entry(self, text = fRealValue, ## Output with entry widget
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Box7.grid(row = 12, column = 1, sticky = "w")
            Output_Box7.delete(0 , tk.END)
            Output_Box7.insert(0, fRealValue)
            Output_Box7.config(state= "disabled") ## not allowing users to change the value of it

            Output_Label4 = tk.Label(self, text = "Annual Percentage Yield: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label4.grid(row = 13, column = 0, sticky = "e")
            Output_Label8 = tk.Label(self, text = fAPY,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label8.grid(row = 13, column = 1, sticky = "w")

            recordResults(iCash, iYear, fRealValue, fAPY)


        def CheckP(sCash):
            flag1 = False
            try:
                iPrinc = int(sCash)
                assert iPrinc > 0
                flag1 = True
                return flag1
            except AssertionError: ## When the value of Cash is not larger than 0, it return a message to user to re-input
                Label_5.grid(row = 4, column = 1)

            except ValueError: ## When the value of Cash is not an integer number, it return a message to user to re-input
                Label_6.grid(row = 4, column = 1)


        def CheckY(sYear):
            flag2 = False
            try:
                iPrinc = int(sYear)
                assert iPrinc > 0
                flag2 = True
                return flag2
            except AssertionError: ## When the value of Year is not larger than 0, it return a message to user to re-input
                Label_9.grid(row = 6, column = 1)

            except ValueError: ## When the value of Year is not an integer number, it return a message to user to re-input
                Label_10.grid(row = 6, column = 1)


        def CheckValid():

            Label_5.grid_remove()
            Label_6.grid_remove()
            Label_9.grid_remove()
            Label_10.grid_remove()

            sYear = iYear.get() 
            sCash = iCash.get()

            CheckP(sCash)
            CheckY(sYear)

            if CheckP(sCash) == True and CheckY(sYear) == True:
                Cal_HoldCash(int(sCash), int(sYear))

        Btn_Enter = tk.Button(self, text = "Calculate", command = CheckValid, ## Button for calculation
                                bg="#94f8ff", fg="#000000",
                                width = 12, height = 3)
        Btn_Enter.grid(row = 8, column = 1)

        
        def ReturnToMenu():
            controller.show_frame("MenuPage")


        Btn_Return = tk.Button(self, text = "Return To Menu", command = ReturnToMenu, ## Button for returning to the menu
                               bg="#94f8ff", fg="#000000",
                                width = 12, height = 3)
        Btn_Return.grid(row = 14, column = 1)



class PropInvestPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        Label_1 = tk.Label(self, text="Investment type: ", font=("Arial", 15), 
                           fg="#000000", bg="#ffffff")
        Label_1.grid(row = 0, column = 0, sticky="e")

        Label_2 = tk.Label(self, text="Property", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_2.grid(row = 0, column = 1)

        Label_3 = tk.Label(self, text="Please enter a value larger than 0 as the price of property", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_3.grid(row = 2, column = 0, columnspan = 2)

        Label_7 = tk.Label(self, text="Price: ", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_7.grid(row = 3, column=0, sticky="e")

        Label_8 =  tk.Label(self, text="Years: ", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_8.grid(row = 5, column=0, sticky="e")

        options = ["Yes", "No"]
        choice = tk.StringVar()
        choice.set("Yes")
        rentChoice = OptionMenu(self, choice, *options) ## A drop down list widget for users to make a choice of renting out the property or not
        rentChoice.grid(row = 7, column = 1)

        iPrice = tk.StringVar()
        Ent_Principal = tk.Entry(self, textvariable = iPrice,
                            font = ("Arial", 12), width = 20)
        Ent_Principal.grid(row = 3, column = 1)

        Label_5 = tk.Label(self, text="Please enter a value larger than 0 as price of property", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_5.grid(row = 4, column = 1)
        Label_6 = tk.Label(self, text="Please enter a integer number for as price of property", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_6.grid(row = 4, column = 1)

        Label_5.grid_remove()
        Label_6.grid_remove()
        

        iYear = tk.StringVar()
        Ent_Year = tk.Entry(self, textvariable = iYear,
                            font = ("Arial", 12), width = 20)
        Ent_Year.grid(row = 5, column=1)

        Label_9 = tk.Label(self, text="Please enter a value larger than 0 for year", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_9.grid(row = 6, column = 1)
        Label_10 = tk.Label(self, text="Please enter a integer number for year", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_10.grid(row = 6, column = 1)

        Label_9.grid_remove()
        Label_10.grid_remove()


        iRent = tk.StringVar()
        Ent_Rent = tk.Entry(self, textvariable = iRent,
                            font = ("Arial", 12), width = 20)
        Ent_Rent.grid(row = 8, column=1)

        Label_13 = tk.Label(self, text = "Rental income per month: ",
                            font = ("Arial", 12), width = 20,
                            fg="#000000", bg="#ffffff")
        Label_13.grid(row = 8, column = 0)

        Label_11 = tk.Label(self, text="Please enter a value larger than 0 for monthly rental income", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_11.grid(row = 9, column = 1)
        Label_12 = tk.Label(self, text="Please enter a integer number for monthly rental income", font=("Arial", 12),
                           fg="#000000", bg="#ffffff")
        Label_12.grid(row = 9, column = 1)

        Label_11.grid_remove()
        Label_12.grid_remove()


        def recordResults (iPrice, iYear, fTotalAssetValue, fAPY):
            currentTime = datetime.datetime.now()
            year = currentTime.strftime("%Y")
            month = currentTime.strftime("%B")
            day = currentTime.strftime("%d")
            hour = currentTime.strftime("%H")
            mins = currentTime.strftime("%M")
            secs = currentTime.strftime("%S")
            reportTime = year + "-" + month + "-" + day + " " + hour + ":" + mins + ":" + secs

            sRent = iRent.get()
            ans = CheckRent(sRent)

            f = open("Report.txt", "a")
            f.write("---Value Report---\n")
            f.write("Generation time: " + reportTime + "\n")
            f.write("\nType of investmetn: " + type + "\n")
            f.write("Type : Property Investment\n")
            f.write("Property price: ", iPrice)
            f.write("Rental income: ", ans[1])
            f.write("Year to be held: ", iYear)
            f.write("Final asset value: ", fTotalAssetValue)
            f.write("APY: ", fAPY)
            f.write("\n\n\n")
            f.close()



        def Cal_InvestProp(iPrice, iYear, iRent):
            fTotalAssetValue = (iPrice * (1 + PROP_RATE) ** iYear) + (iRent * 12 * iYear)
            fAPY = (1 * (1 + PROP_RATE) - 1)
            Output_Label1 = tk.Label(self, text = "Principal: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label1.grid(row = 12, column = 0, sticky = "e")
            Output_Label5 = tk.Label(self, text = iPrice,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label5.grid(row = 12, column = 1, sticky = "w")

            Output_Label2 = tk.Label(self, text = "Years to be held: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label2.grid(row = 13, column = 0, sticky = "e")
            Output_Label6 = tk.Label(self, text = iYear,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label6.grid(row = 13, column = 1, sticky = "w")

            Output_Label3 = tk.Label(self, text = "Final Value: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label3.grid(row = 14, column = 0, sticky = "e")
            Output_Box7 = tk.Entry(self, text = fTotalAssetValue, ## Output with entry widget
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Box7.grid(row = 14, column = 1, sticky = "w")
            Output_Box7.delete(0 , tk.END)
            Output_Box7.insert(0, fTotalAssetValue)
            Output_Box7.config(state= "disabled") ## not allowing users to change the value of it

            Output_Label4 = tk.Label(self, text = "Annual Percentage Yield: ", 
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label4.grid(row = 15, column = 0, sticky = "e")
            Output_Label8 = tk.Label(self, text = fAPY,
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label8.grid(row = 15, column = 1, sticky = "w")

            Output_Label8 = tk.Label(self, text = "(The rental income is exclueded in APY.\nbecause it does not change accroding to the change rate in property price)",
                                     font = ("Arial", 15),
                                     fg="#000000", bg="#ffffff")
            Output_Label8.grid(row = 16, column = 0, sticky = "w")

            recordResults(iPrice, iYear, fTotalAssetValue, fAPY)


        def CheckP(sPrice):
            flag1 = False
            try:
                iPrice = int(sPrice)
                assert iPrice > 0
                flag1 = True
                return flag1
            except AssertionError: ## When the value of Price is not larger than 0, it return a message to user to re-input
                Label_5.grid(row = 4, column = 1)

            except ValueError: ## When the value of Price is not an integer number, it return a message to user to re-input
                Label_6.grid(row = 4, column = 1)


        def CheckY(sYear):
            flag2 = False
            try:
                iYear = int(sYear)
                assert iYear > 0
                flag2 = True
                return flag2
            except AssertionError: ## When the value of Year is not larger than 0, it return a message to user to re-input
                Label_9.grid(row = 6, column = 1)

            except ValueError: ## When the value of Year is not an integer number, it return a message to user to re-input
                Label_10.grid(row = 6, column = 1)


        def CheckRent(sRent):

            if choice.get() == "Yes":
                try:
                    iRent = int(sRent)
                    assert iRent > 0                
                    return True, iRent
                except AssertionError: ## When the value of Rent is not larger than 0, it return a message to user to re-input
                    Label_11.grid(row = 9, column = 1)

                except ValueError: ## When the value of Rent is not an integer number, it return a message to user to re-input
                    Label_12.grid(row = 9, column = 1)

                except TypeError: ## When the value of Rent is not an integer number, it return a message to user to re-input
                    Label_12.grid(row = 9, column = 1)

            else:
                Ent_Rent.delete(0, tk.END)
                Ent_Rent.insert(0, 0)
                iRent = int("0")
                return True, iRent


        def CheckValid():

            Label_5.grid_remove()
            Label_6.grid_remove()
            Label_9.grid_remove()
            Label_10.grid_remove()
            Label_11.grid_remove()
            Label_12.grid_remove()

            sYear = iYear.get() 
            sPrice = iPrice.get()
            sRent = iRent.get()

            CheckP(sPrice)
            CheckY(sYear)
            ans = CheckRent(sRent)

            if CheckP(sPrice) == True and CheckY(sYear) == True and ans[0] == True:
                Cal_InvestProp(int(sPrice), int(sYear), int(ans[1]))


        Btn_Enter = tk.Button(self, text = "Calculate", command = CheckValid, ## Button for calculation
                                bg="#94f8ff", fg="#000000",
                                width = 12, height = 3)
        Btn_Enter.grid(row = 11, column = 1)

        
        def ReturnToMenu():
            controller.show_frame("MenuPage")


        Btn_Return = tk.Button(self, text = "Return To Menu", command = ReturnToMenu, ## Button for returning to the menu
                               bg="#94f8ff", fg="#000000",
                                width = 12, height = 3)
        Btn_Return.grid(row = 17, column = 1)




def main():
    gui = guiApp()
    gui.mainloop()

main()
