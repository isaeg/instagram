import threading
import time
from selenium import webdriver
from tkinter import messagebox
import loginData
import web_followers
import web_followers_db
from tkinter import *
from tkinter import ttk

# 방문할 계정 으로 합시다 .
root = Tk()
root.title("Instagram")
root.geometry("640x480")  # 가로 * 세로


def on_id_click(event):
    id.delete("1.0", END)
    id.config(fg='black')


def on_pwd_click(event):
    pwd.delete("1.0", END)
    pwd.config(fg='black')


def on_toAccount_click(event):
    toAccount.delete("1.0", END)
    toAccount.config(fg='black')


def on_reply_click(event):
    reply.delete("1.0", END)
    reply.config(fg='black')


def on_deniedWord_click(event):
    deniedWord.delete("1.0", END)
    deniedWord.config(fg='black')


def mainStart(keyword, reply, deniedWord, progress_label2, followFlag, loveFlag):
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36')
    options.add_argument("--disable-logging")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    # keyword_list = ["seoul_trends"]
    # for keyword in keyword_list:
    #     # 해시태그 띄어쓰기 사용 불가, 필터링 기능
    #     keyword = keyword.replace(" ", "")
    #     web_followers.workStart(keyword, reply, deniedWord)

    web_followers_db.workStart(keyword, reply, deniedWord, driver, followFlag, loveFlag)
    driver.quit()
    print("[작업 완료] - 자동화 프로그램 동작이 완료되었습니다.")


label = Label(root, text="계정명 :")
# label.pack(side=LEFT, padx=20, pady=40)
label.grid(row=1, column=0)
default_id = "계정을 입력하세요"
id = Text(root, width=20, height=1, fg='gray')
id.insert(END, default_id)
id.grid(row=1, column=1)
id.bind("<Button-1>", on_id_click)

label2 = Label(root, text="비번 :")
label2.grid(row=1, column=3)
default_pwd = '비번을 입력하세요'
pwd = Text(root, width=20, height=1, fg='gray')
pwd.grid(row=1, column=4)
pwd.insert(END, default_pwd)
pwd.bind("<Button-1>", on_pwd_click)

label3 = Label(root, text="방문 할 계정 :")
label3.grid(row=2, column=0)
default_toAccount = '방문할 계정 명'
toAccount = Text(root, width=20, height=1, fg='gray')
toAccount.grid(row=2, column=1)
toAccount.insert(END, default_toAccount)
toAccount.bind("<Button-1>", on_toAccount_click)

label4 = Label(root, text="댓글 :")
label4.grid(row=3, column=0)
default_reply = 'a/b/c --> / 로 구분'
reply = Text(root, width=20, height=5, fg='gray')
reply.grid(row=3, column=1)
reply.insert(END, default_reply)
reply.bind("<Button-1>", on_reply_click)

label5 = Label(root, text="금지 단어:")
label5.grid(row=4, column=0)

default_deniedWord = "a/b/c --> /로 구분"
deniedWord = Text(root, width=20, height=5, fg='gray')
deniedWord.grid(row=4, column=1)
deniedWord.insert(END, default_deniedWord)
deniedWord.bind("<Button-1>", on_deniedWord_click)

label6 = Label(root, text="진행상황:")
label6.grid(row=5, column=0)

chkvar = IntVar()  # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="팔로우", variable=chkvar)
chkbox.select()  # 자동 선택 처리
chkbox.deselect()  # 선택 해제 처리
chkbox.grid()
#
chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="좋아요", variable=chkvar2)
chkbox2.grid()


def btncmd():
    # 내용 출력
    print(id.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(pwd.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(toAccount.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(reply.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(deniedWord.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(chkvar.get(), type(chkvar.get()))
    print(chkvar2.get(), type(chkvar2.get()))
    # print(e.get())
    # print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    # print(chkvar2.get())

    getid = id.get("1.0", END)
    getpwd = pwd.get("1.0", END)
    getAccount = toAccount.get("1.0", END)
    # 아이디 비번 셋
    loginData.id = getid
    loginData.pwd = getpwd

    refuseReply = reply.get("1.0", END)

    refusedWord = deniedWord.get("1.0", END)

    followFlag = chkvar.get()
    loveFlag = chkvar2.get()
    if getid.strip() == default_id or not getid.strip():
        messagebox.showinfo("경고", "계정을 입력하세요")
        return
    if getpwd.strip() == default_pwd or not getpwd.strip():
        messagebox.showinfo("경고", "계정 비번을 입력하세요")
        return
    if getAccount.strip() == default_toAccount or not getAccount.strip():
        messagebox.showinfo("경고", "방문할 계정을 입력하세요")
        return
    if refuseReply.strip() == default_reply or not refuseReply.strip():
        messagebox.showinfo("경고", "작성할 댓글을 달아주세요.")
        return
    if refusedWord.strip() == default_deniedWord or not refusedWord.strip():
        messagebox.showinfo("경고", "금지 단어를 설정하세요")
        return
    # 내용 삭제
    id.delete("1.0", END)
    pwd.delete("1.0", END)
    toAccount.delete("1.0", END)
    deniedWord.delete("1.0", END)
    reply.delete("1.0", END)
    # e.delete(0, END) btn.config(state="disabled")

    progress_label2 = Label(root, text="작업 진행 중...")
    progress_label2.grid(row=5, column=1, pady=10)  #
    btn.config(state="disabled")

    def long_task():
        mainStart(getAccount, refuseReply, refusedWord, progress_label2, followFlag, loveFlag)
        root.after(0, lambda: handle_result(progress_label2))

    threading.Thread(target=long_task).start()
    # progress.stop()


def handle_result(progress_label2):
    progress_label2.config(text="끝!!!")
    btn.config(state="normal")
    return


btn = Button(root, text="클릭", command=btncmd)
btn.grid()
root.mainloop()
''' static '''
# deniedWord = '본계/재택/문의/부업/알바/원금/재테크/수익률'
# followFlag = False
# replyFlag = False
# LoveFlag = False
# reply = "선팔하고 갑니당 ㅎㅎ 맞팔하고 소통해요!!! / 피드 너무 예쁘네요,,, 제 피드도 님 피드 참고해서 예쁘게 꾸며볼게요~!! / 우와.. 피드 이쁘다.. 저도 참고하도록 선팔하구 갑니다 ㅎㅎ / 예쁜 피드에 눈요기 하구 팔로잉하고 갑니당 히히/wowowow / 좋아요꿀꿀"
