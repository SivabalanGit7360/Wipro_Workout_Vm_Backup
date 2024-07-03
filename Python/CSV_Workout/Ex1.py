# csv.reader - fileobject as arugument and return a list of list
import csv
def csv_reader(fileobject):
    records = csv.reader(fileobject)
    for record in records:
        print(' '.join(record))
        
def csv_dict_reader(fileobject):
    records = csv.DictReader(fileobject)
    for record in records:
        print(record['first_name'], record['last_name'])
        
if __name__ == "__main__":
    with(open("CSV_Workout/uk-500.csv","r")) as fh:
        csv_reader(fh)