from selenium import webdriver
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    form = browser.find_element_by_id('answer')
    form.send_keys(calc(x))
    checkbox = browser.find_element_by_css_selector('.form-check-input#robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    browser.find_element_by_class_name('btn').click()

finally:
    sleep(15)
    browser.quit()


