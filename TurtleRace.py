#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
a1a=turtle.Turtle()
a2a=turtle.Turtle()
a3a=turtle.Turtle()

#import turtles
color=['blue','green','red']

#colors

turtle_list=[a1a,a2a,a3a]
for i in range(3):
    turtle_list[i].color(color[i])
    turtle_list[i].penup()
    turtle_list[i].goto(-160, 100*i)
    turtle_list[i].pendown()
    #setup raceand setup list
    
    pos=turtle_list[0].pos()
print(pos)
#show start pos

from random import randint
for movement in range(100):
    for turtle in turtle_list:
        speed=randint(1,5)        
        turtle.forward(speed)

for turtle in turtle_list:
    print(turtle.pos())
#race starting and end pos

