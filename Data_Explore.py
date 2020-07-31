import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
import numpy as np
from pandas import DataFrame

#---------initial data orginzation from the raw text file-------------------
data = [Date,Time,Wind,Gust,Dir,RH,Temp,Pres] = [],[],[],[],[],[],[],[]
f_in = open(input('What file do you wish to examine? '),'r')
line = f_in.readlines()
f_in.close()

for x in range(len(line)):
    for y in range(8):
        hdl = line[x].split(';')
        data[y].append(hdl[y])

#-------------------sort out data into daily csv files-----------------------------
u_dates = np.unique(Date)

for x in range(len(u_dates)):
   for date in u_dates:
    file = str(date)+'_Date.csv'
    f_out = open(file.replace('/','_'),'w+')
    dframe = DataFrame({'Time':Time,'Wind':Wind,'Gust':Gust,'Dir':Dir,'RH':RH,'Temp':Temp,'Pres':Pres},index=Date)
    write_frame = dframe.loc[date]
    write_frame.to_csv(file.replace('/','_'),index=False)
    f_out.close()