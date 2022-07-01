# PythonProject
This is Chelsea's python project for exploration




## Development Process
1. Start new exploring / research in the test_sandbox
2. Cleanup test_sandbox according to coding standards
3. Make sure all tests pass in the test_sandbox
4. Move all functions and tests from test_sandbox into sensibly named files
5. Delete all functions and tests from the test_sandbox that were moved in step 4



## Coding Standards

### Variable Naming
1. start with lowercase letter, use _ in between words
2. use useful words that describe what is inside the variable
3. avoid abbreviation
4. use the modified hungarian notation below
##### Modified hungarian notation
https://en.wikipedia.org/wiki/Hungarian_notation  
string - str_  
a string is a data type that is a word in quotes  
example: "string"

integer - int_  
a integer is a number  
example: 4

float - flt_  
a float is a data type that deciphers the number with decimal or fraction  
example: 4.657

list - lst_  
a list is items in curvy braces, and square brackets separated by commas  
example:["ok", 6, "dgsd"]

boolean - bool_is_  
a boolean is a true/false data type  
example: true/false

dict - dict_%keys%_to_%values%  
a dict put items and sort
example:  {name:"dklsjf", age:345678}

tuple - tpl_  
a tuple is strings in parentheses separated by commas  
example: ("word", "wfaioshf")

range - rng_  
range is a function that uses numbers 
example: [1, 2, 3, 4, 5]
#### Data Types
https://realpython.com/python-data-types/

### Function Naming
1. Starts with uppercase letter
2. Try to use full words, not abbreviations

### Test Naming
1. Follow format below
2. def test_%scenario%_equals_%value%
3. example: def test_x_equals_seven

### Assertion Format
1. use self.assertEqual with a hard coded value as first argument and a variable as the second
2. example self.assertEqual("2",str_actual_value)
3. example2: self.assertEqual(5,int_value)