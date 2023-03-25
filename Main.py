import Expense_Tracker as ET
import Import_Methods as IM
individual_expense = ET.Expense()
sheet = ET.Expense_Sheet()

types = (
    'CSV' ,'Excel-NOT WORKING' , 'Google-NOT WORKING'
)


while True:
    func = input('What would you like to do?(add, delete, import, export or view) Enter done when complete: ')
    if func.lower() == 'add':
        date, type, value = individual_expense.create_expense()
        sheet.add(date, type, value)
        print()
    elif func.lower() == 'delete':
        sheet.delete()
        print()
    elif func.lower() == 'view':
        sheet.view()
        print()
    elif func.lower() == 'done':
        break
    elif func.lower() == 'import':
        while True:
            try:
                for x, y in enumerate(types):
                    print(f'{x+1}. {y}')
                type_num = int(input('From the list above what number is the file type? '))
                if type_num < 1 or type_num > len(types): raise ValueError
                break
            except:
                print(f'{type_num} is not valid')
        file_name = input('What is the name of your file? ')
        file_name = file_name.split('.') #allows input to end in .csv or not
        if types[type_num-1] == 'CSV': 
            CSVfile = IM.CSV()
            expenses = CSVfile.importfile(file_name)
            sheet.importfile(expenses)
        print()
    elif func.lower() == 'export':
        while True:
            try:
                for x, y in enumerate(types):
                    print(f'{x+1}. {y}')
                type_num = int(input('From the list above what number is the file type? '))
                if type_num < 1 or type_num > len(types): raise ValueError
                break
            except:
                print(f'{type_num} is not valid')
        file_name = input('What is the name of your file? ')
        file_name = file_name.split('.') #allows input to end in .csv or not
        if types[type_num-1] == 'CSV': 
            CSVfile = IM.CSV()
            expenses = sheet.exportfile()
            CSVfile.exportfile(expenses, file_name)
        print()
    else:
        print('Sorry that is not a choice')
        print()