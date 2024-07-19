class User:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.count += 2

    def __str__(self):
        return f'{self.name, self.age}'

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def up_age(self):
        self.age += 1
        return self.age


u = User('Vasiliy', 1)

print(u.up_age())

print(u)