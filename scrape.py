from wsgiref.util import request_uri
import requests
import re
from bs4 import BeautifulSoup

page1 = "https://www.vviruslove.com/2-%d9%83%d9%88%d8%af-%d8%aa%d9%81%d8%b9%d9%8a%d9%84-code-airmaxtv-iptv-2020-2021-2/"
page2 = "https://www.vviruslove.com/2-%d9%83%d9%88%d8%af-%d8%aa%d9%81%d8%b9%d9%8a%d9%84-code-airmaxtv-iptv-2020-2021/"

# check which link has the code image
def check_link():
    result = requests.get(page1)
    if result.url != "https://www.vviruslove.com/":
        return result
    else:
        return requests.get(page2)

def scrape_images():
    result = check_link()

    # if successful parse the download into a BeautifulSoup object, which allows easy manipulation 
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")

    airmax = soup.find_all('img', {'src':re.compile(r'[0-9].jpg')})
    #pro = soup.find_all('img', {'src':re.compile(r'[A-Z].jpg')})
    #return airmax[0]["src"], pro[0]["src"]
    final_code = re.findall(r'\b\d+\b', airmax[0]["src"])[2]
    return final_code


print(scrape_images())