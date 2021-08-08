import pandas as pd
import numpy as np
import datetime
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.style.use('ggplot')
import calendar
data=pd.read_csv("D:Uber Drives.csv")
data.head()
print(data)

#above part =import lib and read data

#clean data
data.tail()
data = data[:-1]
print(data)

#checking for null values
data.isnull().sum()
sns.heatmap(data.isnull(),yticklabels=False, cmap="viridis")

#drop/remove null values from data
data = data.dropna()
sns.heatmap(data.isnull(), yticklabels = False, cmap="viridis")

#Getting an hour, day, days of the week, a month from the date of the trip.
data['START_DATE*'] = pd.to_datetime(data['START_DATE*'], format="%m/%d/%Y %H:%M")
data['END_DATE*'] = pd.to_datetime(data['END_DATE*'], format="%m/%d/%Y %H:%M")

hour = []
day = []
dayofweek = []
month = []
weekday = []
for x in data['START_DATE*']:
    hour.append(x.hour)
    day.append(x.day)
    dayofweek.append(x.dayofweek)
    month.append(x.month)
    weekday.append(calendar.day_name[dayofweek[-1]])
data['HOUR']=hour
data['DAY']=day
data['DAY_OF_WEEK']=dayofweek
data['MONTH']=month
data['WEEKDAY']=weekday

#finding travaling time
time=[]
data['TRAVELLING_TIME']=data['END_DATE*']-data['START_DATE*']
for i in data['TRAVELLING_TIME']:
    time.append(i.seconds/60)
data['TRAVELLING_TIME'] = time
data.head()

#calculate the avg speed of trip
data['TRAVELLING_TIME'] = data['TRAVELLING_TIME']/60
data['SPEED'] = data['MILES*']/data['TRAVELLING_TIME']
data.head()

#Different categories of data
sns.countplot(x='CATEGORY*', data=data)

#Histogram for miles
data['MILES*'].plot.hist()

#trip for pourpose
data['PURPOSE*'].value_counts().plot(kind='bar', figsize=(10, 5), color='blue')

#trip per hour of day
data['HOUR'].value_counts().plot(kind='bar', figsize=(10, 5), color='green')

#trip per day of week
data['WEEKDAY'].value_counts().plot(kind='bar', color='green')

#trip in month
data['MONTH'].value_counts().plot(kind='bar', figsize=(10, 5), color='green')

#The starting points of trips
data['START*'].value_counts().plot(kind='bar', figsize=(25, 5), color='red')

#Comparing all the purpose with miles, hour, day of the month, day of the week, month, Travelling time.
data.groupby('PURPOSE*').mean().plot(kind='bar', figsize=(15, 5))