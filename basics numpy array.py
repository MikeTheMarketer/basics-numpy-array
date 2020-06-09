#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


square_meter = (100,110,105,155,125,135,150,140,150,125)
rooms = (4,3,4,4,2,3,2,3,2,4)
price = (295000,275000,325000,330000,300000,290000,295000,305000,315000,320000)


# In[5]:


my_new_array = np.array([square_meter, rooms, price])
print(my_new_array)


# In[6]:


transposed_array = my_new_array.transpose()
print(transposed_array)


# In[10]:


print(transposed_array.shape)
#array includes 10 rows long and 3 columns - rows include each home statistics - column contain home categories (square_yards, rooms, price)


# In[104]:


def array_function(columns, rows):
    
    my_array = np.ones((columns,rows),dtype=int)
                
    my_array[1::2,1::2] = 0
    
    print(my_array)

    
    
array_function(10,10)


# In[ ]:





# In[ ]:





# In[ ]:




