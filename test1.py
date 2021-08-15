from turtle import *
s=Screen()
s.setup(550,600,330,10)
s.bgcolor('green')

t=Turtle()
t.shape('turtle')
t.color('white')
t.pensize(5)
s.onclick(t.goto)

done()
