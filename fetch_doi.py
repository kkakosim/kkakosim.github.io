import urllib.request
import re

url = 'https://www.sciencedirect.com/science/article/pii/S0032591026008995'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    doi_match = re.search(r'doi\.org/(10\.\d{4,9}/[-._;()/:A-Z0-9]+)', html, re.I)
    if doi_match:
        print('DOI:', doi_match.group(1))
    else:
        print('DOI not found')
except Exception as e:
    print('Error:', e)
