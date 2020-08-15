#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random


# In[9]:


cdicelist=rolldice(3)
udicelist=rolldice(3)
print(cdicelist,udicelist)


# In[ ]:


n = int(input('choose number of dice to use:'))
def roll_dice(n):
    dice = []   
    for i in range(n):
        dice.append(random.randint(1,6))    
    return dice
    print(dice)
myrolling=roll_dice(6)
myrolling=roll_dice(n)
print('you roll:')
print( myrolling)
dice = []   
for i in range(n
        dice.append(random.randint(1,6))    
return roll_dice(n):
print(dice)
myrolling=ai_roll(6)
myrolling=ai_roll(n)
print('AI rolls')
print( myrolling)

computertotal = sum(cdicelist)
usertotal = sum(udicelist)
print('Computer total', computertotal)
print('User total',usertotal )
if usertotal > computertotal:
        elif usertotal < computertotal:
        print('Computer wins')
else:
    print('It is a tie!')

