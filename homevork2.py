# class Student:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 2
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
#
# student1 = Student("Amirolimxon", "Alimboyev", 2003)
# print(student1.get_info())


#-2

class Student:
    def __init__(self, ism, familiya, tyil, email):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 2
        self.gmail = email
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi {self.gmail}"

student1 = Student("Amirolimxon", "Alimboyev", 2003, "azizbekyusupov3120@gmail.com")
print(student1.get_info())