#연속적으로 자료 저장할수있는 자료구조
#리스트,튜플,딕셔너리
#2차원 리스트,튜플...
list1 = []; list2=[]; list3=[];
##########
v1 = 1
for row in range(3):     #3번 반복
    for i in range(5):   #range(0,5,1)
        list1.append(v1)
        v1=v1+1
    list2.append(list1)  #추가
    list1=[]
    #print(list1)
##########
#문제1-2차원 리스트 자료 합계출력
tot=0 #변수선언
for row in range(3):
    for col in range(5):
        print(list2[row][col],end=' ') #각각의 위치에서 뽑아내겠다.
        tot=tot+list2[row][col]
    print()
print('총합계:',tot)
for row in range(3):
    print(list2[row]) #행단위로 뽑아내겠다

print(list2)
