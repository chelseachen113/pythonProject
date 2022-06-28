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
integer - int_  
float - flt_  
list - lst_  
boolean - bool_is_  
dict - dict_  
tuple - tpl_  
range - rng_  
#### Data Types
https://realpython.com/python-data-types/

### Function Naming
1. Starts with uppercase letter
2. Try to use full words, not abbreviations

### Test Naming
1. Follow format below
2. def test_scenario_equals_value
3. example: def test_x_equals_seven

### Assertion Format
1. use self.assertEqual with a hard coded value as first argument and a variable as the second
2. example self.assertEqual("2",str_actual_value)
3. example2: self.assertEqual(5,int_value)