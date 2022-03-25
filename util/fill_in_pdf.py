import numpy as np
import cv2 as cv

hsv_min = np.array((0, 0, 0), np.uint8)
hsv_max = np.array((155, 55, 55), np.uint8)


if __name__ == '__main__':
    file_path = "images/uvedomlenie_prib-1.png"  # имя файла, который будем анализировать
    img = cv.imread(file_path)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник

        if  min(rect[1][0], rect[1][1]) < 20:
            continue
        print(rect)
        box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        cv.drawContours(img, [box], 0, (0, 255, 0), 2)  # рисуем прямоугольник

    cv.imshow('contours', img)  # вывод обработанного кадра в окно

    cv.waitKey()
    cv.destroyAllWindows()