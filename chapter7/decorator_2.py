def trim_str(fn):
    print("Trim")
    def inner(msg):
        return fn(msg.strip())
    return inner

def check_none(fn):
    print("Check_none fn =>",fn)
    def inner(msg):
        if msg != None:
            return fn(msg)
        else:
            return ""
    return inner
    
  
@check_none
@trim_str  
def append_hi(msg):
    return msg + " hi"

@check_none
def to_upper(msg):
    return msg.upper()
print("append_hi=>", append_hi(" hello "), "<=")
print("append_hi ", append_hi(None))