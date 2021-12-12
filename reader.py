import cv2
import pytesseract
import scrape
import urllib.request

airmax, pro = scrape.scrape_images()
urllib.request.urlretrieve(airmax, "airmax.jpg")
urllib.request.urlretrieve(pro, "pro.jpg")

print(airmax, pro)

img = cv2.imread(airmax)
img2 = cv2.imread(pro)
text = pytesseract.image_to_string(img)
text2 = pytesseract.image_to_string(img2)
print("Airmax:", text)
print("Airmax Pro:", text2)
