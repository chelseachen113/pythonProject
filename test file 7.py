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

my_list = ["7", "9", "2", 1, 4]
print(my_list)

for n in my_list:
    if n == "2":
        break
    print(n)

my_list = ["6", "7", "9", "27"]

for counter, name in enumerate(my_list):
    if counter / 3:
        print(name)

def my_func():
    print("chelsea")
my_func()
my_func("Hello, George >:)!")
my_func("Hello, George >:)!")
my_func("Hello, George >:)!")

a= 4
def dis_func():
    return("MANY")
    return("MAY")
    return("MUCHO")
dis_func = a
print(a)

def my_func():
    return 4,6,8

b = my_func():
    print(b)



