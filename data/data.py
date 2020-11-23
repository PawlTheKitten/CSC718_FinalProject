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



if __name__ == "__main__": 
    station = 51002
    folder = f'D:\\SCHOOL\\Fall2020\\CSC718\\project\\CSC718_FinalProject\\data\\noaa{station}'
    first_year = 1984
    last_year = 2019
    skip_years = ['2014']

    if not os.path.exists(folder):
        os.makedirs(folder)
    grab_station_historical(station, first_year, last_year + 1, skip_years, folder)
