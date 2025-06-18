#주제-파일입출력
#1.텍스트파일에 자료 저장하기
outF = None
outStr = ''

#저장할 파일을 오픈한다
outF = open('profile.txt','a',encoding='utf-8') 

#파일에 처리할 내용 작성
print('프로필 정보 입력하세요 :')
while True:
    outStr = input('프로필작성:')
    if outStr!='':
        outF.writelines(outStr + ' ')
    else:
        break


#파일 닫기
outF.close()
print('파일 저장 완료!')
