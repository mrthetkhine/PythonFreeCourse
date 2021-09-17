marks = {
    "Myanmar":40,
    "English":50,
    "Math":60,
}
key = "Myanmar1"
value = marks.pop(key,0)
print("Key => ", value)

print("Key ", marks.setdefault(key,100))
print("Marks ",marks)
for item in reversed(marks):
    print("Item ",item)

print("Marks popitem",marks.popitem())

marks.update(bio=40,chem=50)
print("After update ",marks)
