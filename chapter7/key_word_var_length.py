def sum_marks(**marks):
    total = 0
    print("Numbers ",marks , 'type ',type(marks))
    for k,v in marks.items():
        total += v
    return total

print("Sum ",sum_marks(myanmar=30,english=40,math=50))

our_marks = {
    "eng":100,
    "math":20,
    "myanmar":30
}
print("Sum ",sum_marks(**our_marks))