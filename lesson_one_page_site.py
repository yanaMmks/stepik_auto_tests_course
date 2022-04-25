import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element_by_css_selector(".btn.btn-primary").click()



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element_by_id("input_value").text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

time.sleep(1)
browser.find_element_by_xpath('//*[@id="solve"]').click()

time.sleep(10)
browser.quit()