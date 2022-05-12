import konlpy
from konlpy.tag import Okt
import pymysql

# 전역변수 선언부
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row=None
okt=Okt()


# 메인 코드
conn = pymysql.connect(host='localhost', user='root', password='1234',db='chatbot',port=3307, charset='utf8')




# quest_keyword 배열로 받기
sqlK = "SELECT quest_keyword FROM ans INNER JOIN quest ON quest.quest_id=ans.ans_id "

with conn.cursor() as cur:
    cur.execute(sqlK)  
    result = cur.fetchall() 
    keyList = list(result) 
    print(keyList)
    for i in keyList:
        print(keyList[i])
        print("!")
        


   
