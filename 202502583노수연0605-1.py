#주제-윈도우프로그램제작해보자
'''
from tkinter import *

win1 = Tk()
win2 = Tk()     #생성자

win1.title('윈도우1')
win1.geometry('300x300')
win1.resizable(width=FALSE,height=FALSE)
#win1.resizable(width=False,height=False) false 대소문자 상관 무

win2.title('윈도우2')
win2.geometry('500x300')

win1.mainloop()
win2.mainloop()
'''

from tkinter import *

win1 = Tk()
win1.title('윈도우1')
win1.geometry('300x300')
win1.resizable(width=FALSE,height=FALSE)

#위젯을 생성해서 윈도우에 올리자
la1=Label(win1,text='버튼을 누르면 윈2가 열림')

def fun1(): #처리할 함수정의
    win2=Tk()
    win2.title('윈도우2')
    win2.geometry('500x200')
    win2.mainloop()

btn1=Button(win1,text='윈2',width=20,command=fun1)
btn2=Button(win1,text='종료',width=20,command=quit) #quit 윈도우 X버튼
#위젯배치방법
la1.pack() #배치하지 않으면 윈도우에 올라갈 수 없음. 이거 있어야 보임!
btn1.pack()
btn2.pack()

win1.mainloop()
