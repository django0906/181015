class User:
    def __init__(self, name):
        self.name = name


class Student(User):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


if __name__ == '__main__':
    aa = Student('Seongeun Yu', 28)
    print(aa.name)
    print(aa.age)

