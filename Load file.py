from selenium import webdriver
import time
import os.path



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    Input_FirstN = browser.find_element_by_name("firstname")
    Input_FirstN.send_keys("Ivan")
    Input_LastN = browser.find_element_by_name("lastname")
    Input_LastN.send_keys("Ivanov")
    Input_Email = browser.find_element_by_name("email")
    Input_Email.send_keys("email")
    Input_UploadF=browser.find_element_by_id("file")

    base_dir = os.path.abspath(os.path.dirname(''))
    temp_dir = os.path.join(base_dir, 'file.txt')
    Input_UploadF.send_keys(temp_dir)

  #  Doc = browser.find_element_by_xpath("//input[@type=‘file’]")
  #  File="C:\Users\juli1\PycharmProjects\stepik1\file.txt"
   # Doc.send_keys(File)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
