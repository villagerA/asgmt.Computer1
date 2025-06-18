#다양한 함수 정의해서 모듈로 만들겠다
#절대값함수

def abs(num=0):  #기본값 0으로 정의했다
    if num>0:
        print('num=',num)
    elif num<0:
        print('num=',-num)  # -num은 -1 * num 같다
    else:   #num==0
        print('num값은 0일수 없습니다')

#내부함수 : 함수 정의내에 함수를 또 정의하는 함수
def outF(v1,v2):
    def inF(n1,n2):
        return n1+n2
    return inF(v1,v2)   #outF를 불러서 리턴처리

#2개값 곱셈 함수
def mul(n1=1,n2=1):
    return n1*n2

#mul함수를 람다형으로 추가정의
mul2 = lambda n1,n2 : n1*n2

#재귀함수
#재귀함수1
def selCal():
    print('하',end='')
    selCal()    #자기자신의 함수를 호출

#재귀함수2 - 카운트함수
def count(num):
    if num>=1:
        print(num,end=' ')
        count(num-1)
    else:   #1보다 작을때 멈춘다
        return

#재귀함수 - 팩토리얼함수
def fact(n):
    if n>1:
        return n * fact(n-1)
    else:
        return n

#mymodule0529.py    파일이름을 다른이름으로 저장해주세요 

#주제1 - n값을 입력받아 합계출력 함수


def hap(n):
    tot=0
    for i in range(1,n+1,1):
        tot = tot + i
    print('1~',n,'의 합:',tot)

#학점계산함수 만들어주세요 (100 기준으로 A,F학점 출력)
def grade(score):
    if score>=90:
        print('A 입니다.')
    elif score>=80:
        print('B 입니다.')
    elif score>=70:
        print('C 입니다.')
    elif score>=50:
        print('E 입니다.')
    else:
        print('F 입니다.')
