from typing import overload,Union,Callable
import logging
from enum import Enum,auto


class OrganizationRole(Enum):
    CEO = "ceo"
    PRESIDENT = "president"
    MANAGER = "manager"
    STAFF = "staff"

class SoftwareLanguage(Enum):
    JAVA = auto()
    PYTHON = auto()
    CSharp = auto()

class _DomesticAnimal(object):
    _instance = None
    def __init__(self,breed,source,price):
        self.breed=breed
        self.source=source
        self.price=price
    def display(self):
        animal = None
        if isinstance(self,Cat):
            animal="Cat"
        elif isinstance(self,Dog):
            animal="Dog"
        
        print(f"Hi my {animal} breed is {self.breed},source from {self.source} and the price is {self.price}")


class Dog(_DomesticAnimal):
    def __init__(self,breed,source,price):
        super().__init__(breed,source,price)
    

class Cat(_DomesticAnimal):
    def __init__(self,breed,source,price):
        super().__init__(breed,source,price)


def call():
    dog = Dog("German Shephared","Germany","14000")
    dog.display()

    cat = Cat("British Shorthair","UK","12000")
    cat.display()

def add_2_no(*,a:int, b:int)->int:
    return a+b

@overload
def concat_val(a : str, b: str, c:str) -> str:
    ...
@overload
def concat_val(a:int,b:int,c:int) -> int:
    ...
    
def concrete_call(a : Union[int,str],b : Union[int,str],c: Union[int,str])-> Union[int,str]:
        if isinstance(a,int):
            return a+b+c
        else:
            return a+b+c

def handle_payment(amt:int)-> str:
    val = f"Charging ₹{amt/100:.2f} using payment"
    logging.info(val)
    return val



def order_food(payment_handler : Callable[[int],str]):
    return payment_handler(10)

def main()->None:
    #print(add_2_no(a=5,b=5)) #paramname mandate
    #print(concrete_call(6,6,6)) # Override
    #print(concrete_call("sun","da","r")) # Override
    #print(order_food(handle_payment)) #Callable Function
    my_role=OrganizationRole.PRESIDENT

    print(list(OrganizationRole))
    print(list(SoftwareLanguage))
    

if __name__=="__main__":
    main()