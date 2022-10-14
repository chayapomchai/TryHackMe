from requests import get
import optparse
def getarg():
    parser = optparse.OptionParser()
    parser.add_option("-u","--url",dest="url",help="URL of Website")
    parser.add_option("-w","--wdlt",dest="wordlist",help="The Wordlist Address")
    option,argument = parser.parse_args()
    if (not option.url or not option.wordlist):
        parser.error("[-] Please specify an interface. use --help for more information.")
    return option
option = getarg()
url = option.url
wordlist = option.wordlist
file = open(wordlist).read().splitlines()
#url = 'http:// /'
#file = open("/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt").read().splitlines()
file = [f for f in file if f != ""]
file = [f for f in file if f[0] != "#"]
#print(file)
def status(x):
    x = get(x).status_code
    return x
print("start here")
for i in file:
    rdurl = url + i
    if get(rdurl).status_code == 200:
        print(rdurl)
