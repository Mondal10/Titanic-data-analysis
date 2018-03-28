
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Graph ui setting
sns.set_style("dark")

#reading data 
titanic_data=pd.read_csv('C:/Users/Amit/Desktop/titanic_data.csv')


# In[7]:


titanic_data.head()


# In[8]:


titanic_data.tail()


# In[19]:


#creating dataset without unwanted columns
titanic_data_cleaned=titanic_data.drop(['name','ticket','fare','cabin','embarked','boat','body','home.dest'],axis=1)
titanic_data_cleaned.head()


# In[20]:


titanic_data_cleaned.tail()


# In[21]:


#fixing missing or data format issues
titanic_data_cleaned.isnull().sum()


# In[22]:


#reviewing some missing age data
missing_age_bool=pd.isnull(titanic_data_cleaned['age'])
titanic_data_cleaned[missing_age_bool].head()


# In[23]:


titanic_data_cleaned[missing_age_bool].tail()


# In[27]:


# Taking a look at the datatypes
titanic_data_cleaned.info()


# In[50]:


# Determine number of males and females with missing age values
missing_age_female = titanic_data_cleaned[missing_age_bool]['sex'] == 'female'
missing_age_male = titanic_data_cleaned[missing_age_bool]['sex'] == 'male'

mafs=missing_age_female.sum()
mams=missing_age_male.sum()
print ('number of females age missing:',mafs)
print ('number of males age missing:',mams)


# In[47]:


#statistics
titanic_data_cleaned.describe()


# In[49]:


# Age min at 0.42 looks a bit weird so give a closer look
titanic_data_cleaned[titanic_data_cleaned['age'] < 1]


# In[54]:


youngest_to_survive=titanic_data_cleaned[titanic_data_cleaned['survived']==True]['age'].min()
youngest_to_die=titanic_data_cleaned[titanic_data_cleaned['survived']==False]['age'].min()
oldest_to_survive=titanic_data_cleaned[titanic_data_cleaned['survived']==True]['age'].max()
oldest_to_die=titanic_data_cleaned[titanic_data_cleaned['survived']==False]['age'].max()

yts=youngest_to_survive
ytd=youngest_to_die
ots=oldest_to_survive
otd=oldest_to_die

print (' Youngest to survive:',yts,'\n Youngest to die:',ytd,'\n Oldest to survive',ots,'\n Oldest to die',otd)


# In[55]:


#Were social-economic standing a factor in survival rate?
#Returns survival rate/percentage of sex and class

def survival_rate(pclass, sex):
    """
    Args:
        pclass: class value 1,2 or 3
        sex: male or female
    Returns:
        survival rate as percentage.
    """
    grouped_by_total = titanic_data_cleaned.groupby(['pclass', 'sex']).size()[pclass,sex].astype('float')
    grouped_by_survived_sex =         titanic_data_cleaned.groupby(['pclass','survived','sex']).size()[pclass,1,sex].astype('float')
    survived_sex_pct = (grouped_by_survived_sex / grouped_by_total * 100).round(2)

    return survived_sex_pct


# In[87]:


#actual number grouped by class,survival and sex
groupedby_class_survived_size = titanic_data_cleaned.groupby(['pclass','survived','sex']).size()

#printing grouped class,survival and sex
print ('overall data:\n')
print (groupedby_class_survived_size)
print ('*******************************')

#calculating survival rate
sf1=survival_rate(1,'female')
sm1=survival_rate(1,'male')
sf2=survival_rate(2,'female')
sm2=survival_rate(2,'male')
sf3=survival_rate(3,'female')
sm3=survival_rate(3,'male')


#printing data in percentage form
print ('Class 1: Female survival rate:',sf1)
print ('Class 1: Male survival rate:',sm1)
print ('*******************************')
print ('Class 1: Female survival rate:',sf2)
print ('Class 1: Male survival rate:',sm2)
print ('*******************************')
print ('Class 1: Female survival rate:',sf3)
print ('Class 1: Male survival rate:',sm3)
print ('*******************************')

#graph-group(class,survival and sex)
g = sns.factorplot(x="sex", y="survived", col="pclass", data=titanic_data_cleaned,
                   saturation=.5, kind="bar", ci=None, size=5, aspect=.8)

#Fixing the labels
(g.set_axis_labels('', 'Survival Rate')
     .set_xticklabels(["Women", "Men"])
     .set_titles("Class {col_name}")
     .set(ylim=(0, 1))
     .despine(left=True, bottom=True))

#graph with actual count
g = sns.factorplot('survived', col='sex', hue='pclass', data=titanic_data_cleaned, kind='count', size=7, aspect=.8)

#Fixing labels of second graph
(g.set_axis_labels('Suvivors', 'No. of Passengers')
    .set_xticklabels(["False", "True"])
    .set_titles('{col_name}')
)

titles = ['Women', 'Men']
for ax, title in zip(g.axes.flat, titles):
    ax.set_title(title)


# In[94]:


#Did age, regardless of sex and class, determine your chances of survival?

#Let us first identify and get rid of records with missing Age
print ('number of females age missing:',mafs)
print ('number of males age missing:',mams)

# Droping the NaN values. 
titanic_data_age_cleaned = titanic_data_cleaned.dropna()

#Finding total count of survivors and those who didn't
number_survived = titanic_data_age_cleaned[titanic_data_age_cleaned['survived'] == True]['survived'].count()
number_died = titanic_data_age_cleaned[titanic_data_age_cleaned['survived'] == False]['survived'].count()

#finding average
mean_age_survived = titanic_data_age_cleaned[titanic_data_age_cleaned['survived'] == True]['age'].mean()
mean_age_died = titanic_data_age_cleaned[titanic_data_age_cleaned['survived'] == False]['age'].mean()

#displaying total
print ('Total no. of survivors:',number_survived,
       '\nTotal no. of non-survivors:',number_died,
       '\nMean age of survivors:',mean_age_survived,
       '\nMean age of non-survivors:',mean_age_died)

# Graph - Age of passengers across sex of those who survived
g = sns.factorplot(x="survived", y="age", hue='sex', data=titanic_data_age_cleaned, kind="box", size=7, aspect=.8)

# Fix up the labels
(g.set_axis_labels('Suvivors', 'Age of Passengers')
    .set_xticklabels(["False", "True"])
)


# In[100]:


#Did women and children have preference to lifeboats and therefore survival (assuming there was no shortage of lifeboats)?
# <18years considered child

titanic_data_age_cleaned.loc[
    ( (titanic_data_age_cleaned['sex'] == 'female') &
    (titanic_data_age_cleaned['age'] >= 18) ),
    'Category'] = 'Woman'

titanic_data_age_cleaned.loc[
    ( (titanic_data_age_cleaned['sex'] == 'male') &
    (titanic_data_age_cleaned['age'] >= 18) ),
    'Category'] = 'Man'

titanic_data_age_cleaned.loc[
    (titanic_data_age_cleaned['age'] < 18),
    'Category'] = 'Child'

# totals grouped by Men, Women and Children, and by survival
print (titanic_data_age_cleaned.groupby(['Category','survived']).size())

# Graph - Compare survival count between Men, Women and Children
g = sns.factorplot('survived', col='Category', data=titanic_data_age_cleaned, kind='count', size=7, aspect=.8)

# Fix up the labels
(g.set_axis_labels('Suvivors', 'No. of Passengers')
    .set_xticklabels(['False', 'True'])
)

titles = ['Women', 'Children', 'Men']
for ax, title in zip(g.axes.flat, titles):
    ax.set_title(title)

