from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
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
time.sleep(0.3)
btnInput.click()
time.sleep(3)

# webSearch = '//*[@id="mount_0_0_U4"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div[1]/nav/div/header/div/div/div[1]/div/div/div/div/div/input'
# WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, webSearch)
# ))
keyword = "김포맛집"
driver.get(f"https://www.instagram.com/explore/tags/{keyword}/")
post_selector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > article > div > div > div'
WebDriverWait(driver, 60).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, post_selector)
))
print('아,.,./,/.,/.,ㅌㅋ')
# 최근게시물 기준으로 div가 삭제되고 최근이 생기는 방식
# 링크 추출하기
links = []
while len(links) <20:
    postBox = driver.find_element(By.CSS_SELECTOR,post_selector)
    postLink = postBox.find_elements(By.TAG_NAME,'a') #return []
    #6qjs스크롤 내리기
    for _ in range(6):
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(0.3)
    #포스트 링크 추출 ->href
    # for eachLink in postLink:
    #     print('거짓말하지마')
    #     print(eachLink)
    #     link = eachLink.get_attribute('href')
    #     links.append(links)
    for i in range(len(postLink)):
        eachLink = postLink[i]
        print(eachLink)
        link = eachLink.get_attribute('href')
        links.append(link)
    #중복제거
# 100개 링크..
for link in links:
    print(link)

print(len(links),"개 출력 ")
input()
