"""

Part 1 - Python Introduction


  Instructor      :
  Course Name     :
  Course Length   :
  Description     : 
                    Learn the building blocks of the wonderful general purpose programming language Python
  Audience        :
  Course Syllabus :

"""


"""

Python in Industry

  In Google Python is one of the primary language
  Honeywell uses Python for generating documentation  
  Maya uses python for scripting 
  GIS heavy uses python for scripting 
  US Govt does statistical analysis and Data Visualisation 
  Disney/Pixar Films uses to provide more realistic effect in movies
  Youtube, Instagram, Reddit, Pinterest power their CMS ( Content Management System )
  Facebook uses a lot for internal scripting  
  Face/Speech Recognition
  Controlling Robots and Automation ( MicroPython )
  Data Scientist uses Anaconda with more than 400 packages for science, math, engineering and data analysis

History of Python

  Easy as ABC ( developed at Centrum Wiskunde & Informatica, Netherlands)
  1991 by Guido van Rossum, 
  British Comedy Troupe - Monty Python Flying Circus
  The Zen of Python (19)  


Fundamentals of Python 
  General Purpose Dynamic Compiled Language, OOPS, Interpreted, Functional , Procedural , Library
  Difference between INTERPRETED and COMPILED language
  C is STATISTICALLY typed language so needs to be compiled before using.


Installation of IDLE
  Checking the verison of python installed using ( python -- version)
  Check the installation PATH of python 
  (which -a python) (which -a python2) (which -a python3)
  The Terms "Interactive" and "Shell"
  Starting the Python Shell from CMD or TERMINAL ( python )
  REPL ( Read Evaluate Print Loop )is the best environment to learn a language
  Starting Python Shell using IDLE ( Spotlight Search or Windows Search ) 
  How to Quit the Python Shell using quit() or exit() or CRTL+D

"""

#Python Shell as a Calculator (Trainer Hands On)
2 + 2
2 - 2
2 * 2
2 / 2 
#( Ver 2 always return integer value but ver 3 returns float)


#Printing on the Console (Trainer Hands On)
print ("Hello World")

"""
Literals using primitive data types
  Numeric ( int/long)
    4
  Floating Point ( float )
    10.6
  String ( str )
    "Hello World"
  Boolean ( bool )
    True False
  NoneType ( None )
    None

"""


#How to check the data type of a literal (Trainer Hands On)
type (4)

type (10.6)

type (True)
type (False)

type ('FORSK')
type ("FORSK")
type ('''FORSK''')
type ("""FORSK""")

type ( None )


"""
Type Conversion using Global Functions  
  int()
  float()
  str()
  bool()
"""


#How to convert the data type (Trainer Hands On)
int (4)
int (10.6)
int ("10")
int (True)


float (4)
float (10.6)
float ("10")
float (True)


str (4)
str (10.6)
str ("10")
str (True)



bool (4)
bool (10.6)
bool ("10")
bool (True)

 
bool (1)
bool (0)
bool (True)
bool (False)


#Single Line Commenting (Trainer Hands On)
#Using HASH or POUND ( # ) 

"""
How to store data in Python variables 
  Variable is like a Box and you put a literal in it 
  Literal can be of any above types
  Introduce the concept of Heap and Stack
  Python variables in Stack are references to objects in Heap
  Actual data is contained in the object

  Example for explanation with visual 
    x = 42
    y = x

    y = 78

    x = "hello"

  Identity function id() can be used to find the unique identity of the objct it is pointing to 

    x = 42
    id(x)

    y = x
    id(y)

    y = 78
    id(y)

    x = "hello"
    id(x)

"""
  
"""
Naming Convention (Trainer Hands On)
  Valid characters for variable names
    "A" through "Z", 
    "a" through "z" , 
    underscore _ and, except for the first character, 
    digits 0 through 9. 
  
  Variable names and identifier names can additionally contain Unicode characters as well.

 """

8p = "FORSK"   
!p = "FORSK"
$p = "FORSK"
# Cannot start with a number, Exclamation and $ sign

p!p = "FORSK"
p$p = "FORSK"
# Cannot have a Exclamation or  $ sign or any other special characters

p8 = "FORSK"
# Can have numbers within

+p = "FORSK"
-p = "FORSK"   
*p = "FORSK"
/p = "FORSK"
# Cannot start with or have any Arithmetic Operators
  

for = "FORSK"   
print = "FORSK"
# Cannot use keywords used in python syntax
# and, as, assert, break, class, continue, def, del, elif, else,
# except, False, finally, for, from, global, if, import, in, is, 
# lambda, None, nonlocal, not, or, pass, raise, return, True, try, 
# while, with, yield

# help()  and then type "keywords" to get the list


_for = "FORSK" 
# _ is the only special character which is allowed

my age  = 40  
# Space is not allowed between the variable names

my_age = 40 
# underscore is the best way to have long variable names

"""
Best Practice for Naming Convention
  # Discuss UPPERCASE, lowercase and CamelCase way of naming the variables
  # Never use the characters 'l' (lowercase letter "L")
  # Never use the characters  'O' ("O" like in "Ontario")
  # Never use the characters 'I' (like in "Indiana") 
  # as single character variable names.
"""


#Printing Output of a variable on console (Trainer Hands On)
print ( my_age )


#One variable can hold different data type (Trainer Hands On)
# Integer
my_var = 8
type(my_var)

# Float
my_var = 26.5
type(my_var)
  
# String
my_var = "FORSK"
type(my_var)
  
# Boolean
my_var = True
type(my_var)
  
# NoneType
my_var = None
type(my_var)


#Understanding Error Messages in Python (Trainer Hands On)
#NameError happens when something does not exists
5 + x

#TypeError happens when there is data type mis match
5 + "a"
#Solution to convert the 5 using the str function to string first and then use it
str(5) + "a"
  
#Syntax Error 
print("Hello)


#Arithmetic Operator  

#+ Addition
5 + 5 

#- Subtraction
5 - 5

#* Multiplication 
5 * 5

#/ Division   
5 / 5

#Ver 2 always return integer value 
#Ver 3 returns float value
#Division by 0 would return ZeroDivisionError
  
#% Modulus 
5 % 5

#** Exponent
5 ** 5

#// Integer Division or Floor Division , always returns integer
5 // 5

"""
Arithmetic Expressions
  Python follows the usual order of operations in expressions. 
    exponents and roots
    multiplication and division
    addition and subtraction
"""

3 + 2 * 4


#Other Global Function (Trainer Hands On)
#Introduce the round function to show the rounding to nearest integer value 

int ( 5.9 )
round ( 5.9 )

"""
Assignment Operator  ( give a hands on using two different number )
  = Assignment 
    ( a = 5 )
  += Addition 
    ( a += 1 ) ( a = a + 1 )
  -= Subtraction 
    ( a -= 1 ) ( a = a - 1 )
  *= Multiplication 
    ( a *= 1 ) ( a = a * 1 )
  /= Division 
    ( a /= 1 ) ( a = a / 1 )
  %= Modulus 
    ( a %= 1 ) ( a = a % 1 )
  **= Exponent 
    ( a **= 1 ) ( a = a ** 1 )
  //= Integer Division or Floor Division 
    ( a //= 1 ) ( a = a // 1 )
"""


#Printing Output to the screen
print ( "FORSK TECHNOLOGIES" )

#Taking Integer Input from user
age = input ( "Enter your Age > ")
print (age)
print (type(age))
  
age = int(age)
print (age)
print (type(age))


#Taking Floating Point Input from user 
temperature  = input ( "Enter your temperature of your city > ")
print (temperature)
print (type(temperature))

  
temperature = float(temperature)
print (temperature)
print (type(temperature))


#Taking String Input from user using raw_input function 
name = input ( "Enter your Name >")
print (name)
print (type(name))

"""
Writing and executing programs in files (Trainer Hands On)
  Creation of .py Python Script in IDLE and Saving it.
  Running of the .py Pyton Script from IDLE
  Running of the .py Python Script from TERMINAL or CMD
  Autocomplete variable names by using ATL + / in IDLE
  Indentation concept to be introduced


Block and Indentation Concept Introduction
  Block with nested block
  Indenting Code


Best Practice for creation of Projects (Trainer Hands On)
  # Step 1
  #  Create a file first.py from IDLE File->New

  # Step 2  
  # Define a new function main

  def main():
    pass

  # Step 3
  # Calling the newly created function  
  main()

  # Step 4
  # Running from CMD or TERMINAL
  # python first.py


Installation of Spyder ( Anaconda )  (Trainer Hands On)
  Explanation of the Different Windows
  Creation of first.py in this environment also
  Running of the Project
  Running of some part of code in Spyder

"""




"""
Code Challenge
  Name: 
    Age Calculator
  Filename: 
    age_cal.py
  Problem Statement:
    Lets assume your age is 21 today
    What would be your age after 5 years from today 
    How old were you 10 years back
  Hint: 
    You need to add to calculate future age 
    You need to subtract to calculate your past age 
"""

"""
Code Challenge
  Name: 
    Height Calculator
  Filename: 
    height_cal.py
  Problem Statement:
    Lets assume your height is 5 Foot and 11 inches 
    Convert 5 Foot into meters and 
    Convert 11 inch into meters and 
    print your total height in meters and 
    print your total heigjt in centimetres also 
  Hint: 
    1 Foot = 0.3048 meters 
    1 inch = 0.0254 meters 
    1 m = 100 cm 
"""


"""
Code Challenge
  Name: 
    Adult Body Mass Index Calculator
  Filename: 
    bmi_cal.py
  Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
  Hint: 
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
"""


"""
Code Challenge
  Name: 
    Ponderal Index Calculator
  Filename: 
    ponderal_cal.py
  Problem Statement:
    Calculate the Ponderal Index of a Person and print it
  Hint: 
    Divide the BMI by your Height ( meters ) to get your Ponderal Index
"""


"""
Code Challenge
  Name: 
    Target Heart Rate Calculator
  Filename: 
    heartrate_cal.py
  Problem Statement:
    Calculate the Maximum Heart Rate and Target Heart Rate Range 
    ( Lower and Higher value ) of a person of a specific age.
    Lets Assume your age is 21 years
  Hint: 
    Subtract your age from 220 to get your Maximum Heart Rate
    Lower end of your Target Heart Rate is 70% of Maximum Heart Rate
    Higher end of your Target Heart Rate is 85% of Maximum Heart Rate
    Heart Rate = Beats per minute 
"""

"""
Code Challenge
  Name: 
    Temperature Calculator
  Filename: 
    temp_cal.py
  Problem Statement:
    Assume today's temperature in Jaipur is 29 degree Centigrade. 
    Calculate the temperate in Degree Fahrenheit and print it.
    Calculate the temperature in Degree Kelvin and print it.
  Hint: 
    Multiply by 9/5 and add 32  to get in Fahrenheit
    Add 273 approximately to get in Kelvin
"""

"""
Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilmeters by the litres used to get the average
"""


"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
 """    

"""
Code Challenge
  Name: 
    Gravity Calculator
  Filename: 
    gravity_cal.py
  Problem Statement:
    Compute the position of the object after falling for 10 seconds. 
    Output the value meters and assume that the acceleration is -9.81  
  Hint: 
    Distance = (Acceleration*Time*Time ) / 2
"""

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

"""
CODE CHALLENGES ( Take input from user in all the  code challenges ) 
Challenge 1
Challenge 2
Challenge 3
Challenge 4
Challenge 5
Challenge 6
Challenge 7
Challenge 8
Challenge 9
Challenge 10
"""








