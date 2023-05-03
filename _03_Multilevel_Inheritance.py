class A:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class B(A):

    def __init__(self, name, age):
        A.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age


class C(B):
    def __init__(self, name, age, country):
        B.__init__(self, name, age)
        self.country = country

    def getCountry(self):
        return self.country


ob_c = C("Mahmud", 50, "BD")

print(ob_c.getName(), ob_c.getAge(), ob_c.getCountry())
