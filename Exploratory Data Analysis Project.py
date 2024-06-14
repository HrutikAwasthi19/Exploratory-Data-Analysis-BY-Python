#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np


# In[ ]:





# In[2]:


dataset = pd.read_excel("N:\Superstore_USA.xlsx")


# In[3]:


dataset.head(2)


# In[77]:


dataset['Order Year']=dataset['Order Date'].dt.year


# In[10]:


dataset.shape


# In[8]:


#start with missing value
dataset.isnull().sum()


# In[13]:


#fill with mean value of Product base margin value it is a numerical column so we use mean
dataset["Product Base Margin"].fillna(dataset["Product Base Margin"].mean(),inplace=True)


# In[89]:


dataset['State or Province'].value_counts()[:5]


# In[ ]:





# In[ ]:





# In[ ]:





# In[93]:


sns.barplot(x='Product Category',y='Product Base Margin',data=dataset,estimator='sum')
plt.figure(figsize=(5,4))
plt.show()


# In[91]:


sns.barplot(x='Product Category',y='Profit',data=dataset,estimator='sum')
plt.figure(figsize=(5,4))
plt.show()


# In[ ]:





# In[ ]:





# In[79]:


dataset['Order Year'].value_counts()


# In[80]:


sns.countplot(x='Order Year',data=dataset)
plt.figure(figsize=(5,4))
plt.show()


# In[ ]:





# # Ship Mode

# In[29]:


dataset['Ship Mode'].value_counts()


# In[56]:


x = dataset['Ship Mode'].value_counts().index
y = dataset['Ship Mode'].value_counts().values
y


# In[52]:


plt.figure(figsize=(5,4))
plt.pie(y,labels=x,startangle=60,autopct="%0.2f%%")
plt.legend(loc=2)
plt.show()


# 

# In[55]:


sns.countplot(x="Ship Mode",data=dataset,hue="Product Category")
plt.figure(figsize=(5,4))
plt.show()


# # Customer Segment

# In[61]:


sns.countplot(x="Customer Segment",data=dataset)
plt.figure(figsize=(5,4))
plt.show()


# # Product Caategory

# In[62]:


sns.countplot(x='Product Category',data=dataset)
plt.figure(figsize=(5,4))
plt.show()


# In[71]:


sns.countplot(x="Product Category",data=dataset[dataset["Product Category"]=="Office Supplies"],hue="Product Sub-Category")
plt.figure(figsize=(10,6))
plt.show()


# In[73]:


sns.countplot(x='Product Category',data=dataset[dataset['Product Category']=='Technology'],hue='Product Sub-Category')
plt.figure(figsize=(5,4))
plt.show()


# In[74]:


sns.countplot(x='Product Category',data=dataset[dataset['Product Category']=='Furniture'],hue='Product Sub-Category')
plt.figure(figsize=(5,4))
plt.show()


# In[ ]:





# # Order Priority

# In[14]:


dataset["Order Priority"].value_counts() 


# In[18]:


#finding out unique elements
dataset['Order Priority'].unique()


# In[17]:


dataset['Order Priority'] = dataset['Order Priority'].replace("Critical ","Critical") #permanently replacing value


# In[27]:


plt.figure(figsize=(5,4))
sns.countplot(x="Order Priority",data=dataset)
plt.title('Count of Order Priority')
plt.savefig("Count of Order Priority.jpg")
plt.show()
#to plot column bar plot we use seaborn liabrary


# In[ ]:





# In[ ]:




