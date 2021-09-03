counter = 0
total = 0
while counter <= 100:
    if counter%10 == 0:
        print("counter ",counter)
        total += counter
    counter += 1
print("Total ",total)