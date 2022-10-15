import tkinter as tk
root=tk.Tk()
root.title('しりとり')
root.geometry('500x180')
Label=tk.Label(text='今の文字は「しりとり」です。次の文字を入力してください')
Label.place(x=100,y=150)

def callback(event):
    user_input=event.keysym
    if user_input=="Return":
        print("enter!")
        check_siritori(Label["text"])
root.bind("<Key>",callback)

def GetWord():
    if word_e.get()!='':
        word=str(word_e.get())
        return word
    else:
        Label["text"]="文字が入力されていません"
        raise ValueError("文字が入力されていません")
def check_siritori(word):
    word=GetWord()
    if word[0]==word_list[-1][-1]:
        for words in word_list:
            if words==word:
                Label["text"]="["+word+"]は重複するワードです"
                word_e.delete(0,tk.END)
                raise ValueError("重複するワードがあります")
        word_list.append(word)
    else:
        Label["text"]="["+word+"]はしりとりになっていません"
        word_e.delete(0,tk.END)
        raise ValueError("しりとりになっていません")
    if word[-1]=="ん":
        Label["text"]="「ん」でおわりました。しりとりを終了"
        raise ValueError("しりとり終了")
    print(word_list)
    Label["text"]='今の文字は「'+word+'」です。次の文字を入力してください'
    word_e.delete(0,tk.END)


word=0
word_e=tk.Entry(root,width=25)
word_e.place(x=130,y=50)
word_list=['しりとり']
Button=tk.Button(root,text='しりとり（ひらがな）')
Button.bind("<Button-1>",check_siritori)
Button.place(x=180,y=100)

root.mainloop()
