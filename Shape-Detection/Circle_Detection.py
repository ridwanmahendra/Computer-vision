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

    # Melakukan thresholding dengan threshold 90
    ret, thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)

    # Mencari kontur dari objek
    contours, hierarcy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterasi tiap kontur untuk mencari objek bulat
    for contour in contours:
        # Mendapatkan bounding circle dari kontur
        (x, y), radius = cv2.minEnclosingCircle(contour)

        # Memeriksa apakah radius kontur cukup besar
        if radius >= 20:
            # Menampilkan bounding circle pada objek bulat
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (0, 255, 0), 2)

    # Menampilkan frame
    cv2.imshow('Frame', frame)

    # Tunggu tombol key ditekan
    key = cv2.waitKey(30)
    if key == ord('q'):
        break

# Tutup kamera dan window
cam.release()
cv2.destroyAllWindows()
