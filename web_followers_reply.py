import random
from typing import re

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
'''로그인 끝 '''
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
time.sleep(2)
btnInput.click()
time.sleep(6)

refuseKeyword = ['본계','재택','문의','부업','알바','원금','재테크']

def read_links():
    links = []
    with open('content_links.txt', "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            links.append(line.rstrip())
    return links


def closeClick():
    closeSelect = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x160vmok.x10l6tqk.x1eu8d0j.x1vjfegm > div > div > svg'
    driver.find_element(By.CSS_SELECTOR, closeSelect).click()


def loveClick():
    loveSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x1xp8e9x.x13fuv20.x178xt8z.x9f619.x1yrsyyn.x1pi30zi.x10b6aqq.x1swvt13.xh8yej3 > div.x6s0dn4.xrvj5dj.x1o61qjw > div.x78zum5 > span.xp7jhwk > div > div > span > svg'
    # loveSelector = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > section._aamu._ae3_._ae47._ae48 > span._aamw > div > div > span > svg'
    loveInput = driver.find_element(By.CSS_SELECTOR, loveSelector)
    loveCheck = loveInput.get_attribute("aria-label")
    if loveCheck == "좋아요":
        print("조하요 누를게요 ??")
        loveInput.click()
    else:
        print("이미 눌렀어용")
        pass


def checkTime():
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


def inputReply(comments):
    comment = random.choice(comments)
    time.sleep(random.randrange(5,7))
    replySelector = 'div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > section > main > div > div > div > div > div > div > section > div > form > div > textarea'

    try:
        # 댓글달기 셀렉터가 없다면 --> 댓글 달기 막아놓았다면 except 로 가서 False return
        replyInput = driver.find_element(By.CSS_SELECTOR, replySelector)
        time.sleep(random.randrange(2,5))
        ActionChains(driver).move_to_element(replyInput).click().send_keys(comment).perform()
        replyButtonSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div.x4h1yfo > div > div.xdj266r.xktsk01.xat24cr.x1d52u69 > section > div > form > div > div._aidp > div'
        time.sleep(random.randint(2,5))
        # time.sleep(random.randint(5,7))
        driver.find_element(By.CSS_SELECTOR,replyButtonSelector).click()
        time.sleep(random.randint(1,3))
        return True
    except Exception as e:
        print('댓글 에러!!!!!')
        print(e)
        return False
        # time.sleep(random.randint(4,7))

def getInstaName():
    try:
        nameSelector ='div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div.x4h1yfo > div > div.xyinxu5.x1pi30zi.x1g2khh7.x1swvt13 > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1 > div > div:nth-child(1) > div:nth-child(1) > div > span > span > div > a > div > div > span'
        time.sleep(random.randrange(4,7))
        nameInput = driver.find_element(By.CSS_SELECTOR, nameSelector)
        nameText = nameInput.text
    except Exception as e:
        nameText="이름 뽑기 실패 "
        print("인스타 이름가져오기 실패 ")
        print(e)
        pass
    return nameText


def removeRefueWord(introContent):
    if any(keyword in introContent for keyword in refuseKeyword):
        print("금지단어 있네!!!")
        return True
    else:
        print("금지단어 없네..")
        return False

def refuseWord():
    # 계정 => 소개글 셀렉터
    introSelector ='div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > div:nth-child(2) > section > main > div > header > section > div > h1'
    # introSelector ='div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > div > section > main > div > div > h1'
    time.sleep(random.randrange(1,3))
    try:
        introInput = driver.find_element(By.CSS_SELECTOR,introSelector)
        time.sleep(random.randrange(2,5))
        introContent = introInput.text
        removeFlag = removeRefueWord(introContent)
        ## 금지단어가 있으면 True 없으면 False
        if removeFlag:
            return True
        else:
            return False
    except Exception as e:
        print('소개글이 없는 계정이네요')
        return False

# keyword = "ichiman_lamb"
# driver.get(f"https://www.instagram.com/{keyword}/")

keep_list = []
with open('links_open_test.txt', 'r') as f:
    while True:
        line = f.readline().rstrip()
        if not line:
            break
        keep_list.append(line)
print('keep_list 리스트 가져왓다')

time.sleep(3)
## 장무녕게시글이겟지 ?




for keep in keep_list:
    driver.get(keep)
    time.sleep(4)
    ## False 라면 정상계정 True 라면 다음계정으로 이동
    refuseYN = refuseWord()
    if refuseYN:
        continue
    contentSelector = 'div[id^="mount_0_0"] > div > div > div > div > div > div > div > div > div > div > section > main > div > div > article > div > div'
    postBox = driver.find_element(By.CSS_SELECTOR, contentSelector)
    postOneLink = postBox.find_elements(By.TAG_NAME, 'a')  # return []
    postCount = len(postOneLink)
    count = 0
    paramCount = 20
    if postCount < 13:
        count = postCount
    else:
        count = paramCount
    print('아오진짜')
    print(postCount)
    links = []
    '''게시글 링크 긁어오기 '''
    while len(links) < postCount:
        try:
            # postBox = driver.find_element(By.CSS_SELECTOR, contentSelector)
            postLink = postBox.find_elements(By.TAG_NAME, 'a')  # return []
            for i in range(3):
                try:
                    driver.execute_script("window.scrollBy(0,600);")
                except Exception as e:
                    print('스크롤 하다가 에러 남 ', e)
                    pass
                time.sleep(1)

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

    with open('content_links_test.txt', "w") as f:
        for link in links:
            f.write(f'{link}\n')
    ''''''
    print('게시글 내용 긁어오기 완료')
    content_list = []
    with open('content_links_test.txt', 'r') as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            content_list.append(line)
    print('게시글 내용 읽어오기 완료')
    cnt = 0
    text = "선팔하고 갑니당 ㅎㅎ 맞팔하고 소통해요!!! / 피드 너무 예쁘네요,,, 제 피드도 님 피드 참고해서 예쁘게 꾸며볼게요~!! / 우와.. 피드 이쁘다.. 저도 참고하도록 선팔하구 갑니다 ㅎㅎ / 예쁜 피드에 눈요기 하구 팔로잉하고 갑니당 히히/wowowow / 좋아요꿀꿀"
    comments = [comment.strip() for comment in text.split('/')]
    visited_links = []
    with open('visited.txt','r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            _link = line.rstrip()
            visited_links.append(_link)

    for content in content_list:
        driver.get(content)
        time.sleep(3)
        getContentTime = checkTime()
        timeFlag = checkTimeResult(getContentTime)
        instaName = getInstaName()
        if content in visited_links:
            continue
        else:
            if timeFlag < 30:
                # loveClick()
                replyFlag = inputReply(comments)
                ## False 면 요기 탈출
                if not replyFlag:
                    continue
                # # 댓글 달면  게시글 링크 기록
                # with open('visited.txt', "a") as a:
                #     a.write(f'{content}\n')
                # with open('account.txt', "a") as f:
                #     f.write(f'{instaName}\n')
            else:
                pass
            cnt += 1
            print('최근 7일 좋튀 ', cnt)

# 첫번째 게시물 클릭하기~
# firstContent = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a'
# firstContentInput = driver.find_element(By.CSS_SELECTOR, firstContent)
# firstContentInput.click()
# time.sleep(3)
# 게시글 올린 시간  ~년~월~일
# getContentTime = checkTime()
# timeFlag = checkTimeResult(getContentTime)

# 오늘로부터 3개월 전 이라고 가정 함
# 3개월 이하면  좋아요 누르고 닫기
# if 90 > timeFlag:
#     loveClick()
#     closeClick()
# else:
#     closeClick()
#     pass

# input()
