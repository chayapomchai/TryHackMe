import requests
#print(requests.get('https://xshot.winwin.co.th/Main'))
from requests import get
import pandas as pd
import time 
file = open("/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")
f = pd.DataFrame(file,columns=['name'])
#print(f)
print(len(f))
print("start here")
a = 'http://10.10.41.157/'
l = []
def status(x):
    x = get(x).status_code
    return x
print(status(a))
for i in f.loc[14:200]['name']:
    print(f"{get(a+i)} from {i}")
    if status(a+i) == 429:
        time.sleep(4)
        print(f"{get(a+i)} from {i}")
    if status(a+i) == 200:
        l.append(i)
print(l)
