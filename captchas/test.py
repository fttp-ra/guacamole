import cv2
import time
import numpy as np
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

x = 1

while x <= 5:

    opt = webdriver.ChromeOptions()

    opt.add_argument("--headless")

    browser = webdriver.Chrome(executable_path=r"/home/rhino/opt/chromedriver", options=opt)

    browser.get('http://contribuyente.seniat.gob.ve/BuscaRif/Captcha.jpg')

    captcha = browser.find_element_by_xpath('/html/body/img')

    screenshot = captcha.screenshot_as_png
    with open('captcha%s.png' % x, 'wb') as f:
        f.write(screenshot) 
    
    img = Image.open('captcha%s.png' % x)
    img = img.resize((200, 50), Image.ANTIALIAS)
    img = cv2.imread('./captcha%s.png' % x)
    kernel = np.ones((2),np.uint8)
    erosion = cv2.erode(img,kernel,iterations = 2)
    _,binarizadaInv = cv2.threshold(erosion,95,250,cv2.THRESH_BINARY_INV)
    cv2.imwrite('captcha%s.png' % x, binarizadaInv)

    time.sleep(2)

    #browser.close()

    x+=1