#-*- encoding: utf-8 -*-
from encodings import utf_8
import pandas as pd #pandas 이용
import pymysql
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL 


con, cur = None, None
conn = pymysql.connect(host='183.111.242.56', user='dosly2', password='maeil123',db='dosly2',port=3306, charset='utf8')

conn.query("set character_set_connection=utf8;")
conn.query("set character_set_server=utf8;")
conn.query("set character_set_client=utf8;")
conn.query("set character_set_results=utf8;")
conn.query("set character_set_database=utf8;")
sql="SELECT * FROM quest"
with conn:
    with conn.cursor() as cur:
        
        cur.execute(sql)  
        result = cur.fetchall()
        print(result)

SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://dosly2:maeil123@dosly2.cafe24.com:3306/dosly2"
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI,echo=False)
qkeyword_data = pd.read_sql("SELECT * from quest",engine)
print(qkeyword_data)

