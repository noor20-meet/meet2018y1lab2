Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=b
>>> b=5
>>> a
10
>>> b
5
>>> a=b
>>> b=a
>>> a
5
>>> b
5
>>> a=10
>>> b=a
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> b
10
>>> c=a
>>> a=b
>>> b=c
>>> a=5
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
5
>>> c
5
>>> four='4'
>>> five='4'
>>> print(five)
4
>>> prinve(five*3)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    prinve(five*3)
NameError: name 'prinve' is not defined
>>> print(five*3)
444
>>> my_name='student'
>>> type (my-name)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    type (my-name)
NameError: name 'my' is not defined
>>> type(my_name)
<class 'str'>
>>> print('my name is'+'my_name')
my name ismy_name
>>> print('my name is'+ my_name)
my name isstudent
>>> my_age=14
>>> print('I am '+my_age+' years old')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print('I am '+my_age+' years old')
TypeError: must be str, not int
>>> print('I am ' + my_age + ' years old')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print('I am ' + my_age + ' years old')
TypeError: must be str, not int
>>> my_age='14'
>>> print('I am '+my_age+' years old')
I am 14 years old
>>> score='1'
>>> total=score+(count*3)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    total=score+(count*3)
NameError: name 'count' is not defined
>>> total=score+(score*3)
>>> print(total)
1111
>>> 
