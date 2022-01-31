#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


data = pd.read_csv('file:///D:/Project/HR Data.csv')


# In[10]:


data.shape


# In[12]:


data.head()


# In[13]:


data.isnull().sum()


# In[14]:


data.info()


# In[16]:


data.describe()


# In[18]:


data["left"] = np.where(data["Attrition"] == "Yes",1,0)


# In[19]:


data.head()


# In[20]:


data.describe()


# In[21]:


import warnings
warnings.filterwarnings('ignore')


# In[26]:


def NumericalVariables_targetPlots(df,segment_by,target_var = "Attrition"):
    """A function for plotting the distribution of numerical variables and its effect on attrition"""
    
    fig, ax = plt.subplots(ncols= 2, figsize = (14,6))    

  
    sns.boxplot(x = target_var, y = segment_by, data=df, ax=ax[0])
    ax[0].set_title("Comparision of " + segment_by + " vs " + target_var)
    
    
    ax[1].set_title("Distribution of "+segment_by)
    ax[1].set_ylabel("Frequency")
    sns.distplot(a = df[segment_by], ax=ax[1], kde=False)
    
    plt.show()


# In[28]:


def CategoricalVariables_targetPlots(df, segment_by,invert_axis = False, target_var = "left"):
    
    """A function for Plotting the effect of variables(categorical data) on attrition """
    
    fig, ax = plt.subplots(ncols= 2, figsize = (14,6))
    
  
    if invert_axis == False:
        sns.countplot(x = segment_by, data=df,hue="Attrition",ax=ax[0])
    else:
        sns.countplot(y = segment_by, data=df,hue="Attrition",ax=ax[0])
        
    ax[0].set_title("Comparision of " + segment_by + " vs " + "Attrition")
    
   
    if invert_axis == False:
        sns.barplot(x = segment_by, y = target_var ,data=df,ci=None)
    else:
        sns.barplot(y = segment_by, x = target_var ,data=df,ci=None)
        
    ax[1].set_title("Attrition rate by {}".format(segment_by))
    ax[1].set_ylabel("Average(Attrition)")
    plt.tight_layout()

    plt.show()


# In[29]:


NumericalVariables_targetPlots(data,segment_by="Age")


# In[30]:


NumericalVariables_targetPlots(data,"DailyRate")


# In[31]:


NumericalVariables_targetPlots(data,"MonthlyIncome")


# In[32]:


NumericalVariables_targetPlots(data,"HourlyRate")


# In[33]:


NumericalVariables_targetPlots(data,"PercentSalaryHike")


# In[34]:


NumericalVariables_targetPlots(data,"TotalWorkingYears")


# In[35]:


sns.lmplot(x = "TotalWorkingYears", y = "PercentSalaryHike", data=data,fit_reg=False,hue="Attrition",size=6,
           aspect=1.5)

plt.show()


# In[36]:


NumericalVariables_targetPlots(data,"DistanceFromHome")


# In[38]:


pd.crosstab(data.JobInvolvement,data.Attrition)


# In[39]:


round(data.JobInvolvement.value_counts()/data.shape[0] * 100,2)


# In[40]:


CategoricalVariables_targetPlots(data,"JobInvolvement")


# In[ ]:




