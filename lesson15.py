from re import L
import tkinter


import tkinter as tk
root=tk.Tk()
root.title('りとりし')
root.geometry('500x500')

Label  = tk.Label(text='の文字は「しりとり」です。次の文字を入力してください など')
Label.place(x=10,y=50)

word='しりとり'
word_e=tk.Entry(root,width=25)#入力欄の設定
word_e.place(x=130,y=50)
word_list = ['しりとり']
Button=tk.Button(root,text='しりとり（ひらがな）')

def GetWord():
    if word_e.get()!='':
        word=str(word_e.get())
        return word
    else:
        Label["text"]="文字が入力されていません"
        raise ValueError("文字が入力されていません")

def check_siritori(word):
    word=GetWord()
    print(word)
    print(word[0])
    
    if word[0]==word_list[-1][-1]:
        for words in word_list:
            if words==word:
                Label["text"]="重複するワードがあります。"
                raise ValueError("重複するワードがあります。")
        word_list.append(word)
    else:
        Label["text"]="しりとりになっていません"
        raise ValueError("しりとりになっていません")
    if word[-1]=="ん":
        Label["text"]="「ん」で終わりました。しりとりを終了"
        raise ValueError("しりとりを終了")

    print(word_list)
    Label["text"]='今の文字は「'+word+'」です。次の文字を入力してください'
    word_e.delete(0,tk.END)


Button.bind("<Button-1>",check_siritori)
Button.place(x=108,y=100)
root.mainloop()
