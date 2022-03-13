# 이미지에는 임계점을 적용 가능ㅎ하다

# cv2.threshold(image,thresh,max_value,type)
#thresh 임계 값 , max_value :임계 값을 넘었을 때 적용할 값
# 기본적으로 사용되는건 THRESH_BINARY


import cv2


image = cv2.imread('images/sky.jpg', cv2.IMREAD_GRAYSCALE)
#grayscale로 읽기 uchangesd,color함수가 따로 있음

images=[]
ret, thres1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    cv2.imshow('image',i)
    cv2.waitKey(0)
    

#각 타입별로 (type) 임계점을 처리하는 방식을 사용해서 출력