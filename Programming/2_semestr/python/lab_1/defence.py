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
        self.root.geometry('600x300')
        self.root.resizable(False, False)

        # Переменные для хранения данных
        self.input_value = tk.StringVar()
        self.output_value = tk.StringVar()

        # Создание рабочей зоны
        self.__create_calculator()

    def __create_calculator(self):
        """Показать вкладку с калькулятором"""
        calculator_frame = ttk.Frame(self.root)
        calculator_frame.pack(fill='both', pady=(0, 10))

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
        tk.Button(control_frame, text="🗑️ Очистить все",
                  command=lambda: (self.output_value.set("") is None) and (self.input_value.set("") is None),
                  bg="#FF9800", fg="white", padx=10).pack(side='left', padx=2)

        # Числовые кнопки и операции
        buttons_frame = tk.Frame(calculator_frame)
        buttons_frame.pack(fill='both', expand=True, pady=(0, 10))

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
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

    def __append_to_input(self, char):
        """Добавить символ в конец поля ввода"""
        current = self.input_value.get()
        current += char
        self.input_value.set(current)

    def __calculate(self):
        """Калькулирует"""
        try:
            calc = self.input_value.get()

            numbers = []
            operators = []
            current_number = ""

            i = 0
            while i < len(calc):
                char = calc[i]
                if not calc:
                    raise ValueError("Пустое выражение")

                if char.isdigit() or char == '.' or (char == '-' and (i == 0 or calc[i - 1] in '+-*/')):
                    if char == '-':
                        current_number = '-'
                        i += 1
                        while i < len(calc) and (calc[i].isdigit() or calc[i] == '.'):
                            current_number += calc[i]
                            i += 1
                        if current_number == '-':
                            raise ValueError("Некорректное выражение: минус без числа")
                        try:
                            if '.' in current_number:
                                numbers.append(float(current_number))
                            else:
                                numbers.append(int(current_number))
                        except ValueError:
                            raise ValueError(f"Некорректное число: {current_number}")
                        continue
                    else:
                        current_number = ""
                        while i < len(calc) and (calc[i].isdigit() or calc[i] == '.'):
                            current_number += calc[i]
                            i += 1
                        try:
                            if '.' in current_number:
                                numbers.append(float(current_number))
                            else:
                                numbers.append(int(current_number))
                        except ValueError:
                            raise ValueError(f"Некорректное число: {current_number}")
                        continue

                if char in '-+/*':
                    operators.append(char)
                    i += 1
                else:
                    raise ValueError(f"Недопустимый символ: {char}")

            if len(numbers) != len(operators) + 1:
                raise ValueError("Некорректное выражение")

            i = 0
            while i < len(operators):
                if operators[i] in '*/':
                    if operators[i] == '*':
                        result = numbers[i] * numbers[i + 1]
                    else:
                        if numbers[i + 1] == 0:
                            raise ZeroDivisionError("Деление на ноль")
                        result = numbers[i] / numbers[i + 1]

                    numbers[i:i + 2] = [result]
                    operators.pop(i)
                else:
                    i += 1

            result = numbers[0]
            for i in range(len(operators)):
                if operators[i] == '+':
                    result += numbers[i + 1]
                elif operators[i] == '-':
                    result -= numbers[i + 1]

            if result.is_integer():
                result = int(result)

            self.output_value.set(result)
        except Exception as e:
            mbox.showerror('ОШИБКА', str(e))

    def __delete_last_char(self):
        """Удаляет последний символ из поля ввода калькулятор"""
        current = self.input_value.get()
        if len(current) == 0:
            return
        self.input_value.set(current[:-1])


if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()