# Importando bibliotecas que serão utilizadas.
import zipfile
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup


# Criando váriaveis que serão utilizadas.
download_uri = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'


def main():

    r = requests.get(download_uri)
    soup = BeautifulSoup(r.text)
    allTDs = soup.find_all('td')
    
    for td in allTDs:
        if td.text == '2022-02-07 14:03  ':
            filename = td.find_previous_sibling('td').text
            break

    pathFileDownload = download_uri + filename
    dataframe = pd.read_csv(pathFileDownload)
    dfOrdered = dataframe.sort_values(by=['HourlyDryBulbTemperature'], ascending=False)
    print(dfOrdered)

pass


if __name__ == '__main__':
    main()
