from tkinter import *
from tkinter import messagebox
import random
import json
# -----------------------password gneraTOR----------------------
def genrate():
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','&',"$"]

    nr_letter= random.randint(8,10)
    nr_symbol=random.randint(2,3)
    nr_num=random.randint(2,4)
    pass_list=[]

    for char in range(nr_letter):
        pass_list.append(random.choice(alpha))

    for char in range(nr_symbol):
        pass_list+=random.choice(symbols)
    for char in range(nr_num):
        pass_list+=random.choice(num)
    random.shuffle(pass_list)

    password=""
    for char in pass_list:
        password += char

    # print(f"{password}")
    pass_entry.insert(0,password)


# ------------------save password--------------
def save():
   web=web_entry.get()
   email=email_entry.get()
   password=pass_entry.get()
   new_data={web:{
       "email":email,
       "password":password
   }}

#    messagebox.showinfo(title="confirmation ", message="password saved")
   if len(web)==0:
        messagebox.showwarning(title="warning" , message="web field empty")
   if len(password)==0:
       messagebox.showwarning(title="warning" , message="pass field empty")
   else:
        try:
            with open("data.json", "r") as data_file:
                #   json.dump(new_data , data_file , indent=4)
                # read old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data , data_file, indent=4)
            #   update old data
        else:
            data.update(new_data)
            with open("data.json" , "w") as data_file:
        #   write new data
                json.dump(data , data_file, indent=4)
        finally:
                web_entry.delete(0,END)
                pass_entry.delete(0,END)


# ------------------------search the website------------------------
def search():
     web=web_entry.get()
    #  email=email_entry.get()
    #  password=pass_entry.get()
     with open("data.json") as data_file:
         data=json.load(data_file)
         if web in data:
             email=data[web]["email"]
             password=data[web]["password"]
             messagebox.showinfo(title=web , message=password)
        #  print(data)




    #   -----------------------ui setup----------------

      







window=Tk()
window.title("password generator")
window.config(padx=50, pady=50)
canvas=Canvas(height=200 , width=200)
logo=PhotoImage(file="lockss.png")
canvas.create_image(100,100, image=logo)
canvas.grid(row=0 , column=1)
# canvas.pack()

# labels 
web_label = Label(text="website")
web_label.grid(row=1 , column=0)
email_label=Label(text="emai;l/username")
email_label.grid(row=2, column=0)
passwors_label=Label(text="password")
passwors_label.grid(row=3, column=0)

# entries
web_entry=Entry(width=21)
web_entry.grid(row=1, column=1 )
web_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "prernatiwari0507@gmail.com")
pass_entry=Entry(width=21)
pass_entry.grid(row=3, column=1)

# buttons
search_button=Button(text="search" , command=search)
search_button.grid(row= 1, column=2 )
generate_password=Button(text="generate" , command=genrate)
generate_password.grid(row=3, column=2)
add_button=Button(text="Add " , width=36 , command=save)
add_button.grid(row=4 , column=1, columnspan=2)
window.mainloop()