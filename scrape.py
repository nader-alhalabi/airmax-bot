from wsgiref.util import request_uri
import requests
import re
from bs4 import BeautifulSoup

page1 = "https://www.vviruslove.com/2-%d9%83%d9%88%d8%af-%d8%aa%d9%81%d8%b9%d9%8a%d9%84-code-airmax-2023-2022/"
page2 = "https://www.vviruslove.com/2-%d9%83%d9%88%d8%af-%d8%aa%d9%81%d8%b9%d9%8a%d9%84-code-airmax-2023-2022-2/"

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
    pro = soup.find_all('img', {'src':re.compile(r'[A-Z0-9].jpg')})
    #return airmax[0]["src"], pro[0]["src"]
    final_code = re.findall(r'\b\d+\b', airmax[1]["src"])[2]
    final_code2 = re.findall(r'[0-9A-Z]{6,6}', pro[2]["src"])[0]
    return final_code, final_code2


airmax_code, pro_code = scrape_images()
print("Airmax:",airmax_code)
print("Airmax Pro:",pro_code)