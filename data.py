from zipfile import ZipFile
import numpy as np
import os
import urllib
import urllib.request

def grab_station_historical(station, first, last, skip_years, folder):
    for i in range(first,last,1):
        url = f'https://www.ndbc.noaa.gov/view_text_file.php?filename={station}h{i}.txt.gz&dir=data/historical/stdmet/'
        file = f'{folder}\\{station}h{i}.txt'

        if str(i) not in skip_years and not os.path.isfile(file):
            print(f'Downloading {url} and saving as {file}...')
            urllib.request.urlretrieve(url, file)

# TODO: Write function to read the documents and collect the relevant fields for input and output data.
class Data:

    def __init__(self, folder='.'):
        self.folder = folder
        #self.X = np.array([[0,0,0,0]])
        self.X = np.array([[0,0]])
        
        self.Y = np.array([[0]])
        self.verybad = 0
        self.i = 0

    def set_folder(self, folder):
        self.folder = folder

    def ingest_folder_full(self):
        print(f'[+] Ingesting folder: {self.folder}')
        for file in os.listdir(self.folder):
            self.ingest_file_full(file)
        print(f'[+][+] Ingested {self.i} total lines')


    def ingest_file_full(self, file):
 
        print(f'[+] Ingesting file: {file}')

        # append an empty list here because we are making a list of lists

        # Reading from file line by line 
        f = open(f'{self.folder}/{file}', 'r') 

        lines = f.readlines()       

        # Iterate through a file .
        bad = 0
        WD_array = []
        WVHT_i = 0
        WD_i = 0
        GST_i = 0
        WSPD_i = 0

        j = 0
        for line in lines: 
            #self.X.append([])
            #self.Y.append([])
            l = line.split(' ')

            # because the data format is inconsistent, we have to remove all the '' entries...
            l[:]= [x for x in l if x]

            # some files start actual values at 2nd line
            ## One argument is going to be change in wind direction over past 3 hours so skip the first 3 entries
            
            # Find the indexes of the desired columns
            c = 0
            if j < 1:
                for e in l:
                    if e == 'WVHT':
                        WVHT_i = c
                    elif e == 'WD' or e == 'WDIR':
                        WD_i = c
                    elif e == 'GST':
                        GST_i = c
                    elif e == 'WSPD':
                        WSPD_i = c
                    c+=1

                print(f'[+][+] Found inputs: WVHT_i = {WVHT_i} WD_i = {WD_i} GST_i = {GST_i} WSPD_i = {WSPD_i}')

            # Start at the 5th column because 
            start = 5
            if j > 1:
                WD = l[WD_i]
                WD_array.append(float(WD))
            if j >= start:
                WVHT = l[WVHT_i]
                GST = l[GST_i]
                WSPD = l[WSPD_i]
                WD = l[WD_i]
                
                # Only collect the sample if WVHT is less than 99. 
                ## also only collect of WD is less than 999
                # If it is, then the buoy was erroring.
                if float(WVHT) < 99 and float(WD) < 999:
                    # ground truth output is WVHT, what we are trying to predict
                    #self.Y.append(float(WVHT))
                    self.Y = np.append(self.Y, [[float(WVHT)]], axis=0)
                    # inputs are WD, WSPD, and GST
                    #self.X[self.i].append(float(WD))
                    #self.X[self.i].append(float(WSPD))
                    #self.X[self.i].append(float(GST))
                    
                    # final input is Change in WD in past 3 hours
                    delta_WD = abs(WD_array[j-2] - WD_array[j-3]) + abs(WD_array[j-3] - WD_array[j-4]) + abs(WD_array[j-4] - WD_array[j-5])
                    #print(f'delta_WD = {WD_array[i-2]} - {WD_array[i-3]} + {WD_array[i-3]} - {WD_array[i-4]} + {WD_array[i-4]} - {WD_array[i-5]} = {delta_WD}')
                    #self.X[self.i].append(delta_WD)
                    #self.X = np.append(self.X, [[float(WD), float(WSPD), float(GST), float(delta_WD)]], axis=0)
                    self.X = np.append(self.X, [[float(WD), float(WVHT)]], axis=0)
                    
                    if WSPD == 99.0 or GST == 99.0:
                        self.verybad+=1

                    if not self.i % 1000:
                        #print(f'[+][+] line {j}: WVHT = {self.Y[self.i]} WD = {self.X[self.i][0]} GST = {self.X[self.i][2]} WSPD = {self.X[self.i][1]} delta_WD = {self.X[self.i][3]}')
                        #print(f'[+][+] line {j}: Appended: {[[float(WD), float(WSPD), float(GST), float(delta_WD)]]}')
                        pass
                    
                    self.i+=1 
                else:
                    bad+=1
            j+=1
            

        #print(f'[+][+] Ingested {j-start} lines except for {bad} bad lines')
        self.X = np.delete(self.X, 0, 0)
        self.Y = np.delete(self.Y, 0, 0)
        print('Finished ingesting information:')
        print('   WD.    WSPD    GST  d_WSPD   WVHT ')
        print(f'{np.c_[self.X, self.Y]}')

    def print_data(self, function='all'):

        if function == 'all':
            print('X:')
            print(self.X)
            print('Y:')
            print(self.Y)
        
        if function == 'max':
            print('X:')
            print(max(self.X))
            print('Y:')
            print(max(self.Y))

if __name__ == "__main__": 
    station = 51003
    folder = f'D:/SCHOOL/Fall2020/CSC718/project/CSC718_FinalProject/data/training_data/noaa{station}'
    # first_year = 1984
    # last_year = 2019
    # skip_years = ['2014']

    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    # grab_station_historical(station, first_year, last_year + 1, skip_years, folder)

    data = Data(folder)
    #data.ingest_folder_full()
    data.ingest_file_full('51003h2010.txt')
    #data.print_data('max')
    
