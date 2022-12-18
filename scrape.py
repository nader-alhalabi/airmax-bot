from wsgiref.util import request_uri
import requests
import re
from bs4 import BeautifulSoup

main_page = "https://www.vviruslove.com/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D9%83%D9%88%D8%AF-airmax-tv-iptv-%D9%85%D8%AF%D8%A9-%D8%A7%D9%84%D8%AD%D9%8A%D8%A7%D8%A9-%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D8%A9-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9/"

def get_click_page():
    result = requests.get(main_page)
    soup = BeautifulSoup(result.content, "html.parser")
    air = soup.find_all("a", style="color: #0000ff;")
    return air[1]["href"]


def get_code_page(click_page):
    result1 = requests.get(click_page)
    soup = BeautifulSoup(result1.content, "html.parser")
    air = soup.find_all("a", class_="su-button su-button-style-default su-button-wide")
    return air[0]["href"]


def scrape_images():
    click_page = get_click_page()
    code_page = get_code_page(click_page)
    result = requests.get(code_page)
    soup = BeautifulSoup(result.content, "html.parser")

    airmax = soup.find_all('img', {'src':re.compile(r'[0-9].jpg')})
    pro = soup.find_all('img', {'src':re.compile(r'[A-Z0-9].jpg')})

    airmax_code = re.findall(r'\b\d+\b', airmax[1]["src"])[2]
    pro_code = re.findall(r'[0-9A-Z]{6,6}', pro[2]["src"])[0]
    return airmax_code, pro_code


airmax_code, pro_code = scrape_images()
print("Airmax:",airmax_code)
print("Airmax Pro:",pro_code)