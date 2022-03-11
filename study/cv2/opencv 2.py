import cv2

image = cv2.imread('images/cat.jpg')
print(image.shape)
print(image.size)

px=image[100,100]
print(px)

print(px[2])

#이미지 분야에서 관심은 어떤 부분을 인터레스팅 한 부분이라 한다