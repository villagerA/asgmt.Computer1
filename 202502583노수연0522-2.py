#함수이해-지역변수,전역변수,리스트,딕셔너리 전달등
#import myModule1 as my
from myModule1 import *   #컴퓨터에서는 *는 모든값 의미
from myModule1 import fun5

#메인프로그램부분
a=20
fun1()
fun2()
fun3(1,2,3)
'''
fun3(1,2)
fun3(1)
fun3()
fun4(1,2,3) #매개변수를 필요한 만큼 전달
fun4(1,2,3,4,5,6,7,8,9,10)
fun5(트와이스=9,블랙핑크=4)
'''
