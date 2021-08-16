# coding=utf-8
import requests
from bs4 import BeautifulSoup

# 上課節數（可能因暑輔而有所影響，可自行調整使程式正常運行）
classNum = 6 # 暑輔
# classNum = 8 # 平常

# 學期代碼（基本上不需要更換）
semesterId = "1101101"

classId = str(input('請輸入想查詢的班級：'))
r = requests.get("http://acdm3.tcssh.tc.edu.tw/csv3_web/SF4.ASP?CLA_NO=" + semesterId + classId)
r.encoding = 'big5-hkscs'
r = r.content
soup = BeautifulSoup(r, "lxml")
texts = soup.find_all("font")
i = 0

print(' ')
for i in range(1, 6):
    num = i + 7
    print(texts[i].string)
    while num < i + 8 + 12 * (classNum - 1):
        if len(texts[num].string) > 1:
            print(texts[num].string + ' - ' + texts[num + 5].string)
        num = num + 12
    print(' ')