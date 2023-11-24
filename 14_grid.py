import threading
import time
from uiautomator2 import Direction
import loginData
import web_followers
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


def mainStart(progress_window):
    for i in range(20):
        time.sleep(1)
        # print('테스트중입니다..', i)
        progress_window.update()


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
progress = ttk.Progressbar(root, length=300, maximum=20)
progress.grid(row=6, column=1)

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
    # print(id.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    # print(pwd.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    # print(toAccount.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    # print(reply.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    # print(deniedWord.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    # print(e.get())
    # print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    # print(chkvar2.get())

    getid = id.get("1.0", END)
    getpwd = pwd.get("1.0", END)
    # 아이디 비번 셋
    loginData.id = getid
    loginData.pwd = getpwd

    refuseReply = reply.get("1.0", END)

    refusedWord = deniedWord.get("1.0", END)
    # if getid.strip() == default_id or not getid.strip():
    #     messagebox.showinfo("경고", "계정을 입력하세요")
    #     return
    # if getpwd.strip() == default_pwd or not getpwd.strip():
    #     messagebox.showinfo("경고", "계정 비번을 입력하세요")
    #     return
    # if refuseReply.strip() == default_reply or not refuseReply.strip():
    #     messagebox.showinfo("경고", "작성할 댓글을 달아주세요.")
    #     return
    # if refusedWord.strip() == default_deniedWord or not refusedWord.strip():
    #     messagebox.showinfo("경고", "금지 단어를 설정하세요")
    #     return
    # 내용 삭제
    id.delete("1.0", END)
    pwd.delete("1.0", END)
    toAccount.delete("1.0", END)
    deniedWord.delete("1.0", END)
    reply.delete("1.0", END)
    # e.delete(0, END)
    progress_label2 = Label(root, text="작업 진행 중...")
    progress_label2.grid(row=6, column=1, pady=10)  #


    def long_task():
        mainStart(progress_label2)
        root.after(0, handle_result(progress_label2))

    threading.Thread(target=long_task()).start()
    # progress.stop()


def handle_result(progress_window):
    # 여기에 메인 스레드에서 결과를 처리하는 코드 추가
    progress_window.config(text="끝!!!")
    pass


btn = Button(root, text="클릭", command=btncmd)
btn.grid()
root.mainloop()
