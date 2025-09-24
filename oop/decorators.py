def decorator(func):  #decorator takes a func, creates a new func inside it and returns that new func 
    def wrapper():
        print("I am about to print Hello....")
        func()     #it refers to any function passed to the decorator
        print("I have excuted the function...")
    return wrapper

@decorator  #this is equivalent to say_hello = decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()
# f = decorator(say_hello)
# f()  #calling the wrapper function returned by the decorator