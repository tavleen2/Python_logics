def logger(func):
    def wrapper():
        print("function is being called")
        func()
    return wrapper

@logger
def say_heloo():
    print("hello")

say_heloo()