
import datetime as dt
from decimal import *

class Expense_Sheet:
    def __init__(self):
        self.expenses = []
        self.keys = ('date', 'type', 'value')
    def add(self,date, type, value):
        self.expenses.append({'type': type, 'expense': value, 'date': date})
        print('expense added')
        while True: #loop to quickly add more expenses
            prompt = input('Would you like to add another expense? ')
            if prompt.lower() == 'yes':
                Expense.create_expense()
            elif prompt.lower() == 'no':
                break
            else:
                print(f'{prompt} is not a valid option')
                continue

    def delete(self):
        while True:
            try:
                self.view()
                expense_num = int(input('Which expense number would you like to delete?: '))
                if expense_num > len(self.expenses) or expense_num <= 0: raise ValueError
                break
            except ValueError:
                print(f'{expense_num} is not a valid number on the list. Pleae try again')
        self.expenses.pop(expense_num - 1)
        print(f'Expense number {expense_num} removed')
    def view(self):
        print('-' * 30)
        print(f"num | date | type | value")
        if len(self.expenses) == 0:
            print('No expenses on list!')
        else:
            # go through expense list return a enumerate value to get expense number shown
            for expense_num, expense_dict in enumerate(self.expenses):
                print(f'{expense_num+1}.  {(expense_dict.get("date"))} {expense_dict.get("type")} ${expense_dict.get("expense")}')
        print('-'*30)
    
    #import CSV file to self.expense
    def importfile(self, expenses):
        self.expenses = expenses

    def exportfile(self):
        return self.expenses
    
    def select_expense(self):
        def select_item():
            while True:
                try:
                    self.view()
                    expense_num = int(input('Which expense would you like to edit? '))
                    if expense_num < 1 or expense_num > len(self.expenses): raise ValueError
                    expense = self.expenses.pop(expense_num-1)
                    break
                except ValueError:
                    print(f'{input} is not a valid option')
        
        def select_category():
            while True:
                try:
                    for num, i in enumerate(self.keys): print(f'{num+1}. {i}')
                    type = int(input('Which category would you like to change? '))
                    if type < 1 or type > len(self.keys): raise ValueError
                    key = self.keys[type-1]
                    break
                except ValueError:
                    print(f'{input} is not a valid option')
        expense_tuple = (select_item, select_category)
        return expense_tuple

class Expense:
    def __init__(self):
        self.types = (
                'Housing', 'Transportation', 'Food', 'Utilities', 'Insurance', 
                'Medical', 'Saving', 'Investing', 'Debt', 'Personal',
                'Entertainment', 'Misc.'
                )
        
    def create_expense(self):
        return  self.input_date(),self.input_type(), self.input_value()
    
    def input_type(self):
        for num, type in enumerate(self.types):
            print(f'{num+1}. {type}')
        while True:
            try:
                type_num = int(input(f'Which numbered item describes the type of expense? '))
                if type_num > len(self.types): raise ValueError
                break
            except:
                print(f'{type_num} is not a usable type. Please try again')
                continue
        return self.types[(type_num-1)]
            
    def input_date(self):
        while True:
            try:
                date = input(f'What was the date of the expense?(mm/dd/yyyy) ')
                date = dt.datetime.strptime(date,'%m/%d/%Y')#change to date time
                date = date.date()
                break
            except ValueError:
                print(f'{date} is not a valid date. Please enter date in mm/dd/yyyy format')
                continue
        return date
            
    def input_value(self):
        while True: 
            try: 
                value = input(f'How much was the expense? ')
                if value.startswith('$'): value = value.strip('$') #Can enter input with $ to start
                value = Decimal(value)
                break
            except DecimalException:
                print('Please enter a number')
                continue
        return value.quantize(Decimal('0.00'), rounding=ROUND_UP) #Using Decimal Modual to make more readable

class EditedExpense(Expense):
    def edit_expense(self, type):
        if type == 'date': return self.input_date()
        if type == 'type': return self.input_type()
        if type == 'value': return self.input_value()


        


        



