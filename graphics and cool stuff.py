#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


np.random.seed(10)


# In[7]:


N=30
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)


# In[10]:


area = (30 * np.random.rand(N))**2


# In[11]:


plt.scatter(x, y, s=area, c=colors, alpha=0.4)
plt.show()


# In[20]:


from matplotlib import style
style.use('ggplot')

x = [2,4,6]
y = [12,14,5]

x2 = [3,3,4]
y2 = [7,14,5]


# In[21]:


plt.bar(x, y, color='r', align='center')
plt.bar(x2, y2, color='b', align='center')

plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# In[ ]:




