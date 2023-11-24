from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from datetime import datetime, timedelta
import loginData


def login(driver):
    loginIdSelector = '#loginForm > div > div:nth-child(1) > div > label > input'
    # 3초동안 기다려봐용
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, loginIdSelector)
    ))
    loginPwdSelector = '#loginForm > div > div:nth-child(2) > div > label > input'
    loginButtonSelector = '#loginForm > div > div:nth-child(3)'
    idInput = driver.find_element(By.CSS_SELECTOR, loginIdSelector)
    pwdInput = driver.find_element(By.CSS_SELECTOR, loginPwdSelector)
    btnInput = driver.find_element(By.CSS_SELECTOR, loginButtonSelector)

    idInput.send_keys(loginData.id)
    time.sleep(0.5)
    pwdInput.send_keys(loginData.pwd)
    time.sleep(2)
    btnInput.click()
    time.sleep(6)
