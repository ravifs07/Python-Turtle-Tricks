import turtle as t
from turtle import *

tracer(4)
pensize(5)
colors = ["red","green", "blue"]
for i in range(2000):
    t.color(colors[i%3])
    t.fd(i*5)
    t.lt(200)
    t.width(4)
    t.rt(10)