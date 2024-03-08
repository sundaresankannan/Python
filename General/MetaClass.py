"""
__new__
__call__

"""

from object_python import _DomesticAnimal

class Meta(type):

    def __new__(self,class_name,bases,attrs):
        attrs['added'] = 'New'
        for name,val in attrs.items():
            print(name,val)
        return  type(class_name,bases,attrs)
        

class Dog(metaclass=Meta):
    x=8
    y=6
    def hello(self):
        print("hello")


d = Dog()
a = Dog()
print(d,a)


print(_DomesticAnimal._instance)