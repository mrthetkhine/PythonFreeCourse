import csv

with open("data.csv","a",newline='') as file:
    writer = csv.writer(file)
    id = int(input("Enter id "))
    name = input("Enter name ")
    school = input("Enter school ")
    writer.writerow([id,name,school])
    
print("Writing done")