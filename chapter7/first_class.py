#Rule 1 , can be stored in variable
#Rule 2, can be passed as parameter.
#Rule 3, can be returned from function
def get_another():
    print("Invoked get another")
    return hello
def invoke(func):
    print("Invoked called ")
    func()
    
def hello():
    print ("Hello called")
x = hello #Rule 1
invoke(hello) # Rule 2

get_another()()