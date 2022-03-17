import time
import os
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)


input2 = browser.find_element_by_css_selector('[name="firstname"]')
input2.send_keys("Ivan")

input2 = browser.find_element_by_css_selector('[name="lastname"]')
input2.send_keys("Ivanov")

input2 = browser.find_element_by_css_selector('[name="email"]')
input2.send_keys("Ivan@mail.ru")




current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file_new.txt')

element = browser.find_element_by_id("file")
element.send_keys(file_path)

time.sleep(1)
browser.find_element_by_css_selector(".btn.btn-primary").click()

