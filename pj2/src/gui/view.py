import tkinter as tk
from tkinter import ttk

import sv_ttk


class View():
    def __init__(self, app, model):
        self.master = app
        self.model = model
        sv_ttk.set_theme("dark")
        sv_ttk.use_light_theme()

        self.master.geometry("800x600+200+200")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.set_dark_mode()
        self.create_widgets()

    def set_dark_mode(self):
        # テーマを変更する前に、使用可能なテーマを確認する
        print(ttk.Style().theme_names())

        # テーマをダークモードに変更する
        ttk.Style().theme_use('xpnative')  # 例えばclamテーマを使用する

        # テーマを変更する後に、使用可能なテーマを確認する
        print(ttk.Style().theme_names())

    def create_widgets(self):
        self.create_main()

    def create_main(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.grid(row=0, column=0, sticky="nsew", pady=20)
        self.label1 = tk.Label(self.main_frame, text="main_frame")
        self.label1.pack()
        self.right_btn = tk.Button(self.main_frame, text="画面1")
        self.right_btn.pack()
        self.left_btn = tk.Button(self.main_frame, text="画面2")
        self.left_btn.pack()

    def create_right_frame(self):
        self.right_frame = tk.Frame()
        self.right_frame.grid(row=0, column=0, sticky="nsew")
        self.right_label = tk.Label(self.right_frame, text="Right_frmae")
        self.right_label.pack()
