from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text


    num2 = browser.find_element_by_id("num2").text

    summa = int(num1) + int(num2)
    print(summa)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(summa))

    browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
