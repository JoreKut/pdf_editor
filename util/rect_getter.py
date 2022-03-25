from asyncio.windows_events import NULL
import cv2 as cv
from SETTING import *

def get_rects(page_paht):
    
    img = cv.imread(page_paht)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    contours0, f = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    resulting_rects = []

    previouse_rect = NULL
    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник

        if  min(rect[1][0], rect[1][1]) < 20:
            continue
        if previouse_rect is not NULL:
            # сравнивае предыдущий объект
            # изначально из одного квадрата мы получаем два объекта:
            #   внешний контур
            #   внутренний контур
            # толщина равна 0.5 по определению
            if abs(previouse_rect[0][0] - rect[0][0]) < 2 and abs(previouse_rect[0][1] - rect[0][1]) < 2:
                continue

        resulting_rects.append(rect)
        previouse_rect = rect

    return resulting_rects