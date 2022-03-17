import math
from selenium import webdriver

browser = webdriver.Chrome()
link = " http://suninjuly.github.io/redirect_accept.html"
browser.get(link)


input = browser.find_element_by_css_selector('.trollface.btn-primary').click()

# переключились на новое окно
new_win = browser.window_handles[1]
browser.switch_to.window(new_win)


x_element = browser.find_element_by_id("input_value")
y = x_element.text

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

text_value = calc(y)

input1 = browser.find_element_by_id("answer")
input1.send_keys(text_value)
button = browser.find_element_by_css_selector(".btn-primary")
button.click()
