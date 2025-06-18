#주제-프로필파일을 프로그램에 가져오

#파일 열기
inFp = open('score.csv','r',encoding='utf-8')

#파일을 열어서 계산결과를 파일에 쓰기
outFp = open('score.csv','a',encoding='utf-8')

#처리구문
inStr = ''
while True:
    inStr = inFp.readline() #텍스트파일에 있는 자료를 리스트로 읽어옴
    print(inStr)
    if inStr == '': #읽어온 문자열이 아무것도 없다면 종료
        break
    jumsu = inStr.split(',') #구분자 , 로 문자열 분리
    print(jumsu)
    res = int(jumsu[0])+int(jumsu[1])+int(jumsu[2])
    print('결과:',res)
    outFp.write(','+str(res))
    #outFp.writelines(','+str(res))

    
#파일닫기
inFp.close()
print('파일읽기 종료!')

outFp.close()
print('결과 파일에 저장 완료!')
