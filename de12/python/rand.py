import japanize_kivy
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
# 既存のコードの上部に以下のインポート文を追加します
from kivy.uix.label import Label

class TransportationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.result_label = Label(text='', size_hint_y=None, height=44)
        layout.add_widget(self.result_label)
        return layout


kivy.require('1.11.1')

class TransportationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.destination_input = TextInput(hint_text='目的地を入力')
        search_button = Button(text='交通情報を検索', on_press=self.search_transportation)
        self.result_label = Label(text='', size_hint_y=None, height=44)

        layout.add_widget(self.destination_input)
        layout.add_widget(search_button)
        layout.add_widget(self.result_label)
        return layout

    def search_transportation(self, instance):
        destination = self.destination_input.text.strip()
        if destination:
            # ヤフージャパンのAPIキーを設定
            api_key = 'YOUR_YAHOO_JAPAN_API_KEY'

            # APIエンドポイント
            api_url = f'https://map.yahooapis.jp/direction/v1/transit?appid={api_key}&from=&to={destination}&format=json'

            # APIリクエストを送信
            response = requests.get(api_url)

            if response.status_code == 200:
                # レスポンスを処理し、結果を取得
                transportation_info = response.json()

def ant_game():
    print("アリをつぶす？ つぶさない？")
    user_choice = input("「つぶす」または「つぶさない」を入力してください：").strip().lower()

    if user_choice == "つぶす":
        print("小学校入学です！")
    elif user_choice == "つぶさない":
        print("ミジンコです！")
    else:
        print("無効な選択です。正しい選択を入力してください。")

    print("次の質問:")
    print("今日は1人休みが出た 牛乳じゃんけん参加する？しない？")
    user_choice = input("「参加する」または「参加しない」を入力してください：").strip().lower()

    if user_choice == "参加する":
        print("中学校入学！")
    elif user_choice == "参加しない":
        print("引きこもりからのニート")
    else:

     ant_game()
     print("次の質問:")
     print("たくさんある部活動。あなたは入る？入らない？")
    user_choice = input("「入る」または「入らない」を入力してください： ").strip().lower()

    if user_choice == "入る":
        print("高校入学です！")
    elif user_choice == "入らない":
        print("ミジンコです！")
        print("ゲームオーバー！ミジンコになりました。")
        return  # ゲーム終了
    else:
       
    
        print("次の質問:")
    print("新しくなった制服。あなたは着崩す？着崩さない？")
    user_choice = input("「着崩す」または「着崩さない」を入力してください： ").strip().lower()

    if user_choice == "着崩さない":
        print("大学入学！")
    elif user_choice == "着崩す":
        print("ガラの悪い人とつるむようになり、逮捕！")
        print("ゲームオーバー！ニートになりました。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了


        print("次の質問:")
    print("友達から誘われたサークルが飲みサーだった。あなたは入る？入らない？")
    user_choice = input("「入る」または「入らない」を入力してください： ").strip().lower()

    if user_choice == "入らない":
        print("無事に大学4年生!")
    elif user_choice == "入る":
        print("飲酒を原因に問題を起こしてしまい、大学退学! ニート！")
        print("ゲームオーバー！ニートになりました。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了

    print("次の質問:")
    print("卒業後の進路。どうする?")
    user_choice = input("「旅に出る」または「一般企業に就職する」を入力してください： ").strip().lower()

    if user_choice == "旅に出る":
        print("大きな決断をした!")
    elif user_choice == "一般企業に就職する":
        print("就職先を見つけた。なんとか生活していけそうだ。")
        print("ゲーム終了！ブラック企業じゃないといいね！")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了

    print("次の質問:")
    print("旅はどこに出よう?")
    user_choice = input("「国内」または「海外」を入力してください： ").strip().lower()

    if user_choice == "海外":
        print("どこにいこうか？")
    elif user_choice == "国内":
        print("日本を旅する中であなたは地方の大切さに気づき、地方創生を意識するようになった。")
        print("ゲーム終了！あなたは地方でのんびり生活することにした。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了

    print("次の質問:")
    print("旅はどこに出よう?")
    user_choice = input("「アメリカ」または「インド」を入力してください： ").strip().lower()

    if user_choice == "インド":
        print("何をしようか？")
    elif user_choice == "イギリス":
        print("あなたは、イギリスを深い文化を学んだ。")
        print("ゲーム終了！イギリスでの経験を生かし、外資系企業に就職した。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了

    print("次の質問:")
    print("インドで何をしよう?")
    user_choice = input("「木の下で横になる」または「象に乗る」を入力してください： ").strip().lower()

    if user_choice == "木の下で横になる":
        print("ゲーム勝利！あなたは悟りを開き、仏になった！")
        return  # ゲーム終了
    elif user_choice == "象に乗る":
        print("インドを満喫した！")
        print("ゲーム終了！あなたは東南アジアに目を向けるようになった。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        return  # ゲーム終了

if __name__ == "__main__":
    ant_game()