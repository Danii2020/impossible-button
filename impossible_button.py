from tkinter import *
import random

main_window = Tk()
main_window.title("My love")

main_window.geometry("400x400")
main_window.resizable(0,0)
main_window.configure(bg='pink')

def move_button(e):
   button_no.place(x=random.randint(0, 400), y=random.randint(0, 400))
def love_window():
    love_window = Toplevel()
    love_window.title("Love window")
    love_window.geometry("500x100")
    love_window.resizable(0,0)
    love_window.configure(bg='pink')
    main_window.eval(f'tk::PlaceWindow {str(love_window)} center')
    love_lable = Label(love_window, text="¡SABÍA QUE DIRIAS QUE SÍ! 😍", fg="white", bg="pink", font=("Sans", 20, "bold"))
    love_lable.pack(pady=2)

title_label = Label(main_window, text="¿Quiéres ser mi novia 🥰?", fg="white", bg='pink', font=("Sans", 20, "bold"))
title_label.pack(pady=5)

button_yes = Button(main_window, text="Si 😍", font=("Arial", 10, "bold"), bg="#FFEFBA", fg="black", height=1, width=8, command=love_window)
button_yes.place(x=120, y=50)

button_no = Button(main_window, text="No 😑", font=("Arial", 10, "bold"), bg="#FFEFBA", fg="black", height=1, width=8)
button_no.place(x=200, y=50)

button_no.bind("<Enter>", move_button)

main_window.mainloop()
