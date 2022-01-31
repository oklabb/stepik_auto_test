from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_tag_name('button').click()
    browser.switch_to.window(browser.window_handles[-1])
    num = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(num)
    browser.find_element_by_tag_name('button').click()
    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
    alert.accept()

finally:
    browser.quit()