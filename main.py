import cv2
import numpy as np

# Загрузка изображения
img = cv2.imread('pics/color_text.jpg')

# Создание нового изображения того же размера и типа данных
new_image = np.zeros(img.shape, dtype='uint8')

# Преобразование изображения в формат HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Создание маски для изображения
mask = cv2.inRange(hsv, (0, 0, 0), (255, 255, 255))

# Применение маски к изображению
img = cv2.bitwise_and(img, img, mask)

# Размытие изображения с помощью Гауссовского фильтра
img = cv2.GaussianBlur(img, (5, 5), 0)

# Применение оператора Canny для обнаружения границ
img = cv2.Canny(img, 55, 55)

# Нахождение контуров на изображении
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Рисование контуров на новом изображении
cv2.drawContours(new_image, con, -1, (255, 100, 20), 1)
print(new_image.shape)

# Получение высоты, ширины и каналов нового изображения
ht, wt, chanel = new_image.shape

# Определение трех цветов для замены
color_1 = [255, 100, 20]
color_2 = [20, 100, 255]
color_3 = [100, 20, 255]

# Замена цветов на изображении в соответствии с условиями
for x in range(0, wt):
    for y in range(0, 165):
        yx = new_image[y, x]
        if not all(color_1 == yx):
            continue
        new_image[y, x] = color_2

    for y in range(303, ht):
        yx = new_image[y, x]
        if all(color_1 == yx):
            new_image[y, x] = color_3

# Сохранение результата на диск и отображение его в окне
cv2.imwrite('pics/result.jpg', new_image)
cv2.imshow('result', new_image)
cv2.waitKey(0)
