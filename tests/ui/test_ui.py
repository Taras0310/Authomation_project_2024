from webbrowser import Chrome

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    #відкриваємо сторінку github
    driver.get('https://github.com/login')



    #знаходимо інпут вводу імені
    login_element = driver.find_element(By.ID, 'login_field')

    #вводимо неправильне ім'я
    login_element.send_keys('taras.test')

    #аналогічні дії для паролю
    password_element = driver.find_element(By.ID, 'password')
    password_element.send_keys('test123')

    btn_element = driver.find_element(By.NAME, 'commit')

    #емулюємо клік
    btn_element.click()
    #time.sleep(3)

    # закриваємо браузер
    driver.close()