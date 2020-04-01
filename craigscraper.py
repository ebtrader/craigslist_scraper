from bs4 import BeautifulSoup
import requests
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = "https://boston.craigslist.org/search/sof"

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')

# Extracting all the <a> tags whose class name is 'result-title' into a list.
titles = soup.findAll('a', {'class': 'result-title'})

# Extracting text from the the <a> tags, i.e. class titles.
counts = {}

for title in titles:
    #print(title.text)

#puts the jobs in a dictionary

    for word in title:
        counts[word] = counts.get(word,0) + 1

#prints the dictionary
#print(counts)

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
#print(lst)

lst = sorted(lst, reverse=True)
#print(lst)

for val, key in lst[:20] :
    print(key, val)
