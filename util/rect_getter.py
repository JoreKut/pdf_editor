import cv2 as cv
from util.SETTING import *

def get_rects(page_path):

    img = cv.imread(page_path)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    desired_rectangles = []

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        x = rect[1][0]
        y = rect[1][1]
        box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат

        '''
            if rect[2] == 90 and 25 < min(x,y) < 45:
        '''
        if rect[2] == 90 and 20 < min(x,y) < 55:
            desired_rectangles.append(rect)
            cv.drawContours(img, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник

    i = cv.resize(img, (0, 0), fx=0.4, fy=0.4)
    cv.imshow('contours', i)  # вывод обработанного кадра в окно
    cv.waitKey()
    cv.destroyAllWindows()
    cv.imwrite('output.jpg', img)

    desired_rectangles.reverse()
    return desired_rectangles

