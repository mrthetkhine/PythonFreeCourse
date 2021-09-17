marks = {
    "Myanmar":40,
    "English":50,
    "Math":60,
}
key = "Myanmar"
value = marks.get(key,0)
print("Key => ", value)

marks["Myanmar"] = 60
print("Marks ",marks)

del marks["Myanmar"]
print("Marks ",marks)

#del marks["Myanmar"]
print("Marks key ",marks.keys())

print("Marks value ",marks.values())

for k in iter(marks):
    print("Key ",k)
    
new_dict = dict.fromkeys(iter(marks),[10,20])
print("New Dict " ,new_dict)

