# Import library OpenCV
import cv2
import numpy as np
# Inisialisasi objek untuk capture video dari kamera
cam = cv2.VideoCapture(0)

while True:
    # Membaca frame video dari kamera
    success, frame = cam.read()

    # Jika frame tidak dapat dibaca, berhenti loop
    if not success:
        break

    # Mengubah frame ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Membuat mask untuk mendeteksi warna merah
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2

    # Mencari kontur dari objek
    contours, hierarcy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterasi tiap kontur untuk mencari objek warna merah
    for contour in contours:
        # Mendapatkan bounding box dari kontur
        x, y, w, h = cv2.boundingRect(contour)

        # Menampilkan bounding box pada objek warna merah
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Menampilkan teks "objek terdeteksi" di atas bounding box
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'objek terdeteksi', (x, y-5), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

    # Menampilkan frame
    cv2.imshow('Frame', frame)

    # Tunggu tombol key dite
    key = cv2.waitKey(30)
    if key == 'q':
        break
