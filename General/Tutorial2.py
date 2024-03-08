class Person:
    def __init__(self,name) -> None:
        self.name=name
    
    def __repr__(self) -> str:
        return f"{self.name}"
    
    def __mul__(self,x):
        if type(x) is not int:
            raise Exception("Invalid arguments, must be int")
        self.name = self.name * x

p = Person("Sundaresan")
p*2
print(p)