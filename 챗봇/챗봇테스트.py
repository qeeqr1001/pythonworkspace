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


userQuest = input("궁금한것을 물어보세요! ")
nouns=okt.nouns(userQuest) #질문 문장 형태소 분석
print(nouns)
print("수정")

#키워드가 데이터베이스 안에 있는지 찾고 있으면 답변 출력하는 반복문
while True: 
    for i in range(0,3): 
#sql = f"select ans_content from ans where ans_content like'%{nouns[0]}%' "
      
        if nouns[i]!=None:
            sql=f"SELECT ans_content FROM ans INNER JOIN quest ON quest.quest_id=ans.ans_id WHERE quest_keyword like'%{nouns[i]}%' "
           
            if sql!=None:
                
                with conn:
                 with conn.cursor() as cur:
                        cur.execute(sql)  
                        result = cur.fetchall() 
                        print(result) 
                 
            else:             
                print("일치하는 답변이 없습니다") #키워드가(혹은 일치하는 답변이) 데이터베이스 안에 없을 경우
                break
        else: #nouns[i]가 null값일 경우
        
            break








    
