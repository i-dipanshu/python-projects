from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6),3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6),3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


st = Tk()
st.title("ShutDown")
st.geometry("500x300")


lab = Label(st,text="Internet Speed test", font=("Consolas", 20, "bold"))
lab.place(x=100, y=20)

lab = Label(st,text="Download speed", font=("Consolas", 15, "bold"))
lab.place(x=120, y=80)

lab_down = Label(st,text="00 Mbps", font=("Consolas", 15, "bold"))
lab_down.place(x=120, y=120)

lab = Label(st,text="Upload speed", font=("Consolas", 15, "bold"))
lab.place(x=120, y=160)

lab_up = Label(st,text="00 Mbps", font=("Consolas", 15, "bold"))
lab_up.place(x=120, y=200)

button = Button(st, text="Check Speed", font=("Time New Roman", 15, "bold"), relief=RAISED, command=speedcheck)
button.place(x=150, y=240, height=30, width=200)

st.mainloop()