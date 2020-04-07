from selenium import webdriver
import time
import math



try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element_by_css_selector("button.trollface")
    button.click()

    new_window=browser.window_handles[1]
    confirm = browser.switch_to.window(new_window)

    inputValue = browser.find_element_by_id("input_value")
    inputAnswer = browser.find_element_by_id("answer")
    y = inputValue.text
    calcY = calc(y)
    inputAnswer.send_keys(calcY)
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()