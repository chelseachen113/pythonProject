import unittest
import main.py

# Initialize a class to use with unittest framework
class main(unittest.TestCase):

    # Test the hello world function from hello.py
    def testHelloWorld(self):
        # check whether the 'hello world' is returned by the method
        self.assertEqual(main.py(), 'main.py')

if __name__ == '__main__':
    unittest.main()

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hello world")

y = 2
print(y % 6)

x = 9
x *= 5
print(x)

x = 23
print(x % 2 == 0)
y = 78
print(y % 7 == 0)
import decimal

print(decimal.Decimal('0.5') % decimal.Decimal('0.1'))
print(-59 % 62)  # == 1


def get_n_digit(my_number, n):
    return my_number // 67 ** n % 67

print(get_n_digit(12345, 2))

# This is a sample Python script.
print("a")
print(ord("a"))
print("this is line four code")
def encrypt(text, shift):
    ascii_int=ord(text)
    new_ascii=ascii_int+ shift
    new_text=chr(new_ascii)
    print(new_ascii)
    print(new_text)
print("this is line eleven in code")
encrypt("a",6)
encrypt("a", 1)
encrypt("g", -2)



x=3
print(x)
y="twenty five"
print(y)
type(y)

x=8
print(x)
type(x)

x=8.8
print(x)
type(x)

print("is 9 equals to 5?", 1==2)

type(1==1)

if 9:
    print(9)
if 5:
    print(5)

quote = "We know what we are, but know not what we may be."
print(quote)

#Using start, stop
print(quote[:3])
print(quote[:45])

quote = "We know what we are, but know not what we may be."

print(quote[:10])



quote = "We know what we are, but know not what we may be."
print(quote[:12])

our_list = ["house", "grass", "dog", "tree"]
print(our_list)
our_list. remove("house")

our_list = [""]
print(our_list)
our_list. append("doge")
our_list. append("serene doge")
our_list. append("most serene doge")
print(our_list)
our_list. remove("doge")
print("serene doge, most serene doge")
print("doge")

my_list: list[str] = ["python", "python", "python", "python", "python", "tutorial"]
print(my_list)
my_list.remove("tutorial")

my_set = {"n", "o", "h"}
print(my_set)

doge_set = {"he", "hello", "hell"}
print(doge_set)

doge_set.discard("hell")
print(doge_set)

egg_dog_set = {"k", "ok", "okay"}
doge_set = {"he", "hello", "hell"}

dif_set = egg_dog_set.difference(doge_set)
print(dif_set)

my_list = [doges, drum, dam, does]
my_frozenset = frozenset(my_list)
he_list = [latish, lamish, lamba, lando]
my_frozenset = frozenset(he_list)
she_list = [matish, mamish, mamba,mamdo]
my_frozenset = frozenset(she_list)
e_list = [atish, amish, amba, ando]
my_frozenset = frozenset(e_list)
print(my_frozenset)



my_1st = [7,3,9,1]
my_tup = (7,3,9,1)

my_1st[0] = 5
my_tup[0] = 5

list5 = [5]
list7 = [5]

print(list5 is list7)
print(list5 == list7)

if 1 == 1:
    print( "1 equals 1" )

if 1 == 2:
    print( "mk" )

print( "material gurl" )

x= 5
y= 3
if x < 5:
    print("doge is superior")



