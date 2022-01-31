from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element_by_class_name('btn').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_css_selector('.nowrap#input_value').text
    num = calc(x)
    browser.find_element_by_css_selector('.form-control#answer').send_keys(num)
    browser.find_element_by_class_name('btn').click()
    alert = browser.switch_to.alert
    temp = alert.text.split(': ')
    print(temp[-1])
    alert.accept()

finally:
    browser.quit()