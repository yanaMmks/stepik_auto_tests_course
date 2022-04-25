from selenium import webdriver
import time
import math


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(".btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_id("input_value").text
    y=calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    btn = browser.find_element_by_css_selector(".btn.btn-primary")
    btn.click()



    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()