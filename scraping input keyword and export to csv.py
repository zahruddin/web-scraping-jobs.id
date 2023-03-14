# Kelompok 2
# Nama  : Zahruddin Fanani
# Nim   : 2102010006
# Prodi : Teknologi Informasi
#
# Nama  : Defitri Karunia Agustin
# Nim     : 2102010030
# Prodi : Teknologi Informasi


import requests;
from bs4 import BeautifulSoup
import pandas as pd

# kelompok Ganjil
# key = 'programmer'
# kelompok Genap
# key = 'web designer'

key = input('masukan keyword: ')

url = 'https://www.jobs.id/lowongan-kerja?kata-kunci={}'.format(key)

req = requests.get(url)

# print(req)

soup  = BeautifulSoup(req.text, 'html.parser')
items = soup.find_all('div','col-xs-12 single-job-ads')
data = []
for it in items:
  posisi = it.find('a','bold').text
  instansi = ''.join(it.find('p').find('a').text.strip().split('\n'))
  gaji = ', '.join([s.text.strip() for s in it.find_all('span', 'semi-bold')])
  if gaji == 'Gaji Dirahasiakan': gaji = 0
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