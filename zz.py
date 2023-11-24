import re
from datetime import datetime, timedelta
import loginData
visited_account = []
try:
    with open('a2.txt', 'r') as f:
        f.readline()
        print('ㅋㅋ 있네')
except Exception as e:
    with open('a2.txt', 'a') as f:
        f.write(f'hello!{loginData.id.strip()}')
        print('ㅋㅋ없네')
pass
