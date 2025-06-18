#함수정의부분
def fun1():
    global a
    a=10
    print('a =',a)
def fun2():
    print('a =',a)
    
def fun3(n1=0,n2=0,n3=0):
    res=n1+n2+n3
    print('결과:',res)

def fun4(*para):    #튜플 매개변수로
    res=0
    for i in para:  #ex)(1,2,3)
        res=res+i
    print('res=',res)

def fun5(**para):   #딕셔너리 형식으로 전달
    for key in para.keys(): #키-값 로 전달
        print(key,'--->',para[key])
