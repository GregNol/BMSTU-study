"""
Автор: Титов Матвей Алексеевич ИУ7-12Б
Назначение: Калькулятор
"""

import tkinter as tk
from tkinter import messagebox as mbox, ttk
from back import *

class CalculatorApp:
    def __init__(self, root):
        """Инициализация объекта класса"""
        self.root = root

        # Подготовка окна
        self.root.title('Калькулятор')
        self.root.geometry('550x600')
        self.root.resizable(False, False)

        # Переменные для хранения данных
        self.input_value = tk.StringVar()
        self.output_value = tk.StringVar()
        self.base_input_value = tk.StringVar()
        self.base_output_value = tk.StringVar()

        # Создание меню
        self.__create_menu()

        # Создание рабочей зоны
        self.__create_notebook()

    def __create_menu(self):
        """Создает меню"""
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        menu.add_cascade(label='Информация', command=self.__show_info)
        
    def __create_notebook(self):
        """Создает ноутбук с вкладками калькулятор и перевод чисел"""
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both', padx=5, pady=5)

        # Добавляем калькулятор
        frame1 = self.__create_calculator(notebook)
        frame1.pack(fill='both', expand=True)
        notebook.add(frame1, text="Калькулятор", compound='left')

        frame2 = self.__create_transfer(notebook)
        frame2.pack(fill='both', expand=True)
        notebook.add(frame2, text="Перевод чисел", compound='left')

    def __create_calculator(self, nb):
        """Показать вкладку с калькулятором"""
        calculator_frame = ttk.Frame(nb)

        tk.Label(calculator_frame, text="Ввод:").pack(anchor="w")
        input_frame = tk.Frame(
            calculator_frame, relief='sunken', borderwidth=2)
        input_frame.pack(fill='x', pady=(0, 10))

        # Поле ввода
        input_entry = tk.Entry(input_frame, textvariable=self.input_value, justify='right')
        input_entry.pack(fill='both', expand=True, padx=5, pady=5)
        input_entry.focus()

        # Поле вывода
        tk.Label(calculator_frame, text="Результат:").pack(anchor="w")
        output_frame = tk.Frame(calculator_frame, relief='sunken', borderwidth=2)
        output_frame.pack(fill='x', pady=(0, 10))

        output_entry = tk.Entry(output_frame, textvariable=self.output_value, justify='right', state="readonly")
        output_entry.pack(fill='both', expand=True, padx=5, pady=5)

        # Кнопки управления
        control_frame = tk.Frame(calculator_frame)
        control_frame.pack(fill='x', pady=(0, 10))

        tk.Button(control_frame, text="⌫ Удалить последний",
                  command=lambda: self.__delete_last_char(),
                  bg="#FF9800", fg="white", padx=10).pack(side='left', padx=2)
        tk.Button(control_frame, text="🗑️ Очистить ввод",
                  command=lambda: self.input_value.set(""),
                  bg="#FF9800", fg="white", padx=10).pack(side='left', padx=2)
        tk.Button(control_frame, text="🗑️ Очистить результат",
                  command=lambda: self.output_value.set(""),
                  bg="#FF9800", fg="white", padx=10).pack(side='left', padx=2)

        # Числовые кнопки и операции
        buttons_frame = tk.Frame(calculator_frame)
        buttons_frame.pack(fill='both', expand=True, pady=(0, 10))

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['(', ')', '%', '^']
        ]

        for row in buttons:
            row_frame = tk.Frame(buttons_frame)
            row_frame.pack(fill='both', expand=True)
            for btn_text in row:
                if btn_text == '=':
                    tk.Button(row_frame, text=btn_text,
                              command=self.__calculate, bg="#2196F3", fg="white").pack(side='left', fill='both',
                                                                                     expand=True, padx=2, pady=2)
                else:
                    tk.Button(row_frame, text=btn_text,
                              command=lambda x=btn_text: self.__append_to_input(x)).pack(side='left', fill='both',
                                                                                       expand=True, padx=2, pady=2)
        return calculator_frame

    def __create_transfer(self, nb):
        """Показать вкладку для преобразования систем счисления"""

        transfer_frame = ttk.Frame(nb)

        # Поле для входного числа
        tk.Label(transfer_frame, text="Число для перевода:").pack(anchor="w")
        input_frame = tk.Frame(
            transfer_frame, relief='sunken', borderwidth=2)
        input_frame.pack(fill='x', pady=(0, 10))

        base_input_entry = tk.Entry(input_frame, textvariable=self.base_input_value,
                                    font=("Arial", 14), justify='right')
        base_input_entry.pack(fill='both', expand=True, padx=5, pady=5)
        base_input_entry.focus()

        # Поле для выходного числа
        tk.Label(transfer_frame, text="Результат:").pack(anchor="w")
        output_frame = tk.Frame(transfer_frame, relief='sunken', borderwidth=2)
        output_frame.pack(fill='x', pady=(0, 10))

        base_output_entry = tk.Entry(output_frame, textvariable=self.base_output_value,
                                     justify='right', state="readonly")
        base_output_entry.pack(fill='both', expand=True, padx=5, pady=5)

        # Кнопки преобразования
        button_frame = tk.Frame(transfer_frame)
        button_frame.pack(fill='x', pady=(0, 10))

        tk.Button(button_frame, text="10 → 7", command=self.__convert_to_base7,
                  bg="#2196F3", fg="white", padx=20, pady=10).pack(side='left', padx=5)
        tk.Button(button_frame, text="7 → 10", command=self.__convert_from_base7,
                  bg="#2196F3", fg="white", padx=20, pady=10).pack(side='left', padx=5)

        # Кнопки очистки
        control_frame = tk.Frame(transfer_frame)
        control_frame.pack(fill='x', pady=(0, 10))

        tk.Button(control_frame, text="Очистить входное поле",
                  command=lambda: self.base_input_value.set(""),
                  bg="#FF9800", fg="white", padx=10).pack(side='left', padx=2)
        tk.Button(control_frame, text="Очистить результат",
                  command=lambda: self.base_output_value.set(""),
                  bg="#FF9800", fg="white", padx=10).pack(side='left', padx=2)
        tk.Button(control_frame, text="Очистить все",
                  command=lambda: (self.base_input_value.set("") is None) and (self.base_output_value.set("") is None),
                  bg="#FF9800", fg="white", padx=10).pack(side='left', padx=2)
        tk.Button(control_frame, text="Удалить последний",
                  command=self.__delete_last_char_base,
                  bg="#FF9800", fg="white", padx=10).pack(side='left', padx=2)
        buttons_frame = tk.Frame(transfer_frame)
        buttons_frame.pack(fill='both', expand=True, pady=(0, 10))

        buttons = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', '.', '-']
        ]

        for row in buttons:
            row_frame = tk.Frame(buttons_frame)
            row_frame.pack(fill='both', expand=True)
            for btn_text in row:
                tk.Button(row_frame, text=btn_text,
                              command=lambda x=btn_text: self.__append_to_base_input(x)).pack(side='left', fill='both',
                                                                                       expand=True, padx=2, pady=2)
        # Информационное сообщение
        info_frame = tk.LabelFrame(transfer_frame, text="Справка", padx=10, pady=10)
        info_frame.pack(fill='both', expand=True, pady=10)

        info_text = tk.Label(info_frame, text="• Вводите целые или вещественные числа\n"
                                              "• Для целых чисел используется стандартное преобразование\n"
                                              "• Для вещественных чисел преобразуется целая и дробная части\n"
                                              "• Обратное преобразование (7→10) работает для целых и вещественных чисел в 7-й системе",
                             justify='left', font=("Arial", 9))
        info_text.pack(anchor="w")

        return transfer_frame

    def __convert_to_base7(self):
        """Преобразовать число из 10-й системы в 7-ю"""
        try:
            num_str = self.base_input_value.get().strip()
            if not num_str:
                mbox.showwarning("Предупреждение", "Введите число!")
                return

            # Проверяем, есть ли точка (вещественное число)
            if '.' in num_str:
                if num_str.count('.') > 1 or num_str[0] == '.':
                    mbox.showerror('Ошибка', 'Число введено в некорректном формате.')
                parts = num_str.split('.')
                integer_part = parts[0]
                fractional_part = float('0.' + parts[1])

                # Преобразуем целую часть
                integer_base7 = int_to_base7(integer_part)

                # Преобразуем дробную часть
                fractional_base7 = frac_to_base7(fractional_part)

                result = integer_base7 + '.' + fractional_base7
            else:
                number = num_str
                result = int_to_base7(number)

            self.base_output_value.set(result)
        except ValueError:
            mbox.showerror("Ошибка", "Введите корректное число!")
        except Exception as e:
            mbox.showerror("Ошибка", str(e))

    def __convert_from_base7(self):
        """Преобразовать число из 7-й системы в 10-ю"""
        try:
            num_str = self.base_input_value.get().strip()
            if not num_str:
                mbox.showwarning(
                    "Предупреждение", "Введите число в 7-й системе!")
                return

            # Проверяем корректность цифр
            if not all(c in '-0123456.' for c in num_str):
                mbox.showerror(
                    "Ошибка", "Число содержит недопустимые символы!")
                return
            if (num_str.count('-') > 1) or (num_str[0] != '-' and num_str.count('-') == 1):
                mbox.showerror("Ошибка", "Введите корректное число!")
                return
            if '.' in num_str:
                if num_str.count('.') > 1 or num_str[0] == '.':
                    mbox.showerror('Ошибка', 'Число введено в некорректном формате.')
                parts = num_str.split('.')
                integer_part = int_from_base7(parts[0])
                fractional_part = frac_from_base7('0.' + parts[1])
                result = integer_part + '.' + fractional_part
            else:
                result = int_from_base7(num_str)

            self.base_output_value.set(result)
        except ValueError:
            mbox.showerror("Ошибка", "Неверное число в 7-й системе!")
        except Exception as e:
            mbox.showerror("Ошибка", str(e))

    def __append_to_input(self, char):
        """Добавить символ в конец поля ввода"""
        current = self.input_value.get()
        current += char
        self.input_value.set(current)

    def __append_to_base_input(self, char):
        """Добавить символ в конец поля ввода перевода"""
        start = self.base_input_value.get()
        end = start + char
        self.base_input_value.set(end)

    def __calculate(self):
        """Заглушка для калькулятора"""
        self.output_value.set(self.input_value.get())

    def __delete_last_char(self):
        """Удаляет последний символ из поля ввода калькулятор"""
        current = self.input_value.get()
        if len(current) == 0:
            return
        self.input_value.set(current[:-1])

    def __delete_last_char_base(self):
        """Удаляет последний символ из поля ввода перевода чисел"""
        current = self.base_input_value.get()
        if len(current) == 0:
            return
        self.base_input_value.set(current[:-1])

    def __show_info(self):
        """Выводит информацию о приложении"""
        mbox.showinfo(title='Информация', message='Версия калькулятора: 2.1\n\nАвтор: Титов Матвей '
                                                  'Алексеевич\n\nФункционал:\n- Болванка калькулятора\n- Перевод '
                                                  'чисел из 7 в 10 СИ и обратно')

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()