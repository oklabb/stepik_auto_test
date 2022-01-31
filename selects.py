from selenium import webdriver
from time import sleep

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    total = str(int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text))
    css = f'[value="{total}"]'
    browser.find_element_by_class_name('custom-select').click()
    browser.find_element_by_css_selector(css).click()
    browser.find_element_by_class_name('btn').click()

finally:
    sleep(10)
    browser.quit()
