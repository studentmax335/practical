class Demo:
    def __init__(self):
        print("Constructor called: Object created")

    def __del__(self):
        print("Destructor called: Object destroyed")

# Creating and deleting an object
obj = Demo()
del obj
