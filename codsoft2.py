from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string, random

root = Tk()
root.geometry("500x500")
root.title("Roshan Password Generator")
root.config(bg="#000000")
root.resizable(False, False)

def password_generate():
    try:
        length_password = solid.get()
        small_letter = string.ascii_lowercase
        capital_letter = string.ascii_uppercase
        digits = string.digits
        character = string.punctuation
        all_list = []
        all_list.extend(list(small_letter))
        all_list.extend(list(capital_letter))
        all_list.extend(list(digits))
        all_list.extend(list(character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))
    except:
        messagebox.askretrycancel("A Problem Has Been Occured", "Please Try Again")

all_no = {"1" : "1", "2" : "2", "3" : "3", "4" : "4","5" : "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9", "10" : "10", "11" : "11", "12" : "12", "13" : "13", "14" : "14", "15" : "15", "16" : "16", "17" : "17", "18" : "18", "19" : "19", "20" : "20", "21" : "21", "22" : "22", "23" : "23", "24" : "24", "25" : "25", "26" : "26", "27" : "27", "28" : "28", "29" : "29", "30" : "30"}

Title_label = Label(root, text="Roshan Password Generator", bg="#2FF924", fg="black", font=("futura", 15, "bold"))
Title_label.pack(anchor="center", pady="20px")

length_label = Label(root, text="Select the Length of Your Password :- ", bg="#2FF924", font=("ubuntu", 12))
length_label.place(x="20px", y="70px")

def on_enter(e):
    generate_btn['bg'] = "#2FF924"
    generate_btn['fg'] = "white"

def on_leave(e):
    generate_btn['bg'] = "#2FF924"
    generate_btn['fg'] = "black"   

solid = IntVar()
Selector = Combobox(root, textvariable=solid, state="readonly")
Selector['values'] = [l for l in all_no.keys()]
Selector.current(7)
Selector.place(x="240px", y="72px")

generate_btn = Button(root, text="Generate Password", bg="#2FF924", font=("ubuntu", 15), cursor="hand2", command=password_generate)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)
generate_btn.pack(anchor="center", pady="50px")

result_label = Label(root, text="Generated Password Here :- ", bg="#2FF924",  font=("ubuntu", 12))
result_label.place(x="20px", y="160px")

password= StringVar()
pass_final = Entry(root, textvariable= password, state="readonly", bg="#2FF924", font=("ubuntu", 15))
pass_final.place(x="200px", y="160px")

root.mainloop()
