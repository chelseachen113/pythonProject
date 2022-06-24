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

