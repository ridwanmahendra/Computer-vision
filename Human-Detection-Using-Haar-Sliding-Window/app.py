

# Import library yang dibutuhkan
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca citra atau video yang akan digunakan sebagai input
image = cv2.imread("/Volumes/DATAMAC/notebook/Computer-vision/Images/im2.jpg")

# Ubah citra menjadi objek numpy array
image_array = np.array(image)

# Tentukan ukuran sliding window
window_size = (64, 64)

# Muat classifier Haar cascade yang akan digunakan untuk deteksi
classifier = cv2.CascadeClassifier("/Volumes/DATAMAC/notebook/Computer-vision/library/haarcascade_frontalface_default.xml")

# Mulai proses deteksi menggunakan sliding window
for y in range(0, image_array.shape[0], window_size[1]):
    for x in range(0, image_array.shape[1], window_size[0]):
        # Ambil sub-citra dengan ukuran sliding window
        sub_image = image_array[y:y+window_size[1], x:x+window_size[0]]

        # Proses deteksi objek manusia pada sub-citra menggunakan Haar cascade
        objects = classifier.detectMultiScale(sub_image)

        # Jika objek manusia terdeteksi, tampilkan bounding box pada sub-citra
        if len(objects) > 0:
            for (x, y, w, h) in objects:
                cv2.rectangle(sub_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Tampilkan hasil deteksi pada layar
plt.imshow(sub_image)