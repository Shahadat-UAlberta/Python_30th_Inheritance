class A:
    def __init__(self):
        self.fatherName = "A"
        print("A Class")

class B:
    def __init__(self):
        self.motherName = "B"
        print("B Class")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

        print("C Class")

    def getDetails(self):
        print(self.fatherName, self.motherName)
        
ob_c = C()

ob_c.getDetails()
