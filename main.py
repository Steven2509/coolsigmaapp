import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
#from emotion_detector import detect_emotion
from emotion_detector import detect_emotion_from_frame


from settings import get_setting, set_setting
import pygame
import os
import random
from webcam_view import update_frame, release_cam, cap
from whatshoulddo import todo_popup_happy, todo_popup_neutral, todo_popup_sad

# === Cửa sổ chính ===
root = tk.Tk()
root.title("Sigma")
root.iconbitmap("assets\icon.ico")

# Kích thước ngang
WIDTH, HEIGHT = 600, 400
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

username = get_setting("name", "User")
pygame.mixer.init()


def whattodo():
    global result
    if result == "You're feeling: 😃 happy":
        todo_popup_happy(root)
    elif result == "You're feeling: 😐 neutral":
        todo_popup_neutral(root)
    else:
        todo_popup_sad(root)


def playmusic():
    global isplaying, result
    isplaying=True
    if result == "You're feeling: 😃 happy":
        music_dir = "music\happy"  # Thư mục chứa file .mp3
        all_files = os.listdir(music_dir)
        # Lọc ra những file kết thúc bằng .mp3
        mp3_files = [f for f in all_files if f.endswith(".mp3")]
        # Random một file trong danh sách
        random_file = random.choice(mp3_files)
        # Đường dẫn đầy đủ tới file
        random_path = os.path.join(music_dir, random_file)
        pygame.mixer.music.load(random_path)
        pygame.mixer.music.play()
    elif result == "You're feeling: 😐 neutral":
        music_dir = "music/neutral"  # Thư mục chứa file .mp3
        all_files = os.listdir(music_dir)
        # Lọc ra những file kết thúc bằng .mp3
        mp3_files = [f for f in all_files if f.endswith(".mp3")]
        # Random một file trong danh sách
        random_file = random.choice(mp3_files)
        # Đường dẫn đầy đủ tới file
        random_path = os.path.join(music_dir, random_file)
        pygame.mixer.music.load(random_path)
        pygame.mixer.music.play()
    else:
        music_dir = "music\sad"  # Thư mục chứa file .mp3
        all_files = os.listdir(music_dir)
        # Lọc ra những file kết thúc bằng .mp3
        mp3_files = [f for f in all_files if f.endswith(".mp3")]
        # Random một file trong danh sách
        random_file = random.choice(mp3_files)
        # Đường dẫn đầy đủ tới file
        random_path = os.path.join(music_dir, random_file)
        pygame.mixer.music.load(random_path)
        pygame.mixer.music.play()

def togglemusic():
    global isplaying
    if isplaying:
        pygame.mixer.music.pause()
        tatnhac.config(image=play_img)
        isplaying = False
    else:
        pygame.mixer.music.unpause()
        tatnhac.config(image=pause_img)
        isplaying = True


def on_check():
    global result,musicbutton,tatnhac,todo
    pygame.mixer.music.stop()
    if "musicbutton" in globals():
        musicbutton.place_forget()
    if "tatnhac" in globals():
        tatnhac.place_forget()
    if "todo" in globals():
        todo.place_forget()
    ret, frame = cap.read()
    if not ret:
        result_var.set("❌ Cannot read camera")
        return

    result = detect_emotion_from_frame(frame)
    result_var.set(result)
    #nút bật nhạc

    if result != "😐 No face detected":
        musicbutton = tk.Button(root, text=f"Recommended Music For {username}", command=playmusic, font=("Arial", 10),bg="#052e3b", fg="white", activebackground="#007acc", relief="groove")
        musicbutton.place(x=220, y=300, width=250, height=40)
        tatnhac = tk.Button(root, image=pause_img, command=togglemusic)
        tatnhac.place(x=480, y=300, width=40, height=40)
        # === Nút mở popup ===
        todo = tk.Button(root, text="What you should do", command=whattodo, font=("Arial", 14),
            bg="#052e3b", fg="white", activebackground="#007acc", relief="groove")
        todo.place(x=220, y=255, width=250, height=40)

def caidat():
    def save_name():
        name = entry.get().strip()
        if name:
            set_setting("name", name)
            greeting_label.config(text=f"Xin chào {name}")  # ✅ Cập nhật dòng chữ
            musicbutton.config(text=f"Recommended Music For {name}")
            window.destroy()

    window = tk.Toplevel(root)
    window.title("Cài đặt tên")
    window.geometry("300x150")
    window.resizable(False, False)

    tk.Label(window, text="Tên người dùng:", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(window, font=("Arial", 12))
    entry.insert(0, get_setting("name", ""))
    entry.pack(pady=5)

    tk.Button(window, text="Lưu", command=save_name, font=("Arial", 11),
              bg="#00cc66", fg="white").pack(pady=10)


# === Background ảnh ===
bg_image = Image.open("assets/bg.jpg").resize((WIDTH, HEIGHT))
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#webcam
# Label hiển thị webcam
cam_label = tk.Label(root)
cam_label.place(x=30, y=80, width=160, height=120)

# Gọi hàm cập nhật webcam
update_frame(cam_label)

# Đóng camera khi thoát app
def on_close():
    release_cam()
    root.destroy()


play_img = ImageTk.PhotoImage(Image.open("assets/play.png").resize((40, 40)))
pause_img = ImageTk.PhotoImage(Image.open("assets/pause.png").resize((40, 40)))


#dòng chữ chào mừng
greeting_label = tk.Label(root, text=f"Xin chào {username}", font=("Arial", 20),
                          fg="white", bg="#000000")
greeting_label.place(relx=0.5, y=20, anchor="n")


#nút cài đặt
setting_img = Image.open("assets/setting.png").resize((40, 40))  # bạn chỉnh kích thước tùy ý
setting_photo = ImageTk.PhotoImage(setting_img)

setting_btn = tk.Button(root, image=setting_photo, command=caidat,
                        bd=0, bg="black", activebackground="black", highlightthickness=0)
setting_btn.place(x=550, y=10)  # Đặt ở góc phải trên, bạn chỉnh x,y tùy giao diện


# === Nút kiểm tra mặt và kết quả ===
btn = tk.Button(root, text="Check Emotion", command=on_check, font=("Arial", 16),
                bg="#052e3b", fg="white", activebackground="#007acc", relief="groove")
btn.place(x=30, y=220, width=160, height=120)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 16, "bold"),
                        fg="white", bg="#000000", bd=0)
result_label.place(x=220, y=220)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
