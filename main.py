import tkinter as tk

#メイン処理
root=tk.Tk()
root.title('しりとりゲーム')
root.geometry('700x460')#'500x180'など


#入力欄の設定
word=0#入力欄に入れる文字
word_e=tk.Entry(root,width=25)#入力欄の設定
word_e.place(x=200,y=50)#入力欄の位置
word_list=['しりとり']#リスト、初期ワードの設定


Label = tk.Label(text='しりとり')#'今の文字は「しりとり」です。次の文字を入力してください'など
Label.place(x=200,y=200)#マスの位置

label2 = tk.Label(text='key', relief= 'groove')
label2.place(x=200, y=400)

def callback(event):
    user_input = event.keysym
    # print(user_input)
    # print(type(user_input))
    if user_input == "Return":
        print("enter!")
        check_siritori(Label["text"])


root.bind("<Key>", callback)


#入力したワードを取得
def GetWord():
    #入力が空白になってないかチェック
    if word_e.get()!='':
        word=str(word_e.get())
        return word
    else:
        Label["text"]="文字が入力されていません"
        raise ValueError("文字が入力されていません")

def check_siritori(word):
    word=GetWord() #ワードを取得

    if word[0]==word_list[-1][-1]: #最初の文字としりとりの最後の文字が一致する場合
        for words in word_list:#配列の数分比較
            if words==word:#リスト内のワードと重複する場合
                Label["text"]="重複するワードがあります"
                raise ValueError("重複するワードがあります")#エラー処理
        word_list.append(word) #リストにワードを追加
    else:
        Label["text"]="しりとりになっていません"
        word_e.delete(0, tk.END)
        raise ValueError("しりとりになっていません")

    if word[-1]=="ん":#最後の文字が「ん」になっている場合
        Label["text"]="「ん」でおわりました。しりとりを終了"
        word_e.delete(0, tk.END)
        raise ValueError("しりとり終了")#エラー処理

    print(word_list)#リスト表示
    Label["text"]='今の文字は「'+word+'」です。次の文字を入力してください'
    word_e.delete(0, tk.END) ## word_eを、0文字目から最後の文字まで削除


#ボタンの作成
Button=tk.Button(root,text='しりとり（ひらがな）')
Button.bind("<Button-1>",check_siritori)
Button.place(x=200,y=100)

root.mainloop()
