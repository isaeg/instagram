import time
import uiautomator2 as u2
import time

from uiautomator2 import Direction

serial = "R3CR30K5HJT"

keyWorld = "잠실 맛집"
d = u2.connect(serial)

links = []
with open('links.txt', 'r' ) as f:

    while True:
        line = f.readline()
        if not line:
            break
        links.append(line.rstrip())

cnt =1
for link in links:
    print(f'{cnt} 쨰 방문')
    d.open_url(link)

    input()
    cnt +=1
url = "https://www.instagram.com/dndosnepwpsbx/"
#adb shell 로 방문
# d.shell(f"am start -a android.intent.intent.action.VIWE -d {url}")
# input()

# open url
d.open_url(url)
input()