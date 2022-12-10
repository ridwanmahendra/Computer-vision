# Import library OpenCV
import cv2

# Inisialisasi objek untuk background subtraction
bgSubtractor = cv2.createBackgroundSubtractorMOG2()

# Buka video
videoCapture = cv2.VideoCapture("/Volumes/DATAMAC/notebook/Computer-vision/Data/Video/video.mp4")

while True:
    # Membaca frame video
    success, frame = videoCapture.read()

    # Jika frame tidak dapat dibaca, berhenti loop
    if not success:
        break

    # Melakukan background subtraction
    fgMask = bgSubtractor.apply(frame)

    # Menampilkan hasil background subtraction dengan resolusi kecil
    frame_small = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    bg_small = cv2.resize(bgSubtractor.getBackgroundImage(), (0,0), fx=0.25, fy=0.25)
    diff_small = cv2.resize(cv2.absdiff(frame, bgSubtractor.getBackgroundImage()), (0,0), fx=0.25, fy=0.25)
    fgMask_small = cv2.resize(fgMask, (0,0), fx=0.25, fy=0.25)
    cv2.imshow('Frame', frame_small)
    cv2.imshow('Background', bg_small)
    cv2.imshow('Difference', diff_small)
    cv2.imshow('Foreground Mask', fgMask_small)

    # Tunggu tombol key ditekan
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
    