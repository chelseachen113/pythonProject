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

if True:
    pass

print('1234567890')

x=6
if x > 5:
    print('slay queen')

y=5
if y > 6:
    print('YAS GURL')
elif y < 7:
    print('car max car insurance')
else:
    print('GROCERY MAGGOT BARNS AND MARGRET')

x = "AeA DANCING IN SEPTEMBER" if 4 > 2 else "HeLo"
print(x)

my_list = [1, 2, 3, 4]
y = my_list if 2 in my_list else []
print(y)

z = my_list if 7 in my_list else []
print(z)

my_list = [1, 2, 3, 4]

z = my_list if 7 in my_list else []

if 7 in my_list:
    x = my_list
else:
    x = [SHUASHEE]

print(x)
print(x == z)

m= 2
while x < 20:
    print(" james charles ")
