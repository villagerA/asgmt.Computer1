#메인프로그램 작성할 파일

from mymodule0529 import *  #* 모든 값 의미

#절대값 함수 호출
num = int(input('n값 입력?'))
abs(num)

#내부함수 호출
res = outF(10,20)
print('res=',res)

#곱셈함수 호출
res = mul(3)
print('res=',res)
res = mul2(3,5)     #람다로 정의한 함수 호출
print('res=',res)

#카운트함수 호출
count(10)

#팩토리얼함수 호출
res = fact(5)
print('\n결과=',res)

#n의 값 입력해서 합 결과 출력 함수 호출
n = int(input('n값 입력?'))
hap(n)

#학점계산함수 호출
score = int(input('score값 입력?'))
grade(score)
