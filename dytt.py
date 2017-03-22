#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
from urllib.request import urlopen

dytt = "http://www.dytt8.net"

index = dytt + "/html/gndy/dyzz/index.html"

total = 154

# http://www.dytt8.net/html/gndy/dyzz/list_23_1.html
list_item = "http://www.dytt8.net/html/gndy/dyzz/list_23_"
list_23_x = [list_item+str(i+1)+".html" for i in range(total)]
ulink_list = []

def get_ulink_list():
  global ulink_list
  for list_i in list_23_x:
    page = urlopen(list_i)
    bso = BeautifulSoup(page, "html.parser")
    ulink_list_a = bso.find("div", {"class":"co_content8"}).findAll("a", {"class":"ulink"})
    ulink_list += [a.attrs["href"] for a in ulink_list_a]

#get_ulink_list()

def save_csv():
  with open("dytt_url.csv", "w") as f:
    for l in ulink_list:
        f.write(l+"\n")

def get_from_csv():
    global ulink_list
    with open('dytt_url.csv', 'r') as f:
        ulink_list += [line.strip() for line in f.readlines()]

moves = []

def get_url():
    global moves
    global ulink_list
    for ulink in ulink_list:
        movepage = urlopen(dytt+ulink)
        moveosoup = BeautifulSoup(movepage)
        movea = moveosoup.findAll("a", {"href":"#"})
        for a in movea:
            moves += dict(title=moveosoup.title, ftpurl=a.get_text())

def save_move():
    global moves
    with open("dytt_move.txt", "w") as f:
        for move in moves:
            f.write(str(move)+"\n")

get_from_csv()
get_url()
save_move()

#print(ulink_list)
