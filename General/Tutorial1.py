import inspect
from queue import Queue

def make_class(x):
    class TestClass:
        def __init__(self,name):
            self.name=name
        def print_val(self):
            print(x,self.name)
        
    return TestClass

t = make_class(10)
print(t)
d =t("sundar")
d.print_val()
#print(inspect.getsource(Queue))