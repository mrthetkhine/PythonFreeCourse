digit = '012'
char_string = 'ABC'
special_char = '@#$#'

for d in digit:
    for c in char_string:
        for s in special_char:
            print('Password ', d+c+s)
print("end of nested loop")