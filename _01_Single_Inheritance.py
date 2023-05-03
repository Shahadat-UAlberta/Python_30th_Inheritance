"""

## Inheritance

- Reusability

"""

# 01_ Single Inheritance

# Parent Class
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(self.name)
        print(self.age)

# Child Class
class B(A):

    def __init__(self, name, age, salary, designation):
        self.salary = salary
        self.designation = designation

        A.__init__(self, name, age)

    def display_details_B(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        print(self.designation)


b = B("Mahmud", 50, 1000, "SDE")

b.display_details_B()

