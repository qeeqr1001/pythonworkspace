#-*- encoding: utf-8 -*-

import pandas as pd #pandas 이용
import pymysql
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL 
import konlpy
from konlpy.tag import Okt

okt=Okt()
con, cur = None, None
# conn = pymysql.connect(host='183.111.242.56', user='dosly2', password='maeil123',db='dosly2',port=3306, charset='utf8')

# conn.query("set character_set_connection=utf8;")
# conn.query("set character_set_server=utf8;")
# conn.query("set character_set_client=utf8;")
# conn.query("set character_set_results=utf8;")
# conn.query("set character_set_database=utf8;")


SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://dosly2:maeil123@dosly2.cafe24.com:3306/dosly2"
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI,echo=False)
qkeyword_data = pd.read_sql("SELECT * from word",engine)
print(qkeyword_data)

#word테이블에서 데이터 가져오고 배열만들기.
word_dic={} #word 배열
row=0
for rule in qkeyword_data["word_content"]:
    word_dic[row]=rule.split('\n')
    row+=1
print(word_dic)

# word_dic2=''.join(word_dic)

# print(word_dic2)




req = input('궁금한 점을 입력해보세요. ') 
nouns=okt.nouns(req) #질문 문장 형태소 분석
print(nouns)

def getresponse(req): 
    sql={}
    for i in range(len(nouns)):
        for j in range(len(word_dic)):
            # print(word_dic[j])
            strword=''.join(word_dic[j])
            if nouns[i]==strword:
                
                nouns[i]
                # sql=f"SELECT connect_questid FROM connect INNER JOIN word ON connect.connect_wordid=word.word_id WHERE word_content like'%{nouns[i]}%' "
                # sql2=f"SELECT quest_content FROM quest left JOIN connect ON quest.quest_id=connect.connect_questid left JOIN word ON connect.connect_wordid=word.word_id  WHERE word_content like'%{nouns[i]}%' "
                print(nouns[i]+"키워드가 word테이블에 있습니다.")
                print(strword)
                sql=f"SELECT quest_content FROM quest left JOIN connect ON quest.quest_id=connect.connect_questid left JOIN word ON connect.connect_wordid=word.word_id  WHERE word_content like'%{nouns[i]}%' "
                getsql(sql)
                
                # with conn:
                #     with conn.cursor() as cur:
                #         cur.execute(sql2)  
                #         result = cur.fetchall() 
                #         print(result)
                #         continue
            else:
                continue
      
    
def getsql(sql):
    results={}
    conn = pymysql.connect(host='183.111.242.56', user='dosly2', password='maeil123',db='dosly2',port=3306, charset='utf8')

    conn.query("set character_set_connection=utf8;")
    conn.query("set character_set_server=utf8;")
    conn.query("set character_set_client=utf8;")
    conn.query("set character_set_results=utf8;")
    conn.query("set character_set_database=utf8;")
    cur=conn.cursor()
           
    cur.execute(sql)
          
    result = cur.fetchall() 
    print(result)
    conn.close()

    # for i in range(len(nouns)):
    #     results[i]=result
    #     print(results[i])
    #     if i>1:
    #         if results[i]==results[i-1]:
    #             print(results[i])
    #         else:
    #             continue
    #     else:
    #         continue

   
                             
#반복문
while True: 
    if req == 'exit': 
        break 
    else:
        getresponse(req)
        break
    
