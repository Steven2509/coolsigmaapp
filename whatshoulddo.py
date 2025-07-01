import tkinter as tk
from tkinter import *
import os
import random

def todo_popup_happy(root):
    popup = tk.Toplevel(root)
    popup.title("Thông tin chi tiết")
    popup.geometry("400x300")
    popup.resizable(False, False)

    # === Frame chứa Text + Scroll ===
    text_frame = tk.Frame(popup)
    text_frame.pack(fill=BOTH, expand=True)

    scrollbar = Scrollbar(text_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_widget = Text(text_frame, wrap=WORD, yscrollcommand=scrollbar.set)
    text_widget.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=text_widget.yview)

    # === Đọc file ngẫu nhiên trong thư mục ===
    folder_path = "notes/happy"
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    if not txt_files:
        content = "⚠ Không tìm thấy file .txt nào trong thư mục."
    else:
        random_file = random.choice(txt_files)
        with open(os.path.join(folder_path, random_file), "r", encoding="utf-8") as f:
            content = f.read()

    # === Hiển thị nội dung ===
    text_widget.insert(END, content)
    text_widget.config(state=DISABLED)

def todo_popup_neutral(root):
    popup = tk.Toplevel(root)
    popup.title("Thông tin chi tiết")
    popup.geometry("400x300")
    popup.resizable(False, False)

    # === Frame chứa Text + Scroll ===
    text_frame = tk.Frame(popup)
    text_frame.pack(fill=BOTH, expand=True)

    scrollbar = Scrollbar(text_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_widget = Text(text_frame, wrap=WORD, yscrollcommand=scrollbar.set)
    text_widget.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=text_widget.yview)

    # === Đọc file ngẫu nhiên trong thư mục ===
    folder_path = "notes/neutral"
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    if not txt_files:
        content = "⚠ Không tìm thấy file .txt nào trong thư mục."
    else:
        random_file = random.choice(txt_files)
        with open(os.path.join(folder_path, random_file), "r", encoding="utf-8") as f:
            content = f.read()

    # === Hiển thị nội dung ===
    text_widget.insert(END, content)
    text_widget.config(state=DISABLED)

def todo_popup_sad(root):
    popup = tk.Toplevel(root)
    popup.title("Thông tin chi tiết")
    popup.geometry("400x300")
    popup.resizable(False, False)

    # === Frame chứa Text + Scroll ===
    text_frame = tk.Frame(popup)
    text_frame.pack(fill=BOTH, expand=True)

    scrollbar = Scrollbar(text_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_widget = Text(text_frame, wrap=WORD, yscrollcommand=scrollbar.set)
    text_widget.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=text_widget.yview)

    # === Đọc file ngẫu nhiên trong thư mục ===
    folder_path = "notes/sad"
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    if not txt_files:
        content = "⚠ Không tìm thấy file .txt nào trong thư mục."
    else:
        random_file = random.choice(txt_files)
        with open(os.path.join(folder_path, random_file), "r", encoding="utf-8") as f:
            content = f.read()

    # === Hiển thị nội dung ===
    text_widget.insert(END, content)
    text_widget.config(state=DISABLED)
