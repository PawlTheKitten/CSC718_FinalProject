from zipfile import ZipFile
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
        self.X = []
        self.Y = []
        self.verybad = 0

    def set_folder(self, folder):
        self.folder = folder

    def ingest_folder_full(self):

        for file in os.listdir(self.folder):
            self.ingest_file_full(file=file)


    def ingest_file_full(self, file):
 
        print(f'ingesting file: {self.folder}{file}')

        # append an empty list here because we are making a list of lists

        # Reading from file line by line 
        f = open(f'{self.folder}/{file}', 'r') 

        lines = f.readlines()       

        # Iterate through a file .
        i = 0
        bad = 0
        WD_array = []
        for line in lines: 
            self.X.append([])
            self.Y.append([])
            l = line.split(' ')

            # because the data format is inconsistent, we have to remove all the '' entries...
            l[:]= [x for x in l if x]

            # some files start actual values at 2nd line
            ## One argument is going to be change in wind direction over past 3 hours so skip the first 3 entries
            
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # TODO: the files change year to year. I need to find the right column for each desired input
            start = 5
            if i > 1:
                WD = l[4]
                WD_array.append(float(WD))
                print(WD_array)
            if i >= start:
                WVHT = l[7]
                GST = l[6]
                WSPD = l[5]
                WD = l[4]
                
                # Only collect the sample if WVHT is less than 99. 
                ## also only collect of WD is less than 999
                # If it is, then the buoy was erroring.
                if float(WVHT) < 99 and float(WD) < 999:
                    # ground truth output is WVHT, what we are trying to predict
                    self.Y[i-start].append(float(WVHT))

                    # inputs are WD, WSPD, and GST
                    self.X[i-start].append(float(WD))
                    self.X[i-start].append(float(WSPD))
                    self.X[i-start].append(float(GST))

                    # final input is Change in WD in past 3 hours
                    delta_WD = abs(WD_array[i-2] - WD_array[i-3]) + abs(WD_array[i-3] - WD_array[i-4]) + abs(WD_array[i-4] - WD_array[i-5])
                    #print(f'delta_WD = {WD_array[i-2]} - {WD_array[i-3]} + {WD_array[i-3]} - {WD_array[i-4]} + {WD_array[i-4]} - {WD_array[i-5]} = {delta_WD}')
                    self.X[i-start].append(delta_WD)

                    if WSPD == 99.0 or GST == 99.0:
                        self.verybad+=1

                else:
                    bad+=1

            i+=1 
        print(f'ingested {file}. {i} lines with {bad} bad lines and {self.verybad} very bad lines')


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

    data.ingest_file_full('51003h1984.txt')
    #data.print_data('max')
    
