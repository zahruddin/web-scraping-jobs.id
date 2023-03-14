#Zahruddin Fanani
#https://github.com/zahruddin

import requests;
from bs4 import BeautifulSoup
import pandas as pd

key = input('masukan keyword: ')

url = 'https://www.jobs.id/lowongan-kerja?kata-kunci={}'.format(key)

req = requests.get(url)

# print(req)

soup  = BeautifulSoup(req.text, 'html.parser')
items = soup.find_all('div','col-xs-12 single-job-ads')
data = []
for it in items:
  posisi = it.find('a','bold').text #ambil data posisi yang tersedia
  instansi = ''.join(it.find('p').find('a').text.strip().split('\n')) #ambil data instansi yang membuka lowongan
  gaji = ', '.join([s.text.strip() for s in it.find_all('span', 'semi-bold')]) #ambil data gaji yang di tawarkan 
  if gaji == 'Gaji Dirahasiakan': gaji = 0 # jika gaji di rahasiakan akan di ubah jadi 0
  data.append([posisi, instansi,gaji])

df = pd.DataFrame(data, columns=['posisi','instansi','gaji'])
print(df)
print()
print()
print()
save = input('Simpan ke excel (y/t)? ')
if save.upper() == 'Y':
    df.to_csv(key+'-jobs.id.csv')
    print('Data diexport ke excel')
else:
    print('Data tidak diexport ke excel')