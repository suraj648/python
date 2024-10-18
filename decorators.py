
def decorator(func):
    def wrapper():
        print("Hello")
        func()
        print("Hope you are doing okayy :) ")
    return wrapper

@decorator
def greet():
    print("good afternoon")

greet()