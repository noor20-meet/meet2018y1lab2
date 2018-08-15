Python 3.6

.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
my_name=input("What's your name?")
What's your name? Noor
>>> my_name
' Noor'
>>> print("Hello there "+my_name)
Hello there  Noor
>>> len("Noor")
4
>>> var=len("Noor")
>>> print("Your name is "+var+" letters long!")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Your name is "+var+" letters long!")
TypeError: must be str, not int
>>> var="len('Noor')"
>>> var
"len('Noor')"
>>> var=str(len("Noor"))
>>> var
'4'
>>> print("Your name is "+var+" letters long!")
Your name is 4 letters long!
>>> var="Noor"
>>> var[0]
'N'
>>> var[3]
'r'
>>> print("The first letter of your name is "+var[0]+" and the last letter of your name is "+var[3])
The first letter of your name is N and the last letter of your name is r
>>> print("The first letter of your name is "+capitaalize() var[0]+" and the last letter of your name is "+capitalize() var[3])
SyntaxError: invalid syntax
>>> print("The first letter of your name is "+capitalize() var[0]+" and the last letter of your name is "+capitalize() var[3])
SyntaxError: invalid syntax
>>> print("The first letter of your name is "+capitalize( var[0])+" and the last letter of your name is "+capitalize( var[3]))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print("The first letter of your name is "+capitalize( var[0])+" and the last letter of your name is "+capitalize( var[3]))
NameError: name 'capitalize' is not defined

>>> print("The first letter of your name is "+ var[0]+" and the last letter of your name is R")
The first letter of your name is N and the last letter of your name is R
>>> Var2=""Hi there, my name is Claire. Nice to meet you!"
SyntaxError: invalid syntax
>>> var2="Hi there, my name is Claire. Nice to meet you!"
>>> var2[21:27]
'Claire'
>>> mood=input("How are you?")



