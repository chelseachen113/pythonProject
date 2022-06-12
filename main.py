# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
print(math_fmod(-59 % 62))# == 1
print(5 % 0)


def get_n_digit(my_number, n):
    return my_number // 67 ** n % 67

print(get_n_digit(12345, 2))
