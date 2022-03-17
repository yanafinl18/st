from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    y = x_element.get_attribute("valuex")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    text_value = calc(y)


    input1 = browser.find_element_by_id("answer")
    input1.send_keys(text_value)


    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()

    input3 = browser.find_element_by_id("robotsRule")
    input3.click()
    time.sleep(2)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
