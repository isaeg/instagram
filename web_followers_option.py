import random

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


def closeClick():
    closeSelect = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x160vmok.x10l6tqk.x1eu8d0j.x1vjfegm > div > div > svg'
    driver.find_element(By.CSS_SELECTOR, closeSelect).click()


def loveClick():
    loveSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x1xp8e9x.x13fuv20.x178xt8z.x9f619.x1yrsyyn.x1pi30zi.x10b6aqq.x1swvt13.xh8yej3 > div.x6s0dn4.xrvj5dj.x1o61qjw > div.x78zum5 > span.xp7jhwk > div > div > span > svg'
    #loveSelector = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > section._aamu._ae3_._ae47._ae48 > span._aamw > div > div > span > svg'
    loveInput = driver.find_element(By.CSS_SELECTOR, loveSelector)
    loveCheck = loveInput.get_attribute("aria-label")
    if loveCheck == "좋아요":
        print("조하요 누를게요 ??")
        loveInput.click()
    else:
        print("이미 눌렀어용")
        pass


def checkTime():
    contentTimeSelector='div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x1xp8e9x.x13fuv20.x178xt8z.x9f619.x1yrsyyn.x1pi30zi.x10b6aqq.x1swvt13.xh8yej3 > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1yztbdb.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1 > div > a > span > time'
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
# 댓글남기기
def inputReply(comments):
    time.sleep(random.randrange(5,7))
    replySelecor = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div.x4h1yfo > div > div.xdj266r.xktsk01.xat24cr.x1d52u69 > section > div > form > div > textarea'
    replyButtonSelector = 'div[id^="mount_0_0"] > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div.x4h1yfo > div > div.xdj266r.xktsk01.xat24cr.x1d52u69 > section > div > form > div > div._aidp > div'
    replyInput = driver.find_element(By.CSS_SELECTOR, replySelecor)
    comment = random.choice(comments)
    try:
        replyInput.send_keys(comment)
        time.sleep(random.randint(1, 3))
    except Exception as e:
        print(e)
        pass
        # time.sleep(random.randint(4,7))
    time.sleep(random.randint(4,7))
    driver.find_element(By.CSS_SELECTOR,replyButtonSelector).click()

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


with open('content_links.txt', ---"w") as f:
    for link in links:
        f.write(f'{link}\n')

print('게시글 내용 긁어오기 완료')
contnet_list = []
with open('content_links.txt', 'r') as f:
    while True:
        line = f.readline().rstrip()
        if not line:
            break
        contnet_list.append(line)
print('게시글 내용 읽어오기 완료')
cnt =0
for list in contnet_list:
    driver.get(list)
    time.sleep(3)
    getContentTime = checkTime()
    timeFlag = checkTimeResult(getContentTime)
    if 7 > timeFlag:
        loveClick()
        # closeClick()
        with open('visited.txt', "a") as a:
            for link in links:
                a.write(f'{link}\n')
    else:
        # closeClick()
        pass
    input()
    cnt += 1
    print('최근 7일 좋튀 ',cnt)

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
