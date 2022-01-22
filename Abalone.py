#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


data = pd.read_csv('file:///D:/Project/abalone.csv')


# In[34]:


data.shape


# In[35]:


data.head()


# In[36]:


data.describe()


# In[37]:


data.info()


# In[38]:


data.isnull().sum()


# In[39]:


sns.pairplot(data)


# In[41]:


data.columns


# In[42]:


sns.heatmap(data[[ 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
       'Viscera weight', 'Shell weight', 'Rings']])


# In[43]:


data['Sex'].value_counts()


# In[44]:


plt.rcParams['figure.figsize'] = (18, 8)
sns.boxplot(data['Rings'], data['Length'], hue = data['Sex'], palette = 'pastel')
plt.title('Rings vs length and sex', fontsize = 20)


# In[45]:


plt.rcParams['figure.figsize'] = (20, 8)
sns.violinplot(data['Rings'], data['Diameter'], hue = data['Sex'], palette = 'Set1')
plt.title('Rings vs diameter and sex', fontsize = 20)


# In[46]:


plt.rcParams['figure.figsize'] = (18, 8)
sns.boxenplot(data['Rings'], data['Height'], hue = data['Sex'], palette = 'Set2')
plt.title('Rings vs height and sex', fontsize = 20)


# In[47]:


plt.rcParams['figure.figsize'] = (18, 10)
sns.swarmplot(data['Rings'], data['Whole weight'])
plt.title('Rings vs weight')


# In[48]:


plt.rcParams['figure.figsize'] = (18, 10)
sns.swarmplot(data['Rings'], data['Shucked weight'], palette = 'dark')
plt.title('Rings vs shucked weight')


# In[49]:


plt.rcParams['figure.figsize'] = (18, 10)
sns.stripplot(data['Rings'], data['Viscera weight'])
plt.title('Rings vs Viscera Weight')


# In[50]:


plt.rcParams['figure.figsize'] = (18, 10)
sns.regplot(data['Rings'], data['Shell weight'])
plt.title('Rings vs Shell weight')


# In[51]:


from math import pi


# In[53]:


df = pd.DataFrame({
'group': [i for i in range(0, 4177)],
'Sex': data['Sex'],
'Length': data['Length'],
'Diameter': data['Diameter'],
'Whole weight':  data['Whole weight'],
'Viscera weight': data['Viscera weight'],
'Shell weight': data['Shell weight']
})


# In[54]:


categories=list(df)[1:]
N = len(categories)


# In[55]:


values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values


# In[56]:


angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]


# In[57]:


ax = plt.subplot(111, polar=True)


# In[60]:


plt.xticks(angles[:-1], categories, color='grey', size=8)
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)
ax.plot(angles, values, linewidth=1, linestyle='solid')
plt.title('Radar Chart for determing Importances of Features', fontsize = 20)
ax.fill(angles, values, 'red', alpha=0.1)


# In[63]:


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])
data['Sex'].value_counts()
data = pd.get_dummies(data)


# In[64]:


data.head()


# In[65]:


y = data['Rings']
data = data.drop(['Rings'], axis = 1)
x = data
print("Shape of x:", x.shape)
print("Shape of y:", y.shape)


# In[66]:



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
print("Shape of x_train :", x_train.shape)
print("Shape of x_test :", x_test.shape)
print("Shape of y_train :", y_train.shape)
print("Shape of y_test :", y_test.shape)


# In[68]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

model = RandomForestClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)


mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("RMSE :", rmse)


r2 = r2_score(y_test, y_pred)
print("R2 Score :", r2)


# In[69]:


get_ipython().system('pip install eli5')


# In[70]:


import eli5 
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(model, random_state = 0).fit(x_test, y_test)
eli5.show_weights(perm, feature_names = x_test.columns.tolist())


# In[ ]:




