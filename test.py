import requests as r
from bs4 import BeautifulSoup

d = r.get("http://rarbgenter.org/torrents.php?search=Tushy&category%5B%5D=1")

with open("sample.html", "wb") as f:
    f.write(d.content)

print(d.text)
