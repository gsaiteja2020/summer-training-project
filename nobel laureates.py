#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


nobel = pd.read_csv('Nobel.csv')
nobel.head(10)


# ## Which sex and which Country most commonly represented??

# ### Using diplay() instead of print() as display is having nice output as compared to print

# In[3]:


# Displaying Number of nobel prizes handed
display(len(nobel.Prize))

# Displaying number of nobel prizes won by male and female
display(nobel.Sex.value_counts())

# display number of prizes won by top 10 countries
nobel['Birth Country'].value_counts().head(10)


# # When diid USA started to dominate the Nobel Prize charts?
# ## Bcause during 1901 all winners were from Europe

# In[4]:


# Calculating USA born winners per decade
nobel['usa_born_winner'] = nobel['Birth Country'] == 'United States of America'
nobel['decade'] = (np.floor(pd.Series(nobel.Year)/10)*10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index = False)['usa_born_winner'].mean()

# displaying usa born winners per decade
display(prop_usa_winners)


# #### from table it is only giving a rough idea but to actually see when USA started to dominate we need a plot

# ## Visualizing USA Dominance

# In[5]:


sns.set()

plt.rcParams['figure.figsize'] = [11,8]

#Plotting line plot for USA born winners
ax = sns.lineplot(prop_usa_winners['decade'],prop_usa_winners['usa_born_winner'])

# Adding %-formatting to the y- axis
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter())


# ## Gender of Typical Nobel Prize Winners

# In[6]:


# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel.Sex == "Female"
prop_female_winners = nobel.groupby(['decade','Category'],as_index=False)['female_winner'].mean()

# Plotting USA born winners with % winners on the y-axis

# Setting the plotting theme
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners 
ax = sns.lineplot(x='decade', y='female_winner', hue='Category', data=prop_female_winners)
# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter())


# ## First woman to win Nobel Prize and in what category

# In[7]:


nobel[nobel['Sex'] == 'Female'].nsmallest(1,'Year',keep='first')


# # Repeating Laureates

# In[8]:


nobel.groupby("Full Name").filter(lambda x: len(x) >= 2)['Full Name'].value_counts()


# # Plotting Age of Nobel Prize Winners when they won prize

# In[9]:


# Converting birth_date from String to datetime
nobel['Birth Date'] = pd.to_datetime(nobel["Birth Date"],errors='coerce')
# Calculating the age of Nobel Prize winners
nobel['Age'] = nobel['Year'] - nobel['Birth Date'].dt.year

# Plotting the age of Nobel Prize winners

sns.lmplot(x='Year',y='Age',data=nobel, lowess=True, aspect=2, line_kws={"color" : "black"})


# ## Let's look at age trends within different prize categories.

# In[10]:


sns.lmplot(x='Year',y='Age',data=nobel, lowess=True, aspect=2, line_kws={"color" : "black"},row='Category')


# # Oldest and Youngest Nobel Prize winners

# In[11]:


# The oldest winner of a Nobel Prize as of 2016
display(nobel.nlargest(1, "Age"))

# The youngest winner of a Nobel Prize as of 2016
nobel.nsmallest(1, "Age")


