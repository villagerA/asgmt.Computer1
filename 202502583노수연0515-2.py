#2차원리스트
aList = [[1,2,3],
         [4,5,6],
         [7,8,9]]
bList=[]

print(aList[1][1])
print(aList[2][0])
print('자료출력')

for row in range(3):
    for col in range(3):
        print(aList[row][col],end=' ')
    print()
    
#불규칙한 2차원 리스트인 경우 자료추출
d1=[1,2,3,4,5]; d2=[10,20]; d3=[11,12,13,14];
CList=[[1,2,3,4,5],
       [10,20],
       [11,12,13,14]]
print(CList)

for row in range(3):
    for col in range(len(CList[row])):
        print(CList[row][col],end=' ')
    print()

#문제2-행별로 일부 자료만 추출해보자
print(CList[0][1:3])
print(CList[1][1])
print(CList[2][1:])
print(CList[0:2][0:2]) #[:] 모두뽑아라
