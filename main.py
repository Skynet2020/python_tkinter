import tkinter as tk


def class_work():
    root = tk.Tk()  # Формирует главное окно.
    root.geometry("600x500")  # Устанавливает размеры окна в пикселях.
    # 4 строки ниже - создание т.н. "рамок", внутри которых будут отображаться
    # компоненты с кнопками, полями ввода и т.д.:
    frame_1 = tk.Frame()
    frame_2 = tk.Frame(width=600, height=300)
    frame_2.pack_propagate(0)
    frame_3 = tk.Frame()

    # 1. greeting - сообщение "Изучаем Tkinter" вверху окна.
    # 2. result_to_display - поле, в котором будут отображаться результаты
    #     расчетов, либо сообщения об ошибках.
    # 3. entry - поле ввода на экране.
    greeting = tk.Label(master=frame_1, text="Изучаем Tkinter")
    result_to_display = tk.Label(master=frame_2, width=30, height=7,
                                 highlightbackground="black", highlightthickness=1, wraplength=100)
    entry = tk.Entry(highlightbackground="blue",
                     highlightthickness=1, master=frame_2,  font="Arial 12")

    # Функция, которая удаляет введенное значение из поля entry.
    # Обслуживает кнопку clear_btn:
    def del_entry():
        value = entry.get()
        if value != '':
            entry.delete(0, tk.END)
            result_to_display.config(text='')
            return True
        else:
            return False

    # Функция, которая осуществляет необходимый подсчет.
    # Вызывает функцию userFunction().
    # Обслуживает кнопку calc_btn:
    def calc():
        containsLetters = False
        result = ''
        value = entry.get()
        for i in value:
            if i.isalpha():
                containsLetters = True

        if value == '':
            result = "Введите значение."
        elif not containsLetters:
            value = int(value)
            result = userFunction(value)
        else:
            result = "Нельзя вводить буквы. Разрешены только цифры."
        result_to_display.config(text=result)

    # Кнопка "Очистить":
    clear_btn = tk.Button(
        master=frame_2,
        text="Очистить",
        width=25,
        height=2,
        bg="maroon",
        fg="white",
        command=del_entry
    )

    # Кнопка "Посчитать":
    calc_btn = tk.Button(
        master=frame_2,
        text="Посчитать",
        width=25,
        height=2,
        bg='#235C23',
        fg="white",
        command=calc
    )

    # Кнопка "Закрыть":
    button = tk.Button(
        master=frame_3,
        text="Закрыть",
        width=25,
        height=1,
        bg="grey",
        fg="white",
        command=root.destroy
    )

    ##################################
    ##################################
    #####  БЛОК ДЛЯ ВАШЕГО КОДА  #####

    # 1. Создать функцию userFunction
    # 2. Функция должна иметь параметр
    # 3. Этот параметр должен быть умножен на 10
    # 4. Полученный результат должен быть возвращен из функции (инструкция return)

    ##################################
    ##################################
    ##################################

    # Следующие 6 строк формируют пакеты с кнопками, полями ввода
    # и полями отображения результата.
    # Метод pack() отличается от метода place() тем, что place() устанавливает
    # координаты, по которым располагаются эти элементы, в то время как pack()
    # просто формирует пакет и располагает его внутри своего блока в координатах
    # "по умолчанию":
    result_to_display.place(relx=0.025, rely=0.1)
    entry.place(relx=.45, rely=0.1)
    clear_btn.place(relx=.45, rely=.20)
    calc_btn.place(relx=.45, rely=.35)
    greeting.pack()
    button.pack()

    # Упаковывает рамки, внутри которых располагаются элементы, указанные выше:
    frame_1.pack()
    frame_2.pack()
    frame_3.pack()

    # Запускает цикл (который завершается вызовом команды root.destroy - см. кнопку button выше по коду),
    # который держит окно программы открытым:
    root.mainloop()


class_work()
