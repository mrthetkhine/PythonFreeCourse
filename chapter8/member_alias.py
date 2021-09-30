import importlib
import calculator
importlib.reload(calculator)
from calculator import add as sum
print("add ",sum(10,20))

