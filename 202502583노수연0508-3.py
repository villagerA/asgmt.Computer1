#주제-2개이상의 자료를 저장해서 활용방법
#리스트[],튜플(),딕셔너리{}
myList=[1,2,3,4,5]
print(myList)
for i in range(0,5,1):
    print(myList[i])
'''
print(myList)
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[4])
'''
#리스트 다양한 함수 제공
myList.append(100)
print(myList)
myList.insert(2,350)
print(myList)
del(myList[1])
print(myList)
#튜플
myTuple = (10,20,30,40)
print(myTuple)
#myTuple.append(400)    AttributeError가 나는 것을 확인한 코드
#print(myTuple)
print('튜플의 자료')
'''
print(myTuple[0])
print(myTuple[1])
print(myTuple[2])
'''
print(myTuple[0]+myTuple[1]+myTuple[2])
#딕셔너리
myDic = {'apple':'사과','car':'자동차'}
numDic = {1:'one',2:'two'}
chDic = {'a':1,'b':2,'c':3}
print(myDic)
print(myDic['apple'])
print(myDic['car'])
print(numDic)
print(numDic[1])
print(numDic[2])
