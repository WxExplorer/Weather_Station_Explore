import numpy as np
from pandas import DataFrame
import pandas as pd

#This program organizes the weather stations data dump and sorts it out into daily csv files.


swt = True
while swt == True:
    u_input = input('Want to process a file? (y or n) ')

    #inputs the file and sorts out to each data point

    if u_input[0].lower() == 'y':
        f_in = open(input('What file do you wish to sort out? '),'r')
        line = f_in.readlines()
        f_in.close()

        data = [Date,Time,Wind,Gust,Dir,RH,Temp,Pres] = [],[],[],[],[],[],[],[]
        for x in range(len(line)):
            for y in range(8):
                hdl = line[x].split(';')
                data[y].append(hdl[y])

        u_dates = np.unique(Date)  #collects each data the file had, used to create individual dataframes

        #creates daily dataframes than saves them to a csv, labeling them by each day.

        for date in u_dates:
            file = str(date)+'_Date.csv'
            f_out = open(file.replace('/','_'),'w+')
            dframe = DataFrame({'Time':Time,'Wind':Wind,'Gust':Gust,'Dir':Dir,'RH':RH,'Temp':Temp,'Pres':Pres},index=Date)
            write_frame = dframe.loc[date]
            write_frame.to_csv(file.replace('/','_'),index=False)
            f_out.close()
    else:
        print('Closing the organizer')
        swt = False