# Import library OpenCV
import cv2

# Inisialisasi objek untuk background subtraction
bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=16, detectShadows=True)

# Buka video
videoCapture = cv2.VideoCapture("/Volumes/DATAMAC/notebook/Computer-vision/Video/video.mp4")

while True:
    # Membaca frame video
    success, frame = videoCapture.read()

    # Jika frame tidak dapat dibaca, berhenti loop
    if not success:
        break

    # Konversi frame ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Melakukan background subtraction dengan menggunakan warna HSV
    fgMask = bgSubtractor.apply(hsv)

    # Menampilkan hasil background subtraction
    cv2.imshow('Foreground Mask', fgMask)

    # Tunggu tombol key ditekan
    key = cv2.waitKey(30)
    if key == ord('q'):
        break

# Tutup video dan window
videoCapture.release()
cv2.destroyAllWindows()
