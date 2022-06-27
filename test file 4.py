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
