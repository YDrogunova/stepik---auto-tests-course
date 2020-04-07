from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    input1 = browser.find_element_by_id("input_value")
    inputAnswer = browser.find_element_by_id("answer")
    y = input1.text
    calcY = calc(y)
    browser.execute_script("window.scrollBy(0, 100);")
    inputAnswer.send_keys(calcY)
    input2 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    input2.click()
    input3 = browser.find_element_by_css_selector("[for='robotsRule']")
    input3.click()
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
