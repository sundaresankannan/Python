class Users(object):
    def __init__(self,fname,lname,email,phone):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.phone=phone

    @property
    def getName(self)->str:
        return self.fname+" "+self.lname
    


def main():
    user01=Users("Sundaresan","kannan","skannan@gmail.com","9445544900")
    print(user01)
    print(f"User : {user01.getName}")

if __name__ == "__main__":
    main()
