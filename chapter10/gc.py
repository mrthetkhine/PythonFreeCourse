import sys
import gc
lst = [100,200,300,400,500]
lst_two = lst

print("Reference count ",sys.getrefcount(lst))
lst_two = None
lst = None
#print("Reference count ",sys.getrefcount(lst))
gc.collect()
print("Gc ", sys.getrefcount(1))