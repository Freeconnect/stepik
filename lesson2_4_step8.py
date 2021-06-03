from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 20).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id("book").click()
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_id("solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
