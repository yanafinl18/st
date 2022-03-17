import time
import math
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

num = browser.find_element_by_id("input_value").text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


input1 = calc(num)

input2 = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
input2.send_keys(input1)

browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
browser.find_element_by_css_selector('[for="robotsRule"]').click()

time.sleep(1)
browser.find_element_by_css_selector(".btn.btn-primary").click()
