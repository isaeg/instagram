import random
import re

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

# options = webdriver.ChromeOptions()
# # options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36')
# options.add_argument("--disable-logging")
# options.add_argument("--disable-blink-features=AutomationControlled")
# driver = webdriver.Chrome(options=options)
# 없을 때 default 값
refuseKeyword = loginData.refuseKeyword


def login(driver):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
    with open(f'start_time_{loginData.id.strip()}.txt', "a") as f:
        f.write(f'{formatted_time} start \n')
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

    idInput.send_keys(loginData.id)
    time.sleep(0.5)
    pwdInput.send_keys(loginData.pwd)
    time.sleep(2)
    btnInput.click()
    time.sleep(6)
    try:
        with open(f'account_{loginData.id.strip()}.txt', 'r') as f:
            f.readline()
            print(' account_있으니 패스')
        pass
    except Exception as e:
        with open(f'account_{loginData.id.strip()}.txt', 'a') as a:
            a.write(f'hello!!! {loginData.id.strip()}')
            print('account_없으니 일단 write')
        pass
    try:
        with open(f'visited_{loginData.id.strip()}.txt', 'r') as f:
            f.readline()
            print('visited_있으니 패스')
            pass
    except Exception as e:
        with open(f'visited_{loginData.id.strip()}.txt', 'a') as f:
            f.write(f'hello!!! {loginData.id.strip()}')
            print('visited_없으니 일단 write')
        pass

'''공개계정인지 비공계 개정인지 체크함'''


def checkOpen(link, driver):
    driver.get(link)
    try:
        mainSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > div._aady._aa_s'
        # mainSelector = 'div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > div > section > main > div'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, mainSelector)
        ))
        time.sleep(random.randrange(4, 7))
        mainInput = driver.find_element(By.CSS_SELECTOR, mainSelector)
        privateEle = mainInput.find_element(By.CLASS_NAME, "_aa_t")
        isPrivate = True
        print('비공개 게정입니당')
    except Exception as e:
        print("공개 계정입니다")
        contentCountSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > ul > li:nth-child(1) > span > span'
        # contentCountSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > ul > li:nth-child(1) > span > span'
        contentCountInput = driver.find_element(By.CSS_SELECTOR, contentCountSelector)
        contentText = contentCountInput.text

        # 계정에서 팔로우 체크 유무
        mainfollowerSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > div.x6s0dn4.x78zum5.x1q0g3np.xs83m0k.xeuugli.x1n2onr6 > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xmn8rco.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > button > div > div'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, mainfollowerSelector)
        ))
        mainfollowerInput = driver.find_element(By.CSS_SELECTOR, mainfollowerSelector)
        mfollowerText = mainfollowerInput.text

        if contentText == '0':
            print('공개 계정 이지만 게시물 없어서 패스')
            isPrivate = True
        elif mfollowerText == '팔로잉':
            print('이미 팔로잉 한 사람이므로 패스')
            isPrivate = True
        else:
            print('방문할 계정입니다.')
            isPrivate = False
    print(isPrivate)
    return isPrivate


def loveClick(driver):
    loveSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x1xp8e9x.x13fuv20.x178xt8z.x9f619.x1yrsyyn.x1pi30zi.x10b6aqq.x1swvt13.xh8yej3 > div.x6s0dn4.xrvj5dj.x1o61qjw > div.x78zum5 > span.xp7jhwk > div > div > span > svg'
    # loveSelector = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > section._aamu._ae3_._ae47._ae48 > span._aamw > div > div > span > svg'
    loveInput = driver.find_element(By.CSS_SELECTOR, loveSelector)
    loveCheck = loveInput.get_attribute("aria-label")
    if loveCheck == "좋아요":
        print("좋아요 누릅니다!!")
        loveInput.click()
    else:
        print("이미 눌렀어용")
        pass


def checkTime(driver):
    contentTimeSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x1xp8e9x.x13fuv20.x178xt8z.x9f619.x1yrsyyn.x1pi30zi.x10b6aqq.x1swvt13.xh8yej3 > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1yztbdb.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1 > div > a > span > time'
    # contentTimeSelector = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > div._ae5u._ae5v._ae5w > div > div > a > span > time'
    contentTimeInput = driver.find_element(By.CSS_SELECTOR, contentTimeSelector)
    contentTime = contentTimeInput.get_attribute("title")
    # %Y년 %m월 %d일
    return contentTime


def checkTimeResult(days):
    # 지금 내 시간
    current_time = datetime.now()
    # 게시글 시간 타입 변경
    date = datetime.strptime(days, "%Y년 %m월 %d일")
    difference = current_time - date
    # 차이나는 날짜 계산
    result = difference.days
    return result


'''댓글누르기 '''


def inputReply(comments, driver):
    comment = random.choice(comments)
    time.sleep(random.randrange(5, 7))
    replySelector = 'div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > section > main > div > div > div > div > div > div > section > div > form > div > textarea'

    try:
        # 댓글달기 셀렉터가 없다면 --> 댓글 달기 막아놓았다면 except 로 가서 False return
        replyInput = driver.find_element(By.CSS_SELECTOR, replySelector)
        time.sleep(random.randrange(2, 5))
        ActionChains(driver).move_to_element(replyInput).click().send_keys(comment).perform()
        replyButtonSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div.x4h1yfo > div > div.xdj266r.xktsk01.xat24cr.x1d52u69 > section > div > form > div > div._aidp > div'
        time.sleep(random.randint(2, 5))
        # time.sleep(random.randint(5,7))
        driver.find_element(By.CSS_SELECTOR, replyButtonSelector).click()
        time.sleep(random.randint(1, 3))
        return True
    except Exception as e:
        print('댓글 달기 막아놓음 --> 다음 계정으로 이동합니다')
        print(e)
        return False
        # time.sleep(random.randint(4,7))


''''''


def getInstaName(driver):
    try:
        nameSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div.x4h1yfo > div > div.xyinxu5.x1pi30zi.x1g2khh7.x1swvt13 > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1 > div > div:nth-child(1) > div:nth-child(1) > div > span > span > div > a > div > div > span'
        time.sleep(random.randrange(4, 7))
        nameInput = driver.find_element(By.CSS_SELECTOR, nameSelector)
        nameText = nameInput.text
    except Exception as e:
        nameText = "이름 뽑기 실패 "
        print("인스타 이름가져오기 실패 ")
        print(e)
        pass
    return nameText


# 게시글 창에서 팔로우 누르기
def clickFollowers(driver):
    # mount_0_0_QV > div > div > div > div > div > div > div > div > div > section > main > div > div > div > div > div > div > div > div > div > div > div > div
    # followerSelector = 'div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > section > main > div > div > div > div > div > div > div > div > div > div > div > div'
    followerSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div.x4h1yfo > div > div.xyinxu5.x1pi30zi.x1g2khh7.x1swvt13 > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1 > div > div:nth-child(1) > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1 > div'

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, followerSelector)
    ))
    followerInput = driver.find_element(By.CSS_SELECTOR, followerSelector)
    try:
        if followerInput.text == "팔로우":
            followerInput.click()
            print("팔로우 눌렀어")
            time.sleep(random.randrange(1, 5))
        else:
            print("뭐야...?", followerInput.text)
            pass
    except Exception as e:
        print('팔로우 누르기 에러~~')
        print(e)
        pass


def removeRefueWord(introContent, deniedWord):
    # /로 들어온 금지단어들 배열로 변환
    if not deniedWord:
        print('금지단어 설정을 안했어!!')
        return False
    refuseKeyword = [comment.strip() for comment in deniedWord.split('/')]

    if any(keyword in introContent for keyword in refuseKeyword):
        print("금지단어 있네!!!")
        return True
    else:
        print("금지단어 없네..")
        return False


def refuseWord(deniedWord, driver):
    # 계정 => 소개글 셀렉터
    introSelector = 'div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > div:nth-child(2) > section > main > div > header > section > div > h1'
    # introSelector ='div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > div > section > main > div > div > h1'
    time.sleep(random.randrange(1, 3))
    try:
        introInput = driver.find_element(By.CSS_SELECTOR, introSelector)
        time.sleep(random.randrange(2, 5))
        introContent = introInput.text
        removeFlag = removeRefueWord(introContent, deniedWord)
        ## 금지단어가 있으면 True 없으면 False
        if removeFlag:
            return True
        else:
            return False
    except Exception as e:
        print('소개글이 없는 계정이네요 ! 방문합니다')
        return False


def firstLink(keyword, driver):
    # 들어갈 계정
    driver.get(f"https://www.instagram.com/{keyword}/")
    # 팔로워 목록 창
    followers = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > ul > li:nth-child(2) > a'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, followers)
    ))
    # 팔로워 클릭
    postInput = driver.find_element(By.CSS_SELECTOR, followers).click()
    time.sleep(5)
    # 팔로워 리스트 중 에서 스크롤 포함된 div 영역
    # followersList = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div'
    followersList = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano'
    links = []

    while len(links) < 30:
        postBox = driver.find_element(By.CSS_SELECTOR, followersList)
        postLink = postBox.find_elements(By.TAG_NAME, 'a')  # return []
        for i in range(6):
            try:
                # driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', postBox)
                driver.execute_script("arguments[0].scrollBy(0, 600)", postBox)
            except Exception as e:
                print(e)
                pass
            time.sleep(1)
        for i in range(len(postLink)):
            eachLink = postLink[i]
            link = eachLink.get_attribute('href')
            links.append(link)
        # 중복제거
        links = set(links)
        links = list(links)
    # 100개 링크..

    with open('links.txt', "w") as f:
        for links_list in links:
            f.write(f'{links_list}\n')
    print('1차 팔로워 목록 끝 ')


def secondLinks(reply, deniedWord, driver , followFlag,loveFlag):
    lines_to_keep = []
    with open('links.txt', 'r') as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            checkOpenFlag = checkOpen(line, driver)  ## true 면 비공개 false면 공개
            if not checkOpenFlag:
                lines_to_keep.append(line)
    print('공개 팔로워 계정 생성')
    # 공개만 고른 링크 txt 에 씀 -> 추 후 디비쓴다면 update 하면 될 듯
    with open('links_open.txt', 'w') as f:
        f.write('\n'.join(lines_to_keep))
    print("공개 팔로워 생성 완료")
    print(len(lines_to_keep), "명 입니다")

    for link_keep in lines_to_keep:
        driver.get(link_keep)
        time.sleep(random.randrange(1, 3))
        # 소개글에 광고성있으면 패스해버리기
        refuseYN = refuseWord(deniedWord, driver)
        if refuseYN:
            continue
        contentSelector = 'div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > div > section > main > div > div > article > div > div'
        time.sleep(random.randrange(4, 7))
        postBox = None
        postOneLink = None
        postCount = None

        try:
            postBox = driver.find_element(By.CSS_SELECTOR, contentSelector)
            postOneLink = postBox.find_elements(By.TAG_NAME, 'a')
            postCount = len(postOneLink)
        except Exception as e:
            print('긁으려는 셀렉터 못찾음 ')
            print(e)
            continue
        ## 게시글이 n개 이하면 무한루프 돌기 때문에 게시글 카운트 설정
        count = 0
        # 카운트 갯수를 게시글 갯수 보다 많이 잡으면 무한루프
        if postCount < 13:
            count = postCount
        else:
            count = 20
        linksContent = []
        while len(linksContent) < postCount:
            try:
                contentLink = postBox.find_elements(By.TAG_NAME, 'a')  # return []
                for i in range(3):
                    try:
                        driver.execute_script("window.scrollBy(0,600);")
                    except Exception as e:
                        print('스크롤 하다가 에러 남 ', e)
                        pass
                    time.sleep(1)
                # contentBox = driver.find_element(By.CSS_SELECTOR, contentSelector)

                for i in range(len(contentLink)):
                    eachLink_content = contentLink[i]
                    link = eachLink_content.get_attribute('href')
                    linksContent.append(link)
                    # 중복제거
                    linksContent = set(linksContent)
                    linksContent = list(linksContent)
            except Exception as e:
                print('게시글 긁기 에러다!!!!')
                print(e)
        with open('content_links.txt', "w") as f:
            for content in linksContent:
                f.write(f'{content}\n')

        print('게시글 내용 긁어오기 완료')
        content_list = []
        with open('content_links.txt', 'r') as f:
            while True:
                line = f.readline().rstrip()
                if not line:
                    break
                content_list.append(line)
        print('게시글 내용 읽어오기 완료')
        cnt = 0
        # reply = "선팔하고 갑니당 ㅎㅎ 맞팔하고 소통해요!!! / 피드 너무 예쁘네요,,, 제 피드도 님 피드 참고해서 예쁘게 꾸며볼게요~!! / 우와.. 피드 이쁘다.. 저도 참고하도록 선팔하구 갑니다 ㅎㅎ / 예쁜 피드에 눈요기 하구 팔로잉하고 갑니당 히히/wowowow / 좋아요꿀꿀"
        comments = [comment.strip() for comment in reply.split('/')]
        visited_links = []
        with open(f'visited_{loginData.id.strip()}.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                _link = line.rstrip()
                visited_links.append(_link)
        visited_account = []
        with open(f'account_{loginData.id.strip()}.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                _link = line.rstrip()
                visited_account.append(_link)
        # 계정이 올린 게시글 링크들
        for content in content_list:
            driver.get(content)
            time.sleep(random.randrange(3, 7))
            getContentTime = checkTime(driver)
            timeFlag = checkTimeResult(getContentTime)
            # 게시글에 있는 아이디 가져옴 .
            instaName = getInstaName(driver)
            # 들어온 아이디 에다가 댓글까지 썻엇으면
            if instaName in visited_account:
                continue
            # 들어와서 댓글쓴 게시글이면 패스  => 사실상 위에 것 만 필요하다
            if content in visited_links:
                continue
            else:
                # 계정당 하나만 댓글/좋아요 /팔로우
                if 30 > timeFlag:
                    replyFlag = inputReply(comments, driver)
                    # 댓글달기 성공했을 시에
                    if replyFlag:
                        if loveFlag == 1:
                            loveClick(driver)
                        if followFlag == 1:
                            clickFollowers(driver)
                            print("방문목록에 넣습니다~~")
                            with open(f'visited_{loginData.id.strip()}.txt', "a") as a:
                                a.write(f'{content}\n')
                            with open(f'account_{loginData.id.strip()}.txt', "a") as f:
                                f.write(f'{instaName}\n')
                        # 계정당 하나의 게시글만 합시다
                        time.sleep(random.randrange(3, 10))
                        break
                    # 댓글달기 막아놨으면 바로 다음 계정으로
                    else:
                        break
                else:
                    pass
                cnt += 1
                print('최근 7일 방문~~ ', cnt)

def workStart(keyword, reply, deniedWord, driver,followFlag,loveFlag):

    rs = False
    login(driver)
    firstLink(keyword, driver)
    secondLinks(reply, deniedWord, driver, followFlag,loveFlag)
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
    with open(f'start_time_{loginData.id.strip()}.txt', "a") as f:
        f.write(f'{formatted_time} end!! \n')
