class A:
    def __init__(self):
        super().__init__()
        print("Class A constructor")

class B:
    def __init__(self):
        super().__init__()
        print("Class B constructor")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("Class C constructor")

obj = C()
