#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('Gel_Filtration.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(row[1])
  
plt.bar(x, y, color = 'b', width = 0.65, label = "Superdex")
plt.xlabel('Columns')
plt.ylabel('Particle Size')
plt.title('Gel Filtration')
plt.legend()
plt.show()


# In[ ]:




