from logging import shutdown
from tkinter import *
import os
from turtle import color

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown")
st.geometry("500x300")
st.config(bg="black")

r_button = Button(st, text="Restart", font=("Consolas", 10, "bold"), relief=RAISED, bg="white", command=restart)
r_button.place(x=120, y=80, height=40, width=100)

r_button = Button(st, text="Log-Out", font=("Consolas", 10,"bold"), relief=RAISED, bg="white", command=logout)
r_button.place(x=300, y=80, height=40, width=100)

r_button = Button(st, text="Restart Timed", font=("Consolas", 10, "bold"),relief=RAISED, bg="white", command=restart_time)
r_button.place(x=120, y=180, height=40, width=100)

r_button = Button(st, text="ShutDown", font=("Consolas", 10, "bold"), relief=RAISED, bg="white", command=shutdown)
r_button.place(x=300, y=180, height=40, width=100)

st.mainloop()

