import csv
class FileType:
    def __str__(self):
        file_name = input('What is the name of your file? ')
        self.file_name = file_name.split('.') #allows input to end in .csv or not
        return self.file_name[0]
    def importfile(self, file_name):
        while True: #making sure the file can be opened
            try:
                file_hand = open(file_name)
                return file_hand
            except FileNotFoundError:
                print(f'{file_name} not found')
                continue

class CSV(FileType):
    def importfile(self, file_name):
        file_name = f'{file_name[0]}.csv'
        while True: #making sure the file can be opened
            try:
                with open(file_name, 'r') as file_hand:
                    csv_reader = csv.DictReader(file_hand)
                    expenses = [i for i in csv_reader]
                    #need to make this check the keys
                    print(f'{file_name} imported')
                    return expenses
            except FileNotFoundError:
                print(f'{file_name} can not be opened!')

    #export CSV file
    def exportfile(self, expenses, file_name):
        file_name = f'{file_name[0]}.csv'
        while True: #making sure the file can be opened
            try:
                with open(f'{file_name}', 'w') as csv_file:
                    fieldnames = ['type', 'expense', 'date']
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    [csv_writer.writerow(i) for i in expenses]
                    print(f'{file_name} exported')
                    break
            except FileNotFoundError:
                print(f'{file_name} can not be opened!')