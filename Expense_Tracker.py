
import datetime as dt
from decimal import *

class Expense_Sheet:
    def __init__(self):
        self.expenses = []
    def add(self,date, type, value):
        self.expenses.append({'type': type, 'expense': value, 'date': date})
        print('expense added')
        while True: #loop to quickly add more expenses
            prompt = input('Would you like to add another expense? ')
            if prompt.lower() == 'yes':
                individual_expense.create_expense()
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

#old code want to test on Main.py
if __name__ == '__main__':
    class ExpenseRun:
        def start(self):
            self.func = ''
            while True:
                self.func = input('What would you like to do?(add, delete, import, export or view) Enter done when complete: ')
                if self.func.lower() == 'add':
                    individual_expense.create_expense()
                elif self.func.lower() == 'delete':
                    sheet.view()
                    print()
                    expense_num = int(input('Which expense number would you like to delete?: '))
                    sheet.delete(expense_num)
                elif self.func.lower() == 'view':
                    sheet.view()
                    print()
                elif self.func.lower() == 'done':
                    break
                elif self.func.lower() == 'import':
                    sheet.importcsv()
                    print()
                elif self.func.lower() == 'export':
                    sheet.exportcsv()
                    print()
                else:
                    print('Sorry that is not a choice')
    individual_expense = Expense()
    sheet = Expense_Sheet()
    start = ExpenseRun()
    start.start()

print('test')



