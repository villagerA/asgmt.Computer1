#1.영어단어를 입력하면 한글 단어를 알려주는 프로그램을 입력하라
#2.항공우주공학개론
#3.음식레시피

korEng={'자동차':'car','사과':'apple'}

inData = input('한글 단어 입력?')
print(inData, '는 영어로 ', korEng[inData])

print()

aeroDic = {'대기':'행성을 둘러싸고 있는 기체층',
           '밀도':'유체의 단위부피당 질량',
           '온도':'유체의 에너지 레벨의 정량적 수치'}
aeroW = input('항공우주공학개론 관련 단어를 입력하시오 : ')
print(aeroW, '는', aeroDic[aeroW],'(이)다.')

print()

foodDic = {'라면': '1.물을 500ml넣고 끓이기...'
           ,
           '김밥': '1.재료준비 (당근,시금치,김 ...)'}
foodName = input('음식이름을 쓰면 레시피를 알려드립니다')
print(foodDic[foodName])
