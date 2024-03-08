"""
These classes hold certain properties and functions to deal specifically with the data and its representation.
Without a __init__() constructor, the class accepted values and assigned it to appropriate variables.
The output of printing object is a neat representation of the data present in it, without any explicit function coded to do this. That means it has a modified __repr__() function.
"""

from dataclasses import dataclass

@dataclass
class Users(object):
    fname : str
    lname : str
    email : str
    phone : str

    @property
    def getName(self)->str:
        return self.fname+" "+self.lname
    


def main():
    user01=Users("Sundaresan","kannan","skannan@gmail.com","9445544900")
    print(user01)
    print(f"User : {user01.getName}")

if __name__ == "__main__":
    main()
