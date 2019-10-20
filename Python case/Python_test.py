#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Python case'))
	print(os.getcwd())
except:  
	pass

#%%
import numpy as np
import pandas as pd

#%% [markdown]
# # Задача 1

#%%
df = pd.read_csv('alfa_python_test.csv', sep = ',')


#%%
df.info()


#%%
# переведем дату в тип date
df['date'] = pd.to_datetime(df['date'])


#%%
# сгруппируем наш датасет 
date = df.groupby(['id']).agg('max')


#%%
date['id'] = date.index


#%%
# Создадим требуемую таблицу
df_new = date.merge(df, left_on=['id','date'], right_on=['id','date'])


#%%
# Уберем пробелы из перечислений городов
df_new['city'] = df_new['city'].apply(lambda x: str(x).replace(' ', ''))

#%% [markdown]
# ### Напишем функцию, которая будет преобразовывать группы городов:
# ##### Например, группы ABC и СBA должны быть преобразованы к одной записи

#%%
def sets(df_new):
    for i in df_new.index:
        towns = df_new['city'][i]
        towns_list = towns.split(',')
        for j in df_new['city']:
            towns_list_1 = j.split(',')
            if list(set(towns_list_1) ^ set(towns_list)) == []:
                df_new['city'].replace(','.join(towns_list_1), ','.join(towns_list), inplace = True)


#%%
sets(df_new)

#%% [markdown]
# #### Количество id в каждом множестве городов:

#%%
df_new['city'].value_counts()


#%%
Spb = 0
Msk= 0
S = 0
Kaz = 0

for town in df_new['city']:
    if town.count('St-Petersburg') == 1:
        Spb += 1
    if town.count('Moscow') == 1:
        Msk += 1
    if town.count('Sochi') == 1:
        S += 1
    if town.count('Kazan') == 1:
        Kaz += 1


#%%
d = {'Санкт-Петербург' : Spb, 'Москва' : Msk, 'Сочи' : S, 'Казань' : Kaz}

#%% [markdown]
# #### Количество уникальных id в каждом городе:

#%%
d

