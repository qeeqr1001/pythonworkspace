#챗봇프로그램

import pymysql


conn = pymysql.connect(host='localhost', user='root', password='202003446', db='chattest', charset='utf8')
cur = conn.cursor()
# 대부분 아래 두줄은 안쓴다 db에 이미 테이블이 만들어져있는 경우가 대부분
sql = "create table if not exists usertable(keyword char(4),question char(15), answer char(20)"
cur.execute(sql) # 실행

while (True) :
    data1 = input("keyword ==> ")
    if data1 == "" :
        break;
    data2 = input("질문 ==> ")
    data3 = input("답변==> ")
    # 입력받은 정보로 insert문 작성 
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + ")"
    cur.execute(sql) # 실행
conn.comint()
conn.close() #데이터베이스 닫기
