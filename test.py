from selenium import webdriver
from time import sleep

link = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    f_name = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    f_name.send_keys('My answer')
    l_name = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    l_name.send_keys('My answer')
    email = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    email.send_keys('My answer')
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    sleep(5)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    sleep(10)
    browser.quit()