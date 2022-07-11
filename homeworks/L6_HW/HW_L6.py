
# 1_Make the class with composition: class Laptop, class Battery.

class Laptop:
    def __init__(self):
        self.battery = Battery('Capacity of this battery is huge')


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


laptop = Laptop()
print(laptop.battery.capacity)  # Capacity of this battery is huge


# 2.Make the class with aggregation: class Guitar, class GuitarString.

class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_string = GuitarString()
guitar = Guitar(guitar_string)


# Process finished with exit code 0

# 3_Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static

class Calc:
    @staticmethod
    def add_nums(num1, num2, num3):
        return num1 + num2 + num3


print(Calc.add_nums(7, 21, 27))  # 55


# 4*_Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods: carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']

class Pasta:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        ingredients = ['forcemeat', 'tomatoes']
        return cls(ingredients)

    @classmethod
    def bolognaise(cls):
        ingredients = ['bacon', 'parmesan', 'eggs']
        return cls(ingredients)


pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()
pasta_3 = Pasta.carbonara()
print(pasta_1.ingredients)  # ['tomato', 'cucumber']
print(pasta_2.ingredients)  # ['bacon', 'parmesan', 'eggs']
print(pasta_3.ingredients)  # ['forcemeat', 'tomatoes']


# 5*_Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
# In case of setting visitors_count - max_visitors_num should be checked,
# if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
# Example:
# Concert.max_visitor_num = 50
# concert = Concert()
# concert.visitors_count = 1000
# print(concert.visitors_count)  # 50

class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_num=0):
        self.visitors_num = visitors_num

    @property
    def visitors_count(self):
        return self.visitors_num

    @visitors_count.setter
    def visitors_count(self, x):
        self.visitors_num = min(self.max_visitor_num, x)


Concert.max_visitor_num = 150
concert = Concert()
concert.visitors_count = 200
print(concert.visitors_count)  # 150

# Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str),
# email (str), birthday (str), age (int)
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


python_programming = AddressBookDataClass(key=708,
                                          name='Veronika',
                                          phone_number='+380672317515',
                                          address='Kyiv',
                                          email='ver@gmail.com',
                                          birthday='07/08/1995',
                                          age=26)

print(python_programming)
# AddressBookDataClass(key=708, name='Veronika', phone_number='+380672317515', address='Kyiv',
# email='ver@gmail.com', birthday='07/08/1995', age=26)

# 7_Create the same class (6) but using NamedTuple

from collections import namedtuple

AddressBookNT = namedtuple('AddressBookNT', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

python_programming = AddressBookNT(708, 'Veronika', "+1204857565869", 'Kyiv', 'ver@gmail.com', '07/08/1995', 26)
print(python_programming[4])  # ver@gmail.com
print(python_programming.age)  # 26


# 8_Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
# Make its str() representation the same as for AddressBookDataClass defined above.
# Expected result by printing instance of AddressBook:
# AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')

class AddressBook:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key=\'{self.key}\', name=\'{self.name}\', phone_number=\'{self.phone_number}\', ' \
               f'address=\'{self.address}\', email=\'{self.email}\', birthday= \'{self.birthday}\', age=\'{self.age}\')'


Address_book_1 = AddressBook(708, "Veronica", "9472558375860", "Kyiv", "ver@gmail.com", "7/08/95", 26)
print(Address_book_1)


# AddressBook(key='708', name='Veronica', phone_number='9472558375860', address='Kyiv',
# email='ver@gmail.com', birthday= '7/08/95', age='26')

# 9_Change the value of the age property of the person object

class Person:
    name = "John"
    age = 36
    country = "USA"


person_1 = Person()
person_1.age = 46
print(person_1.age)  # 46


# 10_Add an 'email' attribute of the object student and set its value
# Assign the new attribute to 'student_email' variable and print it by using getattr

class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(708, "Nika")
setattr(student, 'student_email', 'tangryt@ukr.net')
print(getattr(student, 'student_email'))  # tangryt@ukr.net


# 11*_By using @property convert the celsius to fahrenheit
# Hint: (temperature * 1.8) + 32)
# create an object {obj} = ...print({obj}.temperature)

class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


water_temperature = Celsius(22)
print(water_temperature.temperature)  # 71.6

