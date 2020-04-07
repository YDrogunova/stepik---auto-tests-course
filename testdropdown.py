from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    input_a = browser.find_element_by_id("num1")
    input_b = browser.find_element_by_id("num2")
    a = input_a.text
    b = input_b.text
    summ = str(int(a) + int(b))


    select = Select(browser.find_element_by_tag_name("select"))
   # select = Select(browser.find_element_by_css_selector(value =' + Summ + '))
    select. select_by_value("[value = 'summ']").click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()