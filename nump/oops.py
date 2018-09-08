class User:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printo(self):
        print(f'ur name is {self.name} salary is {self.salary}')


user1 = User('hello', 4000)
user1.printo()