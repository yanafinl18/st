from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))


browser.find_element_by_id("book").click()

x_element = browser.find_element_by_id("input_value")
y = x_element.text

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

text_value = calc(y)

input1 = browser.find_element_by_id("answer")
input1.send_keys(text_value)
button = browser.find_element_by_id("solve")
button.click()
