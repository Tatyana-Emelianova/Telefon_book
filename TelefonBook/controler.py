import view as v
import funk as f

import tkinter as tk

def menu():
    win = tk.Tk()
    photo = tk.PhotoImage(file="phone.png")
    win.iconphoto(False, photo)
    win.title("Phone Book")
    win.geometry("500x400+40+40")

    lable_1 = tk.Label(win, text = "Здравствуйте!\nВас приветствует самая лучшая телефонная книга",
                        fg = "black",
                        font = ("Arial", 10, "bold")
                        )
    lable_1.pack()

    btn1 = tk.Button(win, text="Добавить контакт", 
                    command=v.print_adding_contact,
                    activebackground="violet",
                    width = 32,
                    height = 2
                    )

    btn2 = tk.Button(win, text="Удалить контакт", 
                    command=f.del_contact,
                    activebackground="violet",
                    width = 32,
                    height = 2
                    )

    btn3 = tk.Button(win, text="Поиск заветного контакта", 
                    command=v.print_search,
                    activebackground="violet",
                    width = 32,
                    height = 2
                    )

    btn4 = tk.Button(win, text="Импорт телефонной книги из txt файла", 
                    command=f.import_book,
                    activebackground="violet",
                    width = 32,
                    height = 2
                    )

    btn5 = tk.Button(win, text="Импорт телефонной книги из csv файла", 
                    command=f.import_book_csv,
                    activebackground="violet",
                    width = 32,
                    height = 2
                    )

    btn0 = tk.Button(win, text="До свидания, книга",
                    command=v.print_exit,
                    # command=root.destroy,
                    activebackground="violet",
                    width = 32,
                    height = 2
                    )

    

    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    btn0.pack()
    name = tk.Entry()
    name.pack(padx=8, pady= 8)
    



    getbtn = tk.Button(win, text="get",
                        command=lambda:get_entery(name))
    getbtn.pack()
        
   
    
    def get_entery(name):
        value = name.get()
        print(value)    

    win.mainloop()

    
# v.lable_1.pack()
# v.btn1.pack()
# v.btn2.pack()
# v.btn3.pack()
# v.btn4.pack()
# v.btn5.pack()
# v.btn0.pack()
# v.tk.Entry().pack(padx=8, pady= 8)
# v.getbtn.pack()
# v.win.mainloop()
# v.menu()


def phonebook():
    menu_item = menu()
    if menu_item == "1":
        v.print_adding_contact()
    elif menu_item == "2":
        f.del_contact()
    elif menu_item == "3":
        v.print_search()
    elif menu_item == "4":
        f.import_book()
    elif menu_item == "0":
        v.print_exit()
