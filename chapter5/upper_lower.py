str = "applE orange banana "

new_str = str.upper()
print("Upper ",new_str)

print("lower ",str.lower())
print("swap ",str.swapcase())
print("title ",str.title())
print("capitalize ",str.capitalize())

print("str.startwith ",str.startswith("appl"))
print("str.endwith ",str.strip().endswith("banana"))

num_str = input("Enter num ")
while not num_str.isdigit():
    num_str = input("Please enter num ")
num = int(num_str)
print("Number is ",num)
