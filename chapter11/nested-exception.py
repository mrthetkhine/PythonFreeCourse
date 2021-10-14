try:
    print("Outer block")
    try:
        print("10/0 ",10/1)
    except:
        print("Inner Exception ")
    else:
        print("Inner Ok ")
    finally:
        print("Inner Finally ")
except:
    print("Outer Exception")
finally:
    print("Outer Finally ")