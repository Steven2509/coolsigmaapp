# emotion_detector.py

import cv2
import torch
import torch.nn as nn
from torchvision import transforms

# === Model kiến trúc ===
class EmotionCNN(nn.Module):
    def __init__(self):
        super(EmotionCNN, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.fc = nn.Sequential(
            nn.Linear(64 * 12 * 12, 128),
            nn.ReLU(),
            nn.Linear(128, 3)
        )

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

# === Load model đã lưu ===
model = EmotionCNN()
model.load_state_dict(torch.load("emotion_model.pt", map_location="cpu"))
model.eval()

classes = ["happy", "neutral", "sad"]
emojis = {"happy": "😃", "neutral": "😐", "sad": "😢"}

# === Tiền xử lý ảnh ===
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((48, 48)),
    transforms.Grayscale(),
    transforms.ToTensor()
])

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# === Hàm xử lý chính ===
def detect_emotion_from_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return "😐 No face detected"

    x, y, w, h = faces[0]
    face_img = gray[y:y+h, x:x+w]
    face_tensor = transform(face_img).unsqueeze(0)

    with torch.no_grad():
        output = model(face_tensor)
        pred = torch.argmax(output, dim=1).item()
        emotion = classes[pred]

    return f"You're feeling: {emojis[emotion]} {emotion}"
