from tkinter import *

root = Tk()
root.title("Instagram")
root.geometry("640x480") # 가로 * 세로
def on_text_click(event):
    id.delete("1.0", END)
    id.config(fg='black')

label = Label(root, text="계정명 :")
# label.pack(side=LEFT, padx=20, pady=40)
label.grid(row=1, column=0)
id = Text(root,width=20, height=1, fg='gray')
id.insert(END, "계정명을 입력하세요")
id.grid(row=1, column=1)
id.bind("<Button-1>", on_text_click)

label2 = Label(root, text="비번 :")
label2.grid(row=1,column=3)
pwd = Text(root,width=20, height=1)
pwd.grid(row=1, column=4)
pwd.insert(END, "비번을 입력하세요")


label3 = Label(root, text="방문 할 계정 :")
label3.grid(row=2,column=0)
toAccount = Text(root,width=20, height=1)
toAccount.grid(row=2, column=1)
toAccount.insert(END, "방문할 계정 명")

label4 = Label(root, text="댓글 :")
label4.grid(row=3,column=0)
reply = Text(root,width=20, height=1)
reply.grid(row=3, column=1)
reply.insert(END, "a/b/c --> / 로 구분해주세용")

label5 = Label(root, text="금지 단어:")
label5.grid(row=4,column=0)
deniedWord = Text(root,width=20, height=1)
deniedWord.grid(row=4, column=1)
deniedWord.insert(END, "a,b,c --> ,로 구분")

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="팔로우", variable=chkvar)
chkbox.select() # 자동 선택 처리
chkbox.deselect() # 선택 해제 처리
chkbox.grid()
#
chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="좋아요", variable=chkvar2)
chkbox2.grid()
def btncmd():
    # 내용 출력
    print(id.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(pwd.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(toAccount.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(deniedWord.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(reply.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    # print(e.get())
    # print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    # print(chkvar2.get())

    # 내용 삭제
    id.delete("1.0", END)
    pwd.delete("1.0", END)
    toAccount.delete("1.0", END)
    deniedWord.delete("1.0", END)
    reply.delete("1.0", END)
    # e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.grid()

root.mainloop()