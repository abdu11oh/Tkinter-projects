from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube video")
root.config(bg='#00D3FD')

Label(root,text = 'YouTube video Ornatish', font ='arial 20 bold', bg='#00D3FD',fg='yellow').pack()


link = StringVar()

Label(root, text = 'Shu yerga link kiriting:',font = 'arial 15 bold').place(x= 160 , y =60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = 'Yuklandi:', font = 'arial 15').place(x=180, y=210)


Button(root,text = 'Yuklash:', font ='arial 15 bold',bg = 'pale violet red',padx
       =2, command = Downloader).place(x=180 , y=150)


root.mainloop()








    















