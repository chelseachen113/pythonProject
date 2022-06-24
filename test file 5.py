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

