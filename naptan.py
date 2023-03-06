import requests
import csv
download_localities = requests.get(url='https://naptan.api.dft.gov.uk/v1/nptg/localities')
with open('localities.csv','w') as f:
    f.write(download_localities.content.decode('utf-8'))
