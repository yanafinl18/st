import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


num_list = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('num', num_list)
def test_link(browser, num):
    link = f"https://stepik.org/lesson/{num}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))

    input1 = browser.find_element_by_css_selector(".ember-text-area.ember-view")
    input1.send_keys(str(answer))
    browser.implicitly_wait(5)

    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    time.sleep(5)
    corr_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert corr_text == "Correct!", "Неверный текст сообщения"
