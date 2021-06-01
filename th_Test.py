from tkinter import *

window = Tk()
window.geometry("400x500")
window.title("제목")

l1 = Label(window, text="검색")
l1.pack()

l2 = Label(window, text="추가")
l2.pack()

l3 = Label(window, text="삭제")
l3.pack()

b1 = Button(window, text="검색", bg="orange", fg="black", width=5, height=2)
b1.pack()



window.mainloop()
