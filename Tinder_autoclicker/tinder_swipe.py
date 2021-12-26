import tkinter as tk
from tkinter import ttk

import time
import sys
import json

import webbrowser

import pyautogui as pg


class TinderSwipe(tk.Tk):
    """
    EN/RU
        Autoswipe for Tinder/
        Автосвайп для тиндера
    """
    def __init__(self):
        super().__init__()
        self.title("Tinder clicker swipe")
        self.overrideredirect(True)
        self.resizable(False, False)
        self.attributes("-topmost", True)

        self.lf_set_ui = tk.Frame(self)
        self.lf_set_ui.pack(fill=tk.BOTH)

        self.language_interface = "en"
        self.change_language(self.language_interface)

    def change_language(self, lang):
        """
        Changes the interface language
        Starting language app_en.json/
        Изменяет язык интерфейса
        Стартовый язык интерфеса app_en.json
        """
        with open(f"app_{lang}.json", "r", encoding="utf-8") as f:
            self.language_dict = json.load(f)
        if lang == "en":
            self.language_interface = "ru"
        else:
            self.language_interface = "en"
        self.lf_set_ui.pack_forget()
        self.set_ui()

    def set_ui(self):

        self.lf_set_ui = tk.Frame(self)
        self.lf_set_ui.pack(fill=tk.BOTH)
        language_btn = tk.Button(self.lf_set_ui,
                                 text=self.language_dict["change"],
                                 background="#555",
                                 foreground="#ccc",
                                 padx="15",
                                 pady="6",
                                 font="15",
                                 command=lambda: self.change_language(self.language_interface)
                                 )
        language_btn.pack(fill=tk.X)

        self.open_tinder_btn = tk.Button(self.lf_set_ui,
                                         text=self.language_dict["open"],
                                         background="#555",
                                         foreground="#ccc",
                                         padx="15",
                                         pady="6",
                                         font="15",
                                         command=self.open_tinder
                                         )
        self.open_tinder_btn.pack(fill=tk.X)

        exit_but = tk.Button(self.lf_set_ui,
                             text=self.language_dict["exit"],
                             background="#555",
                             foreground="#ccc",
                             padx="15",
                             pady="6",
                             font="15",
                             command=self.app_exit
                             )
        exit_but.pack(fill=tk.X)


    def open_tinder(self):
        """
        Open url:https://tinder.com /
        Открытие ссылки в браузере по умолчанию
        """
        webbrowser.get(using='windows-default').\
            open_new_tab('https://tinder.com')
        self.open_tinder_btn.pack_forget()
        """
        Create Frame
        """
        self.lf0 = tk.Frame(self.lf_set_ui)
        self.lf0.pack(fill=tk.BOTH)

        self.next_win_txt = tk.Label(self.lf0,
                                     text=self.language_dict["ready"]
                                     )
        self.next_win_txt.pack(fill=tk.X)

        self.next_win_btn = tk.Button(self.lf0,
                                      text=self.language_dict["next"],
                                      background="#555",
                                      foreground="#ccc",
                                      padx="15",
                                      pady="6",
                                      font="15",
                                      command=self.next_func   # Запуск следующего фрейма
                                      )
        self.next_win_btn.pack(fill=tk.X)

    def next_func(self):
        """
        Удаление старого фрейма
        """
        self.lf0.pack_forget()
        """
        Создание фрейма для ввода числа лайков
        """
        self.input_iter()
        """
        Создание кнопок старта и выхода
        """
        self.start_but = tk.Button(self.lf_set_ui,
                                   text=self.language_dict["start"],
                                   background="#555",
                                   foreground="#ccc",
                                   padx="15",
                                   pady="6",
                                   font="15",
                                   command=lambda: self.start_func()
                                   )
        self.start_but.pack(fill=tk.X)

    def input_iter(self):
        lf1 = tk.LabelFrame(self.lf_set_ui, text=self.language_dict["n_swipes"])
        lf1.pack(fill=tk.BOTH)
        self.ent_iter = ttk.Entry(lf1, width=10)
        self.ent_iter.pack(fill=tk.X)
        self.ent_iter.insert(tk.END, 1)

    def start_func(self):
        """
        Start swipes/
        Запуск кликов
        """
        pg.hotkey("alt", "tab")     # Развернуть tinder
        time.sleep(0.2)
        for _i in range(int(self.ent_iter.get())):
            pg.press("esc", interval=0.2)  # скип в случае пересечения пар
            pg.press("right", interval=0.3)   # нравится

    def app_exit(self):
        """
        Выход из приложения
        """
        self.destroy()
        sys.exit()


if __name__ == "__main__":
    Win = TinderSwipe()
    Win.mainloop()
