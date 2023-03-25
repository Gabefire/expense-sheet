import Expense_Tracker as ET
individual_expense = ET.Expense()
sheet = ET.Expense_Sheet()
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
        sheet.importcsv()
        print()
    elif func.lower() == 'export':
        sheet.exportcsv()
        print()
    else:
        print('Sorry that is not a choice')
        print()