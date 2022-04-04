import util.date_parser as date_parser
from util.cell_writer import CellWritter
from PIL import Image

def merge_images_into_pdf():

    image_1 = Image.open(r'../back/static/output/celled-1.png')
    image_2 = Image.open(r'../back/static/output/celled-2.png')
    image_3 = Image.open(r'../back/static/output/celled-3.png')
    image_4 = Image.open(r'../back/static/output/celled-4.png')

    im_1 = image_1.convert('RGB')
    im_2 = image_2.convert('RGB')
    im_3 = image_3.convert('RGB')
    im_4 = image_4.convert('RGB')

    image_list = [im_2, im_3, im_4]

    im_1.save(r'../back/static/output/result.pdf', save_all=True, append_images=image_list)


def make_pdf(data: dict):
    
    img_name_1 = '1.png'
    img_name_2 = '2.png'
    img_name_3 = '3.png'
    img_name_4 = '4.png'
    
    page1 = CellWritter(img_name_1)
    page2 = CellWritter(img_name_2)
    page3 = CellWritter(img_name_3)
    page4 = CellWritter(img_name_4)

    ''' PAGE_1  '''

    page1.write_text(data["name_z[1]"], 0, 26)
    page1.write_text(data["name_z[2]"], 27, 53)
    page1.write_text(data["name_z[3]"], 54, 77)
    page1.write_text(data["name_z[4]"], 78, 102)

    # name_z[5] - число
    date = date_parser.parse(data["name_z[5]"])
    page1.write_text(date, 103, 110)

    gender = data["name_z[6]"]
    try:
        page1.write_text_in_cell('V', 110+int(gender))
    except:
        pass
    # Место рождения
    page1.write_text(data["name_z[7]"], 113, 184)
    # Вид документа
    page1.write_text(data["name_z[8]"], 185, 194)
    # Серия
    page1.write_text(data["name_z[9]"], 195, 198)
    # Номер
    page1.write_text(data["name_z[10]"], 199, 209)

    # Дата выдачи
    start_date = date_parser.parse(data["name_z[11]"])
    # Действует до
    end_date = date_parser.parse(data["name_z[12]"])
    page1.write_text(start_date+end_date, 210, 225)

    # Вид документа на пребыванеие в РФ
    doc_type = data["name_z[13]"]
    if doc_type != "4":
        try:
            page1.write_text_in_cell('V', 225 + int(doc_type))
        except:
            pass
    # серия
    page1.write_text(data["name_z[14]"], 229, 232)
    # Номер
    page1.write_text(data["name_z[15]"], 233, 247)

    # Дата выдачи
    start_date = date_parser.parse(data["name_z[16]"])
    # Срок действия до
    end_date = date_parser.parse(data["name_z[17]"])

    page1.write_text(start_date + end_date, 248, 263)

    # Цель визита
    purpose_val = data["name_z[18]"]
    try:
        purpose_cell = 263 + int(purpose_val)
        page1.write_text('V', purpose_cell, purpose_cell)
    except:
        pass
    # Телефон
    phone_number = data["name_z[19]"]
    page1.write_text(phone_number, 273, 282)

    # Профессия
    profession = data["name_z[20]"]
    page1.write_text(profession, 283, 308)

    # Дата въезда
    start_date = date_parser.parse(data["name_z[21]"])
    # Пребывание ДО
    end_date = date_parser.parse(data["name_z[22]"])
    period = start_date+end_date
    page1.write_text(period, 309, 324)

    # Миграционная карта

    # Серия
    page1.write_text(data["name_z[23]"], 325, 328)
    # Номер
    page1.write_text(data["name_z[24]"], 329, 339)
    # Сведения о представителях
    page1.write_text(data["name_z[25]"], 340, 414)

    ''' PAGE_2  '''

    # Адрес пребывания
    page2.write_text(data["name_z[26]"], 0, 101)

    # Место пребывания

    # Область, край, ...
    page2.write_text(data["name_z[27]"], 102, 151)
    # Район
    page2.write_text(data["name_z[28]"], 152, 176)
    # Город
    page2.write_text(data["name_z[29]"], 177, 200)

    # Улица
    page2.write_text(data["name_z[30]"], 201, 225)

    # Дом, участок, владение
    page2.write_text_in_cell(data["name_z[31]"], 226)
    # Номер дома
    page2.write_text(data["name_z[32]"], 227, 234)
    # Корпус дома
    page2.write_text(data["name_z[33]"], 235, 239)
    # Строение дома
    page2.write_text(data["name_z[34]"], 240, 243)

    # Квартира
    page2.write_text_in_cell(data["name_z[35]"], 244)
    # Номер квартиры
    page2.write_text(data["name_z[36]"], 245, 248)

    # Место пребывания
    place_val = data["name_z[37]"]
    try:
        page2.write_text_in_cell("V", 248+int(place_val))
    except:
        pass
    # Место ФАКТИЧЕСКОГО нахождения

    # Область, край, ...
    page2.write_text(data["name_z[39]"], 252, 299)
    # Район
    page2.write_text(data["name_z[40]"], 300, 324)
    # Город
    page2.write_text(data["name_z[41]"], 325, 346)

    # Кадастровый номер
    page2.write_text(data["name_z[42]"], 347, 390)
    # Реквизиты
    page2.write_text(data["name_z[43]"], 391, 453)

    ''' PAGE_3  '''

    # Организация/ физ лицо
    if data["name_z[44]"] == "1":
        page3.write_text_in_cell("V", 0)
    elif data["name_z[44]"] == "2":
        page3.write_text_in_cell("V", 1)

    # Фамилия
    page3.write_text(data["name_z[45]"], 2, 28)
    # Имя
    page3.write_text(data["name_z[46]"], 29, 55)
    # Отчество
    page3.write_text(data["name_z[47]"], 56, 77)

    # Вид документа
    page3.write_text(data["name_z[48]"], 78, 88)
    # Серия
    page3.write_text(data["name_z[49]"], 89, 92)
    # Номер
    page3.write_text(data["name_z[50]"], 93, 103)

    # Дата выдачи
    start_date = data["name_z[51]"]
    # Действует до
    end_date = data["name_z[52]"]
    page3.write_text(start_date+end_date, 104, 119)

    # Область, край, ...
    page3.write_text(data["name_z[53]"], 120, 167)
    # Район
    page3.write_text(data["name_z[54]"], 168, 192)
    # Город
    page3.write_text(data["name_z[55]"], 193, 215)

    # Улица
    page3.write_text(data["name_z[56]"], 216, 240)
    # Номер дома
    page3.write_text(data["name_z[57]"], 241, 244)
    # Корпус дома
    page3.write_text(data["name_z[58]"], 245, 249)
    # Строение дома
    page3.write_text(data["name_z[59]"], 250, 253)
    # Квартира
    page3.write_text(data["name_z[60]"], 254, 257)

    # Фамилия
    page3.write_text(data["name_z[1]"], 258, 284)
    # Имя
    page3.write_text(data["name_z[2]"], 285, 311)
    # Отчество
    page3.write_text(data["name_z[3]"], 312, 333)
    # Гражданство
    page3.write_text(data["name_z[4]"], 334, 359)

    # Дата рождения
    date = date_parser.parse(data["name_z[5]"])
    page3.write_text(date, 360, 367)

    # Пол
    gender = data["name_z[6]"]
    try:
        page3.write_text_in_cell('V', 367 + int(gender))
    except:
        pass
    # Место рождения
    page3.write_text(data["name_z[7]"], 370, 441)
    # Вид документа
    page3.write_text(data["name_z[8]"], 442, 452)
    # Серия
    page3.write_text(data["name_z[9]"], 453, 456)
    # Номер
    page3.write_text(data["name_z[10]"], 457, 487)

    # Дата выдачи
    start_date = date_parser.parse(data["name_z[11]"])
    # Действует до
    end_date = date_parser.parse(data["name_z[12]"])
    page3.write_text(start_date + end_date, 468, 483)

    # Место пребывания

    # Область, край, ...
    page3.write_text(data["name_z[27]"], 484, 531)
    # Район
    page3.write_text(data["name_z[28]"], 532, 556)
    # Город
    page3.write_text(data["name_z[29]"], 557, 580)

    # Улица
    page3.write_text(data["name_z[30]"], 581, 605)
    # Дом, участок, владение
    page3.write_text_in_cell(data["name_z[31]"], 606)
    # Номер дома
    page3.write_text(data["name_z[32]"], 607, 614)
    # Корпус дома
    page3.write_text(data["name_z[33]"], 615, 619)
    # Строение дома
    page3.write_text(data["name_z[34]"], 620, 623)

    # Квартира
    page3.write_text_in_cell(data["name_z[35]"], 624)
    # Номер квартиры
    page3.write_text(data["name_z[36]"], 625, 628)

    end_date = date_parser.parse(data["name_z[22]"])
    page3.write_text(end_date, 629, 636)

    ''' PAGE_4  '''
    # Номер принимающей стороны
    page4.write_text(data["name_z[61]"], 0, 10)
    # Наименование организации
    page4.write_text(data["name_z[62]"], 11, 52)
    # ИНН
    page4.write_text(data["name_z[63]"], 53, 63)
    # Адрес организации
    page4.write_text(data["name_z[64]"], 64, 147)

    # Фамилия
    page4.write_text(data["name_z[45]"], 148, 174)
    # Имя
    page4.write_text(data["name_z[46]"], 175, 201)
    # Отчество
    page4.write_text(data["name_z[47]"], 202, 225)

    # Наименование организации
    page4.write_text(data["name_z[62]"], 226, 267)
    # ИНН
    page4.write_text(data["name_z[63]"], 268, 278)

    page1.save()
    page2.save()
    page3.save()
    page4.save()

    merge_images_into_pdf()