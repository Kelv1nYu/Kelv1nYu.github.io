#%%
# Import

import numpy as np
import pandas as pd
import os

import seaborn as sns
import matplotlib as plt

#%%

DATA_DIR = os.getcwd() + '\\archive\\'

df = pd.read_csv(DATA_DIR + 'us_disaster_declarations.csv')
df.head(10)

#%%
df.info()
#%%
# Clean
df_1 = df.iloc[:, 2:15]
df_1['designated_area'] = df['designated_area']

year_list = list()
for i in range(2001, 2021):
    year_list.append(i)


df_1 = df_1.loc[df_1['fy_declared'].isin(year_list)].reset_index(drop=True)
df_1 = df_1.drop(columns = ['incident_end_date', 'disaster_closeout_date'])
df_1

#%%

df_area = df_1[['state', 'designated_area']]
df_area.head(10)

df_area = df_area.groupby(['state', 'designated_area']).size()
df_area = df_area.to_frame()
df_area.columns = ['count']

df_area.to_csv('df_area.csv')


# %%
# area_types = df_area['designated_area'].unique()

# print('Types of area:\n\n', area_types)
# print('Occurrences:\n\n', df['designated_area'].value_counts())
# %%
# Figure 1

df_area_count = df_1['state'].value_counts().rename_axis('State').to_frame('counts')
df_area_count.to_csv('df_area_count.csv')
df_area_count

#%%
# Figure 2
# df_area = df_1['designated_area'].value_counts().rename_axis('Area').to_frame('counts')
# df_area.to_csv('df_area.csv')
# df_area

# %%
# Figure 3
df_time = df_1['fy_declared'].value_counts().rename_axis('Years').to_frame('counts')
df_time.to_csv('df_time.csv')
df_time

# %%
# Figure 4
df_d_type = df_1['declaration_type'].value_counts().rename_axis('Declaration_type').to_frame('counts')
df_d_type.to_csv('df_d_type.csv')
df_d_type

#%%
# Figure 5
df_i_type = df_1['incident_type'].value_counts().rename_axis('Incident_type').to_frame('counts')
df_i_type.to_csv('df_i_type.csv')
df_i_type

#%%
df_1['declaration_date'] = pd.to_datetime(df_1['declaration_date'])
df_1['incident_begin_date'] = pd.to_datetime(df_1['incident_begin_date'])

df_1['diff_time'] = (df_1['declaration_date'] - df_1['incident_begin_date']).dt.seconds/3600
df_1['diff_time'] = round(df_1['diff_time'])

df_1.to_csv('df_d_time.csv')

# %%
