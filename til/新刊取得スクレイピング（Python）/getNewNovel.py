import os
import urllib.request
from bs4 import BeautifulSoup

# アクセスするURL
# 詠みこむファイルはhttp:~のみが記載された物を.pyと同じパスに配置
urlTxt = open(os.path.dirname(os.path.abspath(__file__))+"/url.txt","r")
url = urlTxt.read()
urlTxt.close()

# URLアクセス
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# 新刊情報取得
newNovelInfoList = soup.find_all("div",class_="media-body p-books-media02__contents")

# 新刊情報出力
for newNovelinfo in newNovelInfoList :
    # 新刊タイトル出力
    print(newNovelinfo.find("h2").text)
    # 新刊発売日出力
    count = 0
    for moreDetail in newNovelinfo.find_all("td") :
        if(count == 3) :
            print(moreDetail.text)
        count+=1
    print("-------")
