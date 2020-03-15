
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:37:01 2019

@author: bhavanisathish
"""

from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import themed_tk as tk
import apiai, codecs, json
from gtts import gTTS
import os
from Tkinter import *

window =tk.ThemedTk()
window.get_themes()
window.set_theme("plastik")
window.title("Medical Chatbot")
#window.wm_iconbitmap(bitmap = "images/456icon.ico")
#iconbitmap("images/456icon.ico")
def click():    
    os.system("hello.mp3")
messages =Text(window,width=100,height=40)

messages.pack(side=RIGHT,padx=0,pady=0)

input_user = StringVar()
#img1 = Image.open('images/123.png')
img1 =ImageTk.PhotoImage(file='images/123.png')
#img1 = PhotoImage(file="D:\python files\chatbot\images\123.png  width=500,height=510")
lab=Label(window,image=img1,width=500,height=510)
lab.pack()
but=ttk.Button(window,text="here me",command=click)
but.pack(side=BOTTOM,padx=10,pady=10)
input_field =ttk.Entry(window, text=input_user,width=70)
input_field.pack(side=BOTTOM,padx=10,pady=10)
la=ttk.Label(window,text="Type your text here")
la.pack(side=BOTTOM,padx=7,pady=5)



def Enter_pressed(event):
    
    CLIENT_ACCESS_TOKEN = "dd819e67932e42209bbe54055738f1c2"
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'de' #Default : English
    request.session_id = "<SESSION ID, UNIQUE ssFOR EACH USER>"
        
    input_get = input_field.get()
    #print(input_get)
    messages.insert(INSERT, 'user : %s\n' % input_get)
    # label = Label(window, text=input_get)
            # Message Text
    msgText = input_get#message_object.text

        # Request query/reply for the msg received 
    request.query = msgText

        # Get the response which is a json object
    response = request.getresponse()
    print(response)
    # Convert json obect to a list
    reader = codecs.getdecoder("zlib_codec")
    obj = json.loads(response.read().decode('utf-8'))
    #print(obj)

    # Get reply from the list
    reply = obj['result']['fulfillment']['speech']
    print(reply)
    messages.insert(INSERT, 'bot : %s\n' % reply)
    tts = gTTS(text=reply, slow=True)
    tts.save("hello.mp3")
    input_user.set('')
    # label.pack()
    #return "break"

    

frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()