
import wikipedia

# キーワードを設定
keyword = "マキノン"
# キーワードで検索
wikipedia.set_lang("ja")
result = wikipedia.search(keyword)
print("検索結果",result)

print("最初の検索結果を表示")
page_data = wikipedia.page(result[0])
print(page_data.content)


import japanize_kivy
import urllib.parse
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import webbrowser
kivy.require('1.11.1')
class LinkOpenerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.links = []
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input_text1 = TextInput(
            hint_text='出発駅 ')
        self.input_text2= TextInput(
            hint_text='到着駅')
        self.add_button = Button(text='create')
        self.add_button.bind(on_press=self.add_link)
        self.layout.add_widget(self.input_text1)
        self.layout.add_widget(self.input_text2)
        self.layout.add_widget(self.add_button)
        
        return self.layout
    def add_link(self, instance):
 
            # エンコードされたキーワードとアカウント名を使用してURLを生成
            search_url =f'https://transit.yahoo.co.jp/search/result?from={self.input_text1}&to={self.input_text2}&fromgid=&togid=&flatlon=%2C%2C23408&tlatlon=%2C%2C23404&via=&viacode=&y=2023&m=11&d=06&hh=22&m1=2&m2=9&type=1&ticket=ic&expkind=1&userpass=1&ws=3&s=0&al=1&shin=1&ex=1&hb=1&lb=1&sr=0'
            webbrowser.open(search_url)
if __name__ == '__main__':
    LinkOpenerApp().run()
    
'''
現在時刻から直近の乗換案内を検索して、到着時間を表示する
Yahoo乗換から到着時間をスクレイピングで抽出している
'''
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse # URLエンコード、デコード

startsta = '東京' # 出発駅
endsta = '横浜' # 到着駅

startstaen = urllib.parse.quote(startsta) # encode
endstaen = urllib.parse.quote(endsta) # encode

url0 = 'https://transit.yahoo.co.jp/search/result?from='
url1 = '&flatlon=&to='
url2 = '&viacode=&viacode=&viacode=&shin=&ex=&hb=&al=&lb=&sr=&type=1&ws=3&s=&ei=&fl=1&tl=3&expkind=1&ticket=ic&mtf=1&userpass=0&detour_id=&fromgid=&togid=&kw='

url = url0 + startstaen + url1 + endstaen + url2 + endstaen
# print(url)

req = urllib.request.urlopen(url)
html = req.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

time = soup.select("li.time") # 到着時間の記載部分を抽出
# print(time)
# print(time[2])

print('===到着時間抽出===')
arrive = time[2].select_one('span.mark').text.strip() # <span class="mark">で囲まれたテキストを抽出
print(arrive)
