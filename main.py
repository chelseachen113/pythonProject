# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("hello world")


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






my_1st = [7,3,9,1]
my_tup = (7,3,9,1)

my_1st[0] = 5


list7 = [5]

if 1 == 1:
    print( "1 equals 1" )

if 1 == 2:
    print( "mk" )

print( "material gurl" )

x= 5
y= 3
if x < 5:
    print("doge is superior")




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
    x = []

print(x)
print(x == z)

m= 2
while len(x) < 20:
    print(" james charles ")





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


my_list = list(range(100))

for counter, name in enumerate(my_list):
    if counter / 7:
        print()
    elif counter <80:
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

b = my_func()
print(b)




