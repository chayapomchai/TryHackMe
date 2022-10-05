import requests
print(requests.get('https://xshot.winwin.co.th/Main'))
from requests import get
print("test")
print(get('https://tryhackme.com/room/mrrobot/index'))
print(get('https://tryhackme.com/index'))
print(get('https://tryhackme.com/room/mrrobot/images'))
print(get('https://tryhackme.com/images'))
file = open("/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")
print(type(get('https://xshot.winwin.co.th/Main')))
print(get('https://tryhackme.com/room/mrrobot/# directory-list-2.3-medium.txt').status_code)
print(type(get('https://tryhackme.com/room/mrrobot/# directory-list-2.3-medium.txt').status_code))
print(get('https://tryhackme.com/room/mrrobot/# directory-list-2.3-medium.txt').status_code == get('https://xshot.winwin.co.th/Main').status_code)
print("start here")
for i in file:
#    print(f"{get(f'https://tryhackme.com/room/mrrobot/{i}')} from {i}")
    if get(f'https://tryhackme.com/room/mrrobot/{i}').status_code == get('https://xshot.winwin.co.th/Main').status_code:
        print(i)
        print("yes")