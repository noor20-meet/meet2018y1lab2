Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> yp7=turtle.Turtle()
>>> t=200
>>> b=-200
>>> #draw A
>>> turtle.hideturtle()
>>> yp7.pendown()
>>> yp7.goto(-1000,0)
>>> yp7.penup()
>>> a,c=yp7.pos()
>>> yp7.goto(a,c)
>>> yp7.pendown()
>>> yp7.goto(a+100,c+300)
>>> yp7.goto(a+200,c)
>>> yp7.goto(a+30,c+100)
>>> yp7.goto(a+300,c+100)
t
>>> turtle.manloop()
Python 3.6.5 (default, Apr  1 2018, 05:46:30)
