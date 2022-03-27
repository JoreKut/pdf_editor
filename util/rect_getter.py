import cv2 as cv
from util.SETTING import *

def get_rects(page_path):
    
    img = cv.imread(page_path)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    resulting_rects = []

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        if rect[1][0] < 37 or rect[1][0] > 50:
            continue

        resulting_rects.append(rect)
    
    resulting_rects.reverse()
    
    return resulting_rects
