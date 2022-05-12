import pymysql

# 전역변수 선언부
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row=None

# 메인 코드
conn = pymysql.connect(host='localhost', user='root', password='202003446', db='chattest', charset='utf8')
cur = conn.cursor()

print("궁금한 키워드를 물어보세요.")

# 조회결과가 cur에 들어간다.
sql = "select * from answer where keyword=%s"
cur.execute(sql, ('학생증'))
 


print("키워드    질문    답변       ")
print("----------------------------------------------------")

while (True) :
    # fetchone()으로 한 행씩 가져오기
    row = cur.fetchone()
    if row== None :
        break
    data1,data2,data3 = row
    print("%5s   %15s   %15s  " % (data1, data2, data3))

conn.close()