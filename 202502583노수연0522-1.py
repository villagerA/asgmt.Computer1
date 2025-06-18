#함수 - 목적에 따라 만든 부프로그램
#함수정의부분

def line():
    print('---------------')

def abs(num):
    if num>0:
        print(num, '의 절대값은',num)
    if num<0:
        print(num, '의 절대값은',-num)

def add(n1,n2):
    res = n1+n2
    return res

#계산기 함수
def cal(n1,op,n2):  # cal(1,'+',2)
    result = 0
    if op=='+':
        result=n1+n2    #return n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1*n2
    else:
        result=n1/n2
    return result

def hap(n):
    tot=0
    for i in range(1,n+1,1):
        tot=tot+i
    print('1~',n,'의 합:',tot)

#메인프로그램
line()
abs(-56)
line()
result = add(23,45)+100
print('result=',result)
line()
print('계산기실행합니다')
n1=int(input('n1입력?'))
op=input('+,-,*,/ 중 하나 입력?')
n2=int(input('n2입력?'))
res = cal(n1,op,n2)
print('결과: ',n1,op,n2, '=',res)
line()
for i in range(3):
    n=int(input('1~n가지 더한 n값 입력?'))
    hap(n)
