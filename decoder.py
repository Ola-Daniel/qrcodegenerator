import cv2

# Qr code decoder

filename = input("Import image to be decoded: ")
image = cv2.imread(filename)
detector = cv2.QRCodeDetector()
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
if vertices_array is not None:
    print(data)
