from tkinter import *
root=Tk()
#root.geometry('2000x800')
root.title('Friend')
root.config(bg='#00ffff')
ABC=Frame(root,bg='#ff00ff',bd=20,relief=RIDGE)
ABC.grid()

ABC1=Frame(root,bd=20,)
ABC1.grid()


def bot_reply(msg):
    txt =Text(ABC,bg='#ff0000',fg='#00ff00',height=2,width=40,padx=10,pady=10)
    txt.tag_config("right", justify="right")
    txt.pack()
    a=msg+" <== Bot"
    txt.insert(END,"\n"+a,"right")
    txt.config(state=DISABLED)
    e['text']=''

def sent():

  txt =Text(ABC,bg='#00ff00',fg='#ff0000',height=2,width=40,padx=10,pady=10)

  txt.tag_config("right", justify="right")
  txt.pack()
  v=e.get()
  sent="You => " + v
  txt.insert(END,"\n"+sent)

  if v=='hai':
     root.after(500, bot_reply, 'hello')
  elif v=='hello':
  	root.after(500, bot_reply, 'hai')
  elif v=='how are you':
  	root.after(500, bot_reply, 'fine..')
  elif v=='name':
  	root.after(500, bot_reply, 'PyBot..')
  else:
      root.after(500, bot_reply,'I can\'t reach you..!')


#txt.tag_configure("green", foreground="green")

#txt.grid(column=0,row=0)

e=Entry(ABC1,width=30,bd=2,insertwidth=5,font=("aril",7))
e.grid(row=1,column=0)
b=Button(ABC1,text='sent',command=sent)
b.grid(row=1,column=1)
root.mainloop()
