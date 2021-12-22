import requests
import re
from bs4 import BeautifulSoup

page = "https://www.vviruslove.com/2-%d9%83%d9%88%d8%af-%d8%aa%d9%81%d8%b9%d9%8a%d9%84-code-airmaxtv-iptv-2020-2021-2/"

def scrape_images():
    result = requests.get(page)

    # if successful parse the download into a BeautifulSoup object, which allows easy manipulation 
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")

    images = soup.find_all('img', {'src':re.compile('.jpg')})
    return images[5]["src"], images[9]["src"]
