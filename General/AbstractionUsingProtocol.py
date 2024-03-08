from dataclasses import dataclass
from typing import Protocol


"""
This is the good abstraction using the protocol,
 but when we use the LoginDtl with only loginid and password it prints
 but even we can use the other name variable with the respective name.
"""

@dataclass
class UserMaster(object):
    fname : str
    lname : str
    loginid : str
    password : str
    isactive : str


class LoginDtl(Protocol):
    @property
    def loginid() -> str:
        ...

    @property
    def password() -> str:
        ...

def display(login : LoginDtl , show_active: bool = False) -> str:
    ret_val = f"login ID is {login.loginid} and password is {login.password}"
    if show_active:
        ret_val = ret_val + f" and the user active status is {login.isactive}" # this we have not declared but still can be used

    return ret_val

def main():
    user = UserMaster("sundar","kannan","skannan","sund1234","Y")
    print(display(user))
    print(display(user,True))   


if __name__=="__main__":
    main()