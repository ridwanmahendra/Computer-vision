# Import library OpenCV
import cv2

# Inisialisasi objek untuk background subtraction
bgSubtractor = cv2.createBackgroundSubtractorMOG2()

# Buka video
videoCapture = cv2.VideoCapture("/Volumes/DATAMAC/notebook/Computer-vision/Video/video.mp4")

while True:
    # Membaca frame video
    success, frame = videoCapture.read()

    # Jika frame tidak dapat dibaca, berhenti loop
    if not success:
        break

    # Melakukan background subtraction pada frame video
    fgMask = bgSubtractor.apply(frame)

    # Menampilkan hasil background subtraction
    cv2.imshow('Foreground Mask', fgMask)

    # Tunggu tombol key ditekan
    key = cv2.waitKey(30)
    if key == ord('q'):
        break

# Tutup video dan window
videoCapture.release()
cv2.destroyAllWindows()
