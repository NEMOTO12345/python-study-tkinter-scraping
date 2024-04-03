#スクレイピングアプリ
# URL、htmlタグを入力し検索URLのサイトのhtmlタグの中身を取得できるアプリ。
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext
import requests
from bs4 import BeautifulSoup

root = tk.Tk()
root.title("WEB解析")
root.minsize(400,300)

def get_value(event):
    url = entry.get()
    tag = combo.get()
    web_kaiseki(url,tag)

def web_kaiseki(url,tag):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text,'html.parser')
        temp = soup.find_all(tag)
        print(temp)
        out_put = ""
        for line in temp:
            out_put += line.get_text() + '\n'
        if out_put == "":
            out_put = "見つかりません"
        text_area.delete('1.0', 'end')
        text_area.insert(tk.END,out_put)
    else:
        text_area.delete('1.0', 'end')
        text_area.insert(tk.END,"解析不可")


#画面上のテキストを設定1
static1 = tk.Label(text="URL")
static1.pack()

entry = tk.Entry(width=40)
entry.pack()

#画面上のテキストを設定2
static2 = tk.Label(text="タグ")
static2.pack()

#セレクトボックス(コンボボックス)を作る
combo = ttk.Combobox(root, state='readonly')
# セレクトボックスの選択値を設定
combo["values"] = ("title","h1","h2")
# デフォルトの値をA(index=0)に設定
combo.current(0)
# コンボボックスの配置
combo.pack()

#ボタンの配置
btn = tk.Button(text="検索")
btn.bind("<1>", get_value)
btn.pack()


#結果表示ボックスの配置
text_area = tkinter.scrolledtext.ScrolledText(width = 50,height = 10)
text_area.pack() 

root.mainloop()

