from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    fields = browser.find_elements_by_class_name('form-control')
    for field in fields:
        field.send_keys('My answer')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    add = browser.find_element_by_id('file')
    add.send_keys(file_path)
    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()
