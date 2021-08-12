#currency converter using tkinter by Pranshu Aggarwal

import tkinter
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

window = tkinter.Tk()
window.title("Currency Converter")
window.geometry("500x500")
window.resizable(0,0)



heading = tkinter.Label(window, text="Currency Converter", font= ("Arial Bold", 30))
heading.place(x=70,y=30)

initial_text = tkinter.Label(window, text="From", font= ("Arial Bold", 20))
initial_text.place(x=70,y=130)

final_text = tkinter.Label(window, text="To", font= ("Arial Bold", 20))
final_text.place(x=300,y=130)

initial = Combobox(window)
initial['values']=("Rupees", "USD", "EURO","Franc")
initial.current(0)
initial.place(x=70,y=200)

final = Combobox(window)
final['values']=("Rupees", "USD", "EURO")
final.current(0)
final.place(x=300,y=200)

amount = tkinter.Label(window, text="Amount:", font= ("Arial Bold", 10))
amount.place(x=70,y=230)

value = tkinter.Entry(window, width=10)
value.place(x=100, y = 260)

#main code
signs = ["Rs.", "$", "€"]
answer = ""
def clicked():
    global answer
    am = int(value.get())
    if initial.get()==final.get():
        answer = am
    elif initial.get() == "Rupees":
        if final.get()=="USD":
            answer = "$"+str(am/74)
        elif final.get()=="EURO":
            answer = "€"+str(am*0.011)
    elif initial.get() == "USD":
        if final.get()=="Rupees":
            answer = "Rs."+str(am*74)
        elif final.get()=="EURO":
            answer = "€"+str(am*0.85)
    elif initial.get()=="EURO":
        if final.get()=="Rupees":
            answer = "Rs."+str(am*80)
        elif final.get()=="USD":
            answer = "$"+str(am//0.85)

    result = tkinter.Label(window, text=answer, font= ("Arial Bold", 20))
    result.place(x=300,y=250)

#main code ends

bt = tkinter.Button(window, text = "Convert", bg = "yellow", fg="red", command = clicked)
bt.place(x = 200, y = 300)



window.mainloop()
