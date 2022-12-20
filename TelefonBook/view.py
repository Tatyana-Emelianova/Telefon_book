import funk as f

# import tkinter as tk

# def menu():
#     win = tk.Tk()
#     photo = tk.PhotoImage(file="phone.png")
#     win.iconphoto(False, photo)
#     win.title("Phone Book")
#     win.geometry("500x400+40+40")

#     lable_1 = tk.Label(win, text = "Здравствуйте!\nВас приветствует самая лучшая телефонная книга",
#                         fg = "black",
#                         font = ("Arial", 10, "bold")
#                         )
#     lable_1.pack()

#     btn1 = tk.Button(win, text="Добавить контакт", 
#                     command=print_adding_contact,
#                     activebackground="violet",
#                     width = 32,
#                     height = 2
#                     )

#     btn2 = tk.Button(win, text="Удалить контакт", 
#                     command=f.del_contact,
#                     activebackground="violet",
#                     width = 32,
#                     height = 2
#                     )

#     btn3 = tk.Button(win, text="Поиск заветного контакта", 
#                     command=print_search,
#                     activebackground="violet",
#                     width = 32,
#                     height = 2
#                     )

#     btn4 = tk.Button(win, text="Импорт телефонной книги из txt файла", 
#                     command=f.import_book,
#                     activebackground="violet",
#                     width = 32,
#                     height = 2
#                     )

#     btn5 = tk.Button(win, text="Импорт телефонной книги из csv файла", 
#                     command=f.import_book_csv,
#                     activebackground="violet",
#                     width = 32,
#                     height = 2
#                     )

#     btn0 = tk.Button(win, text="До свидания, книга",
#                     command=print_exit,
#                     # command=root.destroy,
#                     activebackground="violet",
#                     width = 32,
#                     height = 2
#                     )

#     getbtn = tk.Button(win, text="get",
#                     command=get_entery)
    

#     btn1.pack()
#     btn2.pack()
#     btn3.pack()
#     btn4.pack()
#     btn5.pack()
#     btn0.pack()
#     tk.Entry().pack(padx=8, pady= 8)
#     getbtn.pack()

#     win.mainloop()
   
    
# def get_entery():
#     value = name.get
#     print(value)    


# def menu():
#     print('Здравствуйте!\nВас приветствует самая лучшая телефонная книга')
#     list_ = ["1", "2", "3", "4", "0"]
#     variant = input('Вы можете: \nДобавить контакт - нажмите 1;\
#          \nУдалить контакт - нажмите 2;\
#           \nПоиск заветного контакта - нажмите 3;\
#            \nИмпорт телефонной книги из txt файла - нажмите 4;\
            #\nИмпорт телефонной книги из csv файла - нажмите 5;\  
#            \nВыйти из книги - 0;\
#             \nВведите пункт меню - ')
#     while variant not in list_:
#         variant = input("Ведите правильное число: ")
#     return variant


def print_adding_contact():
    surname = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    f.add_contact(surname, first_name, patronymic, phone_number)
    print("Контакт сохранен")


def print_search():
    a = input("Введите данные для поиска: ")
    word = a + "\n"
    data_list = f.export_data()
    item = f.search_data(word, data_list)[0]
    if item != []:
        if len(item)>2:
            for i in range(len(item)):
                if i % 2 == 0:
                    print(item[i])
                    print()

        # print("Фамилия".center(20), "Имя".center(20),
        #       "Телефон".center(15), "Примечание".center(30))
        #       for i in item:
        #         print(i.center(20))

        # print(('\n'.join(map(str, item))))
        # item.pop() #удаляет последний элемент
        else:
            print()
            print(item[0]) # * - печатает в столбик и без квадратных скобок
    else:
        print("Данные не обнаружены")


def print_import_book(name_file):
    print(f"Контакты из файла {name_file} добавлены!")


def print_exit():
    print("До новых встреч!")


def print_del_cont():
    word = input("Введите данные для удаления контакта: ")
    data_list = f.export_data()
    del_ = f.search_data(word, data_list)[0]
    if del_ != []:
        if len(del_) == 2:
            return del_[1]
        else:
            print(
                "Найдено несколько контактов.")
            print(del_)
            index_del = int(
                input("Выберите номер удаляемого контакта, в соответсвии с пледложенными: "))
            while index_del not in f.search_data(word, data_list)[1]:
                index_del = int(input("Ведите правильное число: "))
            return index_del
    else:
        return print("Контакт не найден")


def print_del():
    print(f"Контакт удален")
