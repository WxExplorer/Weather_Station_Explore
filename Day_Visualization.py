import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd

"""This program inputs daily weather data, headers included, and creates two graphs visualizing the data (Temp and RH, Gusts and Pressure).
The program also checks on valid wind gusts, where invalid measurements are written as nan.
Current version stores the daily stats, but needs them stored for later use."""

#----------user inpute for the .csv file--------------------------------------
file = input('Which csv file do you wish to summerize and visulize: ')
data_fr = pd.read_csv(file)

#---------checking for invalid wind gusts-------------------------------------
for x in range(len(data_fr)):
    if data_fr['Wind'][x]*10 <= data_fr['Gust'][x] and data_fr['Wind'][x] > 0.5:
        data_fr['Gust'][x] = np.nan
    elif data_fr['Wind'][x] == data_fr['Gust'][x] and data_fr['Wind'][x] > 5:
        data_fr['Gust'][x] = np.nan

#-----block for daily stats, currently being written--------------------------
data_fr.describe()


#------main plotting area, with temp/RH graph first---------------------------
ax = data_fr.plot(x='Time',y='Temp',color='r',figsize = (10,5))
ax2 = data_fr.plot(x='Time',y='RH',secondary_y=True,color='g',ax=ax,figsize = (10,5))
plt.title('Temperature and RH Daily Graph')
ax.set_ylabel('C')
ax2.set_ylabel('%')
plt.tight_layout()
name = str(file[:-9])+ ' T-RH Graph.png'
plt.savefig(name)


#-------------wind gust and pressure graph------------------------------------
ax = data_fr.plot(x='Time',y='Gust',figsize = (10,5))
ax2 = data_fr.plot(x='Time',y='Pres',secondary_y=True,ax=ax,figsize = (10,5))
plt.title('Wind Gust and Pressure Daily Graph')
ax.set_ylabel('mph')
ax2.set_ylabel('hPa')
plt.tight_layout()
name = str(file[:-9])+ ' Gust-Press Graph.png'
plt.savefig(name)
