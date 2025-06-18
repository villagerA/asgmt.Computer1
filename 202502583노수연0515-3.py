#set은 키만 모아놓은 딕셔너리의 특수한 형태
myset1 = {1,2,3,3,3,4,5,5}
print(myset1)
saleList = ['김밥','김밥','바나나','도시락','김밥']
print(saleList)
print(set(saleList))
print(tuple(saleList))
print(list(myset1))

#set 교집합등
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}
print(set1 & set2)
print(set1 | set2)
setList = set1 - set2
print(setList)
print(list(setList))
#컴프리헨션
numList = [num for num in range(1,11) if num%2==0]
#numList = [num for num in range(1,11)]
print(numList)
#리스트복사
set1List = list(set1)
set2List = list(set2)

testList = set1List
print(testList)
print(set1List)
testList.append(100)
print(testList)
print(set1List)
set1List.append(200)
print(testList)
print(set1List)
#깊은복사
deepList = set2List[:]
print(deepList)
print(set2List)
deepList.append(100)
print(deepList)
print(set2List)
set2List.append(345)
print(deepList)
print(set2List)
