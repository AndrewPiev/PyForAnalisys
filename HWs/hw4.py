#!/usr/bin/env python
# coding: utf-8

# ## Урок 4. Визуальный анализ данных ##
# Условие 1: Задача 1 Постройте график Назовите график Сделайте именование оси x и оси y Сделайте выводы
# 
# 1.1. Данные из прошлого дз
# 1.2 Изучите стоимости недвижимости
# 1.3 Изучите распределение квадратуры жилой
# 2.1.4 Изучите распределение года постройки
# 
# Условие 2: 2 задача
# 
# 2.1 Изучите распределение домов от наличия вида на набережную
# Постройте график
# Сделайте выводы
# 2.2 Изучите распределение этажей домов
# 2.2 Изучите распределение состояния домов
# 
# Условие 3: 3 задача
# Исследуйте, какие характеристики недвижимости влияют на стоимость недвижимости, с применением не менее 5 диаграмм из урока.
# Анализ сделайте в формате storytelling: дополнить каждый график письменными выводами и наблюдениями.

# In[142]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# ### Задача 1

# In[143]:


df = pd.read_csv('https://gbcdn.mrgcdn.ru/uploads/asset/4266730/attachment/08ec55854637add5247d22396d0f7456.csv', sep=',')
df


# ### 1.2

# In[144]:


plt.figure(figsize=(15, 5))
plt.hist(df['price'],color = 'blue', edgecolor = 'black', bins = int(1500/5))
plt.xlim(xmin=50000, xmax = 1500000)
plt.ylim(ymin=0, ymax = 1200)
plt.title('Распределение стоимости недвижимости')
plt.xlabel('Стоимость в миллионах долларов')
plt.ylabel('Количество стоимостей в диапазоне')
plt.grid(True);


# In[145]:


plt.figure(figsize=(15, 5))
plt.hist(df['price'],color = 'blue', edgecolor = 'black', bins = int(1500/5))
plt.xlim(xmin=50000, xmax = 5000000)
plt.ylim(ymin=0, ymax = 1200)
plt.title('Распределение стоимости недвижимости')
plt.xlabel('Стоимость в миллионах долларов')
plt.ylabel('Количество стоимостей в диапазоне')
plt.grid(True);


# In[146]:


plt.figure(figsize=(10, 5))
plt.hist(df['price'],color = 'blue', edgecolor = 'black')
plt.title('Распределение стоимости недвижимости')
plt.xlabel('Стоимость в сотнях тысяч долларов')
plt.ylabel('Количество стоимостей в диапазоне');


# *Вывод: подавляющее большинство недвижимости стоит до 1 млн. долларов*

# In[147]:


df["price"].min(), df["price"].max(), df["price"].mean()


# ### 1.3

# In[148]:


plt.figure(figsize=(20, 6))
sns.histplot(df['sqft_living'])
plt.ticklabel_format(style='plain')
plt.title('Распределение жилой площади')
plt.xlabel('Площадь')
plt.ylabel('Кол-во');


# ### 1.4

# In[149]:


plt.figure(figsize=(20, 6))
sns.histplot(df['yr_built'])
plt.ticklabel_format(style='plain')
plt.title('Распределение года постройки')
plt.xlabel('Год постройки')
plt.ylabel('Кол-во');


# ## Задача 2

# ### 2.1

# In[150]:


df_w = df['waterfront'].value_counts()
df_w


# In[151]:


plt.pie(df_w, autopct='%1.1f%%', labels=['Нет вида\nна набережную', 'Есть вид\nна набережную'])
plt.title('Распределение домов от наличия вида на набережную');


# In[152]:


df[df["waterfront"] == 1]["price"].mean(), df[df["waterfront"] == 0]["price"].mean(), df[df["waterfront"] == 1]["price"].mean()/df[df["waterfront"] == 0]["price"].mean()


# *Стоимость домов с видом на набережную в среднем 3 раза выше и это очень редкое предложение*

# ### 2.2

# In[153]:


df_fl = df['floors'].value_counts()
df_fl


# In[154]:


plt.figure(figsize=(8, 6))
sns.barplot(x = df_fl.index, y = df_fl)
plt.title('Распределение этажей домов')
plt.xlabel('Кол-во этажей')
plt.ylabel('Кол-во')
plt.xticks(rotation=45);


# ### 2.3

# In[155]:


df_con = df['condition'].value_counts()
df_con


# In[156]:


plt.figure(figsize=(8, 6))
sns.barplot(x = df_con.index, y = df_con)
plt.title('Распределение состояния домов')
plt.xlabel('Состояние дома')
plt.ylabel('Кол-во');


# ## Задача 3

# In[157]:


sns.jointplot(x=df['price'], y=df['sqft_living'], kind='reg'); 


# In[158]:


sns.jointplot(x=df['price'], y=df['sqft_above'], kind='reg');


# In[159]:


sns.jointplot(x=df['price'], y=df['grade'], kind='reg');


# In[160]:


sns.jointplot(x=df['price'], y=df['bedrooms'], kind='reg');


# In[161]:


sns.jointplot(x=df['price'], y=df['bathrooms'], kind='reg');


# In[162]:


sns.jointplot(x=df['price'], y=df['yr_built'], kind='reg');


# In[163]:


sns.jointplot(x=df['price'], y=df['floors'], kind='reg');


# *Из диаграмм следует, что все признаки вляют на стоимость прямопропорционально, при этом наибольшее воздействие на цену недвижимости оказывают общая и жилая площади, а наименьшее влияние имеет год постройки*
