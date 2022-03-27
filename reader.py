import cv2
import pytesseract
import scrape
import urllib.request

airmax = scrape.scrape_images()
urllib.request.urlretrieve(airmax, "airmax.jpg")
#urllib.request.urlretrieve(pro, "pro.jpg")

print(airmax)

img = cv2.imread("airmax.jpg")
#img2 = cv2.imread("pro.jpg")
text = pytesseract.image_to_string(img)
#text2 = pytesseract.image_to_string(img2)

# extract only the code from the image text
final_code = [int(s) for s in text.split() if s.isdigit()][1]
print("Airmax:", final_code)
#print("Airmax Pro:", text2)
