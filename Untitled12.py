#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sns


# In[5]:


data = pd.read_csv(r'C:\Users\sivae\OneDrive\Desktop\diabetes_model.csv')
data


# In[15]:


# count plot on outcome


# In[16]:


import pandas as pd


# In[17]:


import numpy as np


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


import seaborn as sns


# In[20]:


data = pd.read_csv(r'C:\Users\sivae\OneDrive\Desktop\diabetes_model.csv')
data


# In[21]:


#count plot on outcome


# In[24]:


sns.countplot(x= 'Outcome',data = data)
plt.show()


# In[25]:


#Analyze the effect of age on Outcome using Boxplot


# In[28]:


sns.boxplot(x = 'Outcome', y='Age', data=data)
plt.title("Age vs Outcome",)
plt.show()


# In[32]:


# Check for the chances of getting diabetes if it is common in family, using the Daiabetes Pedigree Function


# In[44]:


sns.boxplot(x='Outcome',y= 'DiabetesPedigreeFunction',data=data)
plt.show()


# In[ ]:


# Check for the relationship with Insulin & Glucose and group the datapoints by Outcome.


# In[59]:


sns.scatterplot(data['Insulin'],data['Glucose'],hue=data["Outcome"])
plt.title('Relationship with Insulin and Glucose')
plt.show()


# In[ ]:


#Create a heatmap on Correlation of features in the data


# In[82]:



sns.heatmap(data.corr(),annot = True)


# In[ ]:





# In[ ]:




