import csv

with open("data.csv","r",newline='') as file:
    reader = csv.reader(file)
    data = list(reader)
    for item in data:
        print("Item ",item)
    
print("Writing done")