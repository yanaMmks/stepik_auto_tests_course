from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text


    res = str(int(num1, base = 10)+int(num2,base=10))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(res)  # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()