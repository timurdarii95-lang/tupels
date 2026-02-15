class User:
    def __init__(self):
        self.__name = 'Ionel'
        self.__password = "1234"

    def say_hello(self):
        print('hello')

    def get_name(self):
        return self.__name

u = User()
u.say_hello()
#print(u._name) # nu e recomandat, dar avem acces
print(u.get_name())  # cu private, trebuie sa folosim un getter
