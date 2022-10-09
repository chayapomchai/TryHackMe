#print(requests.get('https://xshot.winwin.co.th/Main'))
from requests import get 
file = open("/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt").read().splitlines()
file = [f for f in file if f != ""]
file = [k for k in file if k[0] != "#"]
#print(file)
url = 'http://10.10.47.114/'
#l = []
def status(x):
    x = get(x).status_code
    return x
#print(status(a))
print("start here")
for i in file:
#    print(f"{get(a+i)} from {i}")
#    if status(a+i) == 429:
#        time.sleep(4)
#        print(f"{get(a+i)} from {i}")
    rdurl = url + i
    if status(rdurl) == 200:
        print(rdurl)
#        l.append(i)
#print(l)

#l = [i for i in file[14:1000] if status(a+i) == 200]
#print(l)
