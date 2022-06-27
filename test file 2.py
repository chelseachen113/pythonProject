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
