from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    box_checked = browser.find_element_by_id("treasure")
    x = box_checked.get_attribute("valuex")
    y = calc(x)    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
   
    time.sleep(10)
   
    browser.quit()
