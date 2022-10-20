import tkinter


import tkinter as tk
root=tk.TK()
root.title('りとりし')
root.geometry('500x500')

Label  = tk.Label(text='の文字は「しりとり」です。次の文字を入力してください など')
Label.place(x=10,y=50)

word=0
word_e=tk.Entry(root,widith=25)
word_e.place(x=130,y=50)
word_list = ['しりとり']

Button=tk.Button(root,text='しりとり（ひらがな）')
Button.bind("<Button-1>",check_siritori)

def check_siritori(word):
    word=GetWord()
    
    if word[0]==word_list[-1][-1]:
        for wordsword in word_list:
            if words==word:
                """"""
                Label["text"]="重複するワードがあります。"
                raise ValueError("重複するワードがあります。")
        word_list.append(word)
root.mainloop()
