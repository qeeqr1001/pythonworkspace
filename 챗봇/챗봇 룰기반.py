import pandas as pd #pandas 이용
import pymysql
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import konlpy
from konlpy.tag import Okt

okt=Okt()
con, cur = None, None
conn = pymysql.connect(host='localhost', user='root', password='1234',db='chatbot',port=3307, charset='utf8')

#pd.read_sql로 데이터베이스 데이터를 불러와 변수에 저장
#pandas는 sqlite3를 지원하기때문에 그게 아닌건 엔진을 만들어서 url을 통해서 접속
SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://root:1234@localhost:3307/chatbot"
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI,echo=False)
qkeyword_data = pd.read_sql("SELECT quest_keyword from quest",engine)
print(qkeyword_data)

#|기준으로 나누고 리스트에 넣음.
qkeyword_dic={} #quest_keyword 배열
row=0
for rule in qkeyword_data["quest_keyword"]:
    qkeyword_dic[row]=rule.split('|') 
    row+=1
print(qkeyword_dic)
print(qkeyword_dic[0][1])


req = input('궁금한 점을 입력해보세요. ') 
nouns=okt.nouns(req) #질문 문장 형태소 분석
print(nouns)
    
def getresponse(req):  
               
    for i in range(0,7):
        count=0
        for j in range(0,2):
            if nouns[j]== qkeyword_dic[i][j]:
                count+=1
            
            if count>=2:
                sql=f"SELECT ans_content FROM ans INNER JOIN quest ON quest.quest_id=ans.ans_id WHERE quest_keyword like'%{qkeyword_dic[i][j]}%' "
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(sql)  
                        result = cur.fetchall() 
                        print(result)
                             
           
                
#반복문
while True: 
    if req == 'exit': 
        break 
    else:
        getresponse(req)
        break
        

        




