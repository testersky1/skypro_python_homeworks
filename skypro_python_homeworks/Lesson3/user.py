class User:
    first_name = "__Имя__"
    last_name = "__фамилия__"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getName(self, first_name):
        print(f"Меня зовут {first_name}")

    def getSurName(self, last_name):
        print(f"Моя фамилия {last_name}")

    def allName(self, first_name, last_name):
        print(f"А если кто не понял, то вместе я {last_name} {first_name}")
