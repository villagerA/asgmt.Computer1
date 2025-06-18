#다양한 함수 정의해서 모듈로 만들겠다
#절대값함수

def abs(num=):  #기본값 0으로 정의했다
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
mul2 = ramda n1,n2 : n1*n2

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
        break

#재귀함수 - 팩토리얼함
def fact(n):
    if n>=1:
        return n * fact(n-1)
    else:
        break
