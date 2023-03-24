
import datetime as dt
from decimal import *
import jellyfish
import csv

class Expense_Sheet:
    def __init__(self):
        self.expense_num = 0
        self.expenses = []
        self.file = open('list.txt', 'w')
        self.file.write(f'{"-"*30}\n')

    def add(self,value,type,date):
        self.expense_num += 1
        self.expenses.append({'expense_num': self.expense_num, 'type': type, 'expense': value, 'date': date})
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

    def delete(self, expense_num):
        x = self.expenses.pop(expense_num-1)
        print(f'expense number {expense_num} removed!')
        for y in self.expenses[(expense_num-1):]: y['expense_num'] -= 1  #subtract the expense number int he whole list by 1
        self.expense_num -= 1

    def view(self):
        print('-' * 30)
        print(f"num | type | cost | date")
        if self.expense_num == 0:
            print('No expenses on list!')
        else:
            for x in self.expenses:
                print(f'{x.get("expense_num")}.  {x.get("type")} ${x.get("expense")} {x.get("date")}')
        print('-'*30)

    def close_file(self):
        for x in self.expenses:
                self.file.write(f'{x.get("expense_num")}. {x.get("expense")} -- {"expense complete: True" if x.get("complete") else "expense complete: False"}\n')
        self.file.write('-'*30)
        self.file.close()

class Expense:
    def __init__(self):
        self.types = (
                'housing', 'transportation', 'food', 'utilities', 'insurance', 
                'medical', 'saving', 'investing', 'debt', 'personal',
                'entertainment', 'misc.'
                )
    def create_expense(self):
            
            #Collect type as string with jellyfish module to catch typos and loop for input errors
            def are_types_similar(type): #nested function for typos finding best match from self.types tuple
                    best_match_amt = None #keeping tack of how far off typo is
                    best_string = None #keeping track of best string
                    type = type.lower()
                    for x in self.types:
                        current_difference_off = jellyfish.damerau_levenshtein_distance(type,x)
                        if best_match_amt == None or current_difference_off < best_match_amt:
                            best_match_amt = current_difference_off
                            best_string = x
                    return best_match_amt, best_string
            while True:
                self.type = input(f'\nFrom this list:\n\n1. Housing\n2. Transportation\n3. Food\n4. Utilities\n5. Insurance\n6. Medical \n7. Saving\n8. Investing\n9. Debt\n10. Personal\n11. Entertainment\n12. Misc.\n\nWhich number represents the expense type?: ')
                difference, best_string = are_types_similar(self.type)
                if difference <= 2:
                    self.type = best_string
                    break
                else:
                    print()
                    print(f'{self.type} is not a usable type. Please try again')
                
            #Collect date with Datetime Module
            while True:
                try:
                    self.date = input(f'What was the date of the expense?(mm/dd/yyyy) ')
                    self.date = dt.datetime.strptime(self.date,'%m/%d/%Y')#change to date time
                    break
                except ValueError:
                    print(f'{self.date} is not a valid date. Please enter date in mm/dd/yyyy format')
                    continue
            
            #Collect value with Decimal Module with loop to stop errors
            while True: 
                try: 
                    self.value = input(f'How much was the expense? ')
                    if self.value.startswith('$'): self.value = self.value.strip('$') #Can enter input with $ to start
                    self.value = Decimal(self.value)
                except DecimalException:
                    print('Please enter a number')
                    continue
                self.value = self.value.quantize(Decimal('0.00'), rounding=ROUND_UP) #Using Decimal Modual to make more readable
                print(self.value)
                break
        
            sheet.add(self.value,self.type,self.date.date())
            

class ExpenseRun:
    def start(self):
        self.func = ''
        while True:
            self.func = input('What would you like to do?(add, delete or view) Enter done when complete: ')
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
                sheet.close_file()
                break
            else:
                print('Sorry that is not a choice')
individual_expense = Expense()
sheet = Expense_Sheet()
start = ExpenseRun()
start.start()


