from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from datetime import datetime, timedelta
import loginFunc

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
'''로그인'''
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
import loginData

idInput.send_keys(loginData.id)
time.sleep(0.5)
pwdInput.send_keys(loginData.pwd)
time.sleep(2)
btnInput.click()
time.sleep(6)
'''로그인 끝 '''

keyword = "seoul_trends"
driver.get(f"https://www.instagram.com/{keyword}/")
time.sleep(3)

contentSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > article > div:nth-child(1) > div'
links = []
while len(links) < 50:
    try:
        for i in range(6):
            try:
                driver.execute_script("window.scrollBy(0,600);")
            except Exception as e:
                print('스크롤 하다가 에러 남 ', e)
                pass
            time.sleep(1)
        postBox = driver.find_element(By.CSS_SELECTOR, contentSelector)
        postLink = postBox.find_elements(By.TAG_NAME, 'a')  # return []

        for i in range(len(postLink)):
            eachLink = postLink[i]
            link = eachLink.get_attribute('href')
            links.append(link)
        # 중복제거
        links = set(links)
        links = list(links)
    except Exception as e:
        print('에러다!!!!')
        print(e)


with open('content_links.txt', "w") as f:
    for link in links:
        f.write(f'{link}\n')

print('게시글 링크 따기 완료 !!')
print(len(links))
input()
