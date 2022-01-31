from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element_by_id('book')
    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    x = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_id('solve').click()
    alert = browser.switch_to.alert
    answer = alert.text.split(': ')
    print(answer[-1])
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()