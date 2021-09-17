marks = {
    "Myanmar":40,
    "English":50,
    "Math":60,
}
print("Marks ",marks)

for ele in marks:#key
    print("Element ",ele, " marks ",marks[ele])

for key,value in marks.items():
    print("Key ",key, " => ",value)
    
print("Items ", marks.items())
print("List ", list(marks))