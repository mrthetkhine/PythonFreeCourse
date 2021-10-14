print("Start")

try:
    a = int(input("Enter a "))
    b = int(input ("Enter b "))
    print("10/0 ",a/b)
    print("After exception line")
#except (ZeroDivisionError,ValueError):
#    print("Error when division by zero or value error")
except ValueError:
    print("Please enter number value")
except:
    print("Error occur but I have no idea what erorr it is")
finally:
    print("That is run what happened")
print("End of line")