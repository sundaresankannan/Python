def func(f):
    def wrapper(*arg,**kwarg):
        print("Started")
        rv = f(*arg,**kwarg)
        print("Ended")
        return rv

    return wrapper

@func
def func1(a):
    return "This is my exact function 1"," value:",a

@func
def func2():
    return "This is my exact function 2"

a = func1(12)
b= func2()
print(a)
print(b)
