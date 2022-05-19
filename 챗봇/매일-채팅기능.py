#-*- encoding: utf-8 -*-
import numpy as np
import pandas as pd #pandas 이용
import pymysql
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL 
import konlpy
from konlpy.tag import Okt
from collections import Counter

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
    word_dic[row]=rule.split()
    row+=1
print(word_dic)

# word_dic2=''.join(word_dic)

# print(word_dic2)




req = input('궁금한 점을 입력해보세요. ') 
nouns=okt.nouns(req) #질문 문장 형태소 분석
print(nouns)


def getresponse(req): 
    count=0
    
    for i in range(len(nouns)):
        for j in range(len(word_dic)):
            # print(word_dic[j])
            strword=''.join(word_dic[j])
            if nouns[i]==strword:
                count+=1
                # sql=f"SELECT connect_questid FROM connect INNER JOIN word ON connect.connect_wordid=word.word_id WHERE word_content like'%{nouns[i]}%' "
                # sql2=f"SELECT quest_content FROM quest left JOIN connect ON quest.quest_id=connect.connect_questid left JOIN word ON connect.connect_wordid=word.word_id  WHERE word_content like'%{nouns[i]}%' "
                print(nouns[i]+"키워드가 word테이블에 있습니다.")
                print(strword)
                sql=f"SELECT quest_content FROM quest left JOIN connect ON quest.quest_id=connect.connect_questid left JOIN word ON connect.connect_wordid=word.word_id  WHERE word_content like'%{nouns[i]}%' "
                
                getsql(sql) #sql문 실행하는 함수.
                
            else:
                continue
           
        
        
 
    resultf=list(sum(results,())) #results(2차원배열)을 resultf(1차원 배열)로 펼침
    #print(resultf)
    sameQ(resultf)
    



            
      
results=[]
resultf=[]
def getsql(sql): #sql문 실행 후 그 값을 results 배열에 넣는 함수.
    
    conn = pymysql.connect(host='183.111.242.56', user='dosly2', password='maeil123',db='dosly2',port=3306, charset='utf8')

    conn.query("set character_set_connection=utf8;")
    conn.query("set character_set_server=utf8;")
    conn.query("set character_set_client=utf8;")
    conn.query("set character_set_results=utf8;")
    conn.query("set character_set_database=utf8;")
    cur=conn.cursor()
           
    cur.execute(sql)
    
              
    result = cur.fetchall() 
    # print(result)
    conn.close()
    results.append(result)
    
def getsql2(sql2): #sql문 실행 후 그 값을 results 배열에 넣는 함수.
    
    conn = pymysql.connect(host='183.111.242.56', user='dosly2', password='maeil123',db='dosly2',port=3306, charset='utf8')

    conn.query("set character_set_connection=utf8;")
    conn.query("set character_set_server=utf8;")
    conn.query("set character_set_client=utf8;")
    conn.query("set character_set_results=utf8;")
    conn.query("set character_set_database=utf8;")
    cur=conn.cursor()
           
    cur.execute(sql2)
    
              
    result2 = cur.fetchall() 
    print(result2)
    # print(result)
    conn.close()
   
    
    
    
#ct함수
def sameQ(resultf): #모든 키워드 일치 질문 찾는 함수
    
    keys=[]
    values=[]

    
    
    #same에서 중복되는 값을 찾아 출력하기. 
    result_count=Counter(resultf)    
    for key,value in result_count.items():  
        values.append(value)
        keys.append(key)        
        # print(keys)
        # print(values)
    
    m=max(values) #m=value의 최댓값
    #print(m)
    ml=[] #키워드 가장 많이 일치하는 질문 리스트
    # for i, v in enumerate(values):
    for i in range(len(values)):
        if values[i]==m:
            ml.append(keys[i])
    print("사용자 질문 키워드 모두 일치하는 질문")
    print(ml)
    selectQuest(ml) #사용자가 직접 질문 고르는 함수 실행.
    

                    
    
def selectQuest(ml):

    user_Select=int(input("원하는 질문의 번호를 선택해주세요."))-1
    
    
    for i in range(len(ml)):
        if i==user_Select:
            print("사용자가 선택한 질문")
            print(ml[i])
            mlword=''.join(ml[i])
            sql2=f"SELECT ans_content FROM answer INNER JOIN quest ON answer.ans_id=quest.quest_id  WHERE quest_content like'%{mlword}%' "
            print("질문과 일치하는 대답")
            getsql2(sql2)
            



# def sameQ(i):
        
#         for j in range(len(results[i])):
            
#             for n in range(len(results[i])):
        
#                 if i>0:
                    
#                     if results[i][j]==results[i-1][n]:
                    
#                         same.append(results[i][j])
#                         # print(results[i][n])
#                         # same.append(results[i][j])
#                         # return same
                        
#                     else:
#                         same.append(results[i][j])
#                         continue
#                 else:
                
#                     continue
#         print(results)
        
       
            
            
                             
#반복문
while True: 
    if req == 'exit': 
        break 
    else:
        getresponse(req)
        break
    
