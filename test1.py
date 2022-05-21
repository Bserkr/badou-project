import matplotlib.pyplot as plt
import cv2
img = cv2.imread("./image/Lena.bmp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(121)
plt.imshow(img)
print("---image lenna----")
print(img)
plt.subplot(122)
plt.imshow(gray_img)
print("---image gray----")
print(gray_img)

plt.show()




