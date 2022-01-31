from selenium import webdriver
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser.get(link)
    img = browser.find_element_by_tag_name('img')
    valuex = img.get_attribute('valuex')
    inp = browser.find_element_by_css_selector('[type="text"]')
    inp.send_keys(calc(valuex))
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('.btn').click()

finally:
    sleep(10)
    browser.quit()
