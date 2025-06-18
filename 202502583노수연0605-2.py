#윈도우프로그래밍2
#주제-2개의값 입력받아 결과 출력
from tkinter import *
win = Tk()
win.title('계산프로그램-제작:이름')
win.geometry('500x300')

#윈도우에 올릴 위젯 객체 생성
la1 = Label(win,text='첫번째값:')
la2 = Label(win,text='두번째값:')
la3 = Label(win,text='결　　과:')
e1 = Entry(win,width=20)
e2 = Entry(win,width=20)
e3 = Entry(win,width=20)
result = Entry(win,width=20)
def add():
    n1 = int(e1.get())
    n2 = int(e2.get())
    res = n1 + n2
    result.insert(0,str(res))
btn1 = Button(win,text='덧셈계산',command=add)
def reset():
    e1.delete(0,len(e1.get()))
    e2.delete(0,len(e2.get()))
    result.delete(0,len(result.get()))
btn2 = Button(win,text='초기화',command=reset)
def add():
    n1 = int(e1.get())
    n2 = int(e2.get())
    res = n1 - n2
    result.insert(0,str(res))
btn3 = Button(win,text='뺄셈계산',command=add)

#윈도우에 위젯 올리기
la1.place(x=50,y=50)
e1.place(x=130,y=50)
la2.place(x=50,y=100)
e2.place(x=130,y=100)
la3.place(x=50,y=150)
e3.place(x=130,y=150)
result.place(x=130,y=150)
btn1.place(x=130,y=200)
btn2.place(x=50,y=200)
btn3.place(x=200,y=200)
win.mainloop()
