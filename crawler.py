import urllib.request as req
import bs4
import re

url = "https://www.amazon.co.jp/hz/wishlist/ls/1RIS8BD1SC94Y?ref_=wl_share=hinas3"

request = req.Request(url, headers={
    "User=Agnet": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")


root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="a-text-center a-fixed-left-grid-col g-itemImage wl-has-overlay g-item-sortable-padding a-col-right")
dates = root.find_all("div", class_="a-fixed-right-grid-col dateAddedText a-col-right")

title_list = []
date_list = []

for title in titles:
    title_list.append(title.a["title"])

for date in dates:
    date_string = list(int(s) for s in re.findall(r'-?\d+\.?\d*', date.span.string))
    date_y = str(date_string[0]).zfill(4)
    date_m = str(date_string[1]).zfill(2)
    date_d = str(date_string[2]).zfill(2)

    date_list.append(int(date_y + date_m + date_d))

data_list = list(zip(title_list, date_list))
#print(data_list)

data_sorted = sorted(data_list, key=lambda x: x[1], reverse= True)
print(data_sorted)
