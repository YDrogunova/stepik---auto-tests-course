from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    element = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button1 = browser.find_element_by_css_selector("button.btn").click()
    inputValue = browser.find_element_by_id("input_value")
    inputAnswer = browser.find_element_by_id("answer")
    y = inputValue.text
    calcY = calc(y)
    inputAnswer.send_keys(calcY)
    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()
