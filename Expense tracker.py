from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Expense tracker") #Creates a title for the app window
root.geometry('350x200') #Sets the geometry for the window


incomelbl = Label(root, text = "Enter your income")
incomelbl.grid(column = 0, row = 0)
income = Entry(root, width= 10) #Settings for the text box
income.grid(column = 1, row = 0)

incomeNum = 0


incomeText = Label(root, text = incomeNum)
incomeText.grid(column = 1, row = 3)

expenseText1 = Label(root, text = "Enter expense name")
expenseText1.grid(column = 0, row = 1)
expenseName = Entry(root, width= 10, text = "Enter name") #Settings for the text box
expenseName.grid(column = 1, row = 1)

expenseText2 = Label(root, text = "Enter expense amount")
expenseText2.grid(column = 0, row = 2)
expenseNum = Entry(root, width= 10, text = "Enter amount") #Settings for the text box
expenseNum.grid(column = 1, row = 2)



expenseItem = 4 #Placements for the expense items




def addIncome():
    newIncome = income.get()
    if newIncome.isnumeric():
        incomeText.configure(text = int(newIncome))
        global incomeNum
        incomeNum = incomeNum + int(newIncome)
    else:
        messagebox.showwarning("Value Warning", "Please use numeric values only")

def addExpense():
    newExpenseName = expenseName.get()
    newExpenseNum = expenseNum.get()
    global incomeNum
    global expenseItem

    if newExpenseNum.isnumeric():
        expenseNumLabel = Label(root, text = int(newExpenseNum))
        expenseNumLabel.grid(column = 1, row = expenseItem)
        expenseNameLabel = Label(root, text = newExpenseName)
        expenseNameLabel.grid(column = 0, row = expenseItem)
        incomeText.configure(text = incomeNum - int(newExpenseNum))
        incomeNum = incomeNum - int(newExpenseNum)
        expenseItem = expenseItem + 1
    else:
        messagebox.showwarning("Value Warning", "Please use numeric values only")
        
    


add_expense = Button(root, text = "Add expense", command = addExpense) #Add button settings
add_expense.grid(column = 2, row = 2)

add_income = Button(root, text = "Add income", command = addIncome) #Add button settings
add_income.grid(column = 2, row = 0)

TotalLbl = Label(root, text = "Total you have left:")
TotalLbl.grid(column = 0, row = 3)



root.mainloop()
