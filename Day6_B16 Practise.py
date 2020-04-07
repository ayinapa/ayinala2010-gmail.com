#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Loops 
My_Employs = ['Nani','Ravi','Madan','Somu','Veru', 'Jenny', 'James']
print(My_Employs)
My_Employs[0].title()


# In[12]:


#Split students Individuall with out loops
My_Employs = ['Nani','Ravi','Madan','Somu','Veru', 'Jenny', 'James']
for ItTeam in My_Employs:
    print(ItTeam)


# In[22]:


# Send Team Performace report to everyone 
for ItTeam1 in My_Employs:
    print(f"Your Overall Project Performence  is Excellent with no errors, project deployed to client ontime  {ItTeam1}.")
    print(f"This month you should get 20% bounus {ItTeam1}. \n ") 
print('Congrates to all team members. ') 
    


# In[ ]:




