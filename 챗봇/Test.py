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

sql = "SELECT quest_keyword FROM ans INNER JOIN quest ON quest.quest_id=ans.ans_id "

with conn:
    with conn.cursor() as cur:
        cur.execute(sql)  
        result = cur.fetchall() 
        print(result) 
        keyList=list(result)
        keySubList=list(keyList)
        print(keySubList[0])
            
        


   
