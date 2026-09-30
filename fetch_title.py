import urllib.request
import re

try:
    req = urllib.request.Request('https://www.cost.eu/actions/CA25146/', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    if match: print('H1:', match.group(1).strip())
    match2 = re.search(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL)
    if match2: print('H2:', match2.group(1).strip())
except Exception as e:
    print('Error:', e)
