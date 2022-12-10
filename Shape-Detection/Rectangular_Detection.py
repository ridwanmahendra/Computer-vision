# Import library OpenCV
import cv2

# Inisialisasi objek untuk capture video dari kamera
cam = cv2.VideoCapture(0)

while True:
    # Membaca frame video dari kamera
    success, frame = cam.read()

    # Jika frame tidak dapat dibaca, berhenti loop
    if not success:
        break

    # Mengubah frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Melakukan thresholding dengan threshold 200
    ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Mencari kontur dari objek
    contours, hierarcy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterasi tiap kontur untuk mencari objek persegi panjang
    for contour in contours:
        # Mendapatkan bounding box dari kontur
        x, y, w, h = cv2.boundingRect(contour)

        # Memeriksa apakah kontur memiliki dua sisi yang panjangnya sama (persegi panjang)
        if (w > h and w >= 3*h) or (h > w and h >= 3*w):
            # Menampilkan bounding box pada objek persegi panjang
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Menampilkan frame
    cv2.imshow('Frame', frame)

    # Tunggu tombol key ditekan
    key = cv2.waitKey(30)
   
