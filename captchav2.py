from selenium import webdriver
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

finally:
    sleep(15)
    browser.quit()


