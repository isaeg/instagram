import re
from datetime import datetime, timedelta
import loginData
import pymysql

conn = pymysql.connect(
    host = 'db.isaegad.gabia.io',
    port = 3306,
    user = 'isaegad',
    password = 'dltorrhkdrh2023',
    db = 'dbisaegad'
)
cursor = conn.cursor()
keyword='seoul_trends'
content = 'content'
instaName ='instaName'

insertVisitedSql = '''
   select VERSION  
   from tb_insta_ver
    where INSTA_VER_SEQ  = 
        (select max(INSTA_VER_SEQ) from tb_insta_ver)
'''
cursor.execute(insertVisitedSql)
row = cursor.fetchone()
print(row[0])
