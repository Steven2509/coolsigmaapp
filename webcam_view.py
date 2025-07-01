import cv2
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)

def update_frame(label):
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (160, 120))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        label.imgtk = imgtk
        label.configure(image=imgtk)

    label.after(15, lambda: update_frame(label))

def release_cam():
    cap.release()
