from static.util.cell_writer import CellWritter
from static.util import date_parser
import glob


def make_document_2_pdf(data: dict):
    img_name_1 = 'static/pattern/uvedomlenie_ubitie/1.png'
    img_name_2 = 'static/pattern/uvedomlenie_ubitie/2.png'

    page1 = CellWritter(img_name_1)
    page2 = CellWritter(img_name_2)

    last_name = data["name_z[1]"]
    name_patronymic = data["name_z[2]"]
    birth_day = date_parser.parse(data["name_z[3]"])
    leave_date = date_parser.parse(data["name_z[4]"])

    # Place of stay
    region = data["name_z[5]"]
    district = data["name_z[6]"]
    city = data["name_z[7]"]
    street = data["name_z[8]"]
    apart_num = data["name_z[9]"]
    korpus = data["name_z[10]"]
    stroenie = data["name_z[11]"]
    room = data["name_z[12]"]

    # Receive party
    receive_party = data["name_z[31]"]
    r_last_name = data["name_z[13]"]
    r_name_patronymic = data["name_z[14]"]
    type_of_document = data["name_z[15]"]
    series = data["name_z[16]"]
    doc_number = data["name_z[17]"]
    date_of_receipt = date_parser.parse(data["name_z[18]"])

    type_of_validity_period = data["name_z[20]"]
    validity_period = date_parser.parse(data["name_z[19]"])
    phone_number = data["name_z[21]"]
    name_of_organization = data["name_z[22]"]
    inn = data["name_z[23]"]
    address = data["name_z[24]"]

    polnomochie = data["name_z[25]"]
    p_series = data["name_z[26]"]
    p_number = data["name_z[27]"]
    p_receive_date = date_parser.parse(data["name_z[28]"])
    p_end_of_validity_period = date_parser.parse(data["name_z[29]"])
    p_type_of_validity_period = date_parser.parse(data["name_z[30]"])

    page1.write_text(last_name, 0, 29)
    page1.write_text(name_patronymic, 30, 59)
    page1.write_text(birth_day, 60, 67)
    page1.write_text(leave_date, 68, 75)

    page1.write_text(region, 76, 105)
    page1.write_text(district, 106, 140)
    page1.write_text(city, 141, 172)
    page1.write_text(street, 173, 207)
    page1.write_text(apart_num, 208, 214)
    page1.write_text(korpus, 215, 217)
    page1.write_text(stroenie, 218, 224)
    page1.write_text(room, 225, 228)

    page1.write_text(r_last_name, 229, 262)
    page1.write_text(r_name_patronymic, 263, 296)
    page1.write_text(type_of_document, 297, 327)
    page1.write_text(series, 328, 332)
    page1.write_text(doc_number, 333, 341)
    page1.write_text(date_of_receipt, 342, 349)
    page1.write_text(validity_period, 350, 357)
    page1.write_text(phone_number, 368, 377)
    page1.write_text(last_name, 378, 407)
    page1.write_text(name_patronymic, 408, 437)
    page1.write_text(birth_day, 438, 445)
    '''
    /////////////////////////////////////////////////////
    '''
    page2.write_text(name_of_organization, 0, 91)
    page2.write_text(inn, 92, 103)
    page2.write_text(address, 104, 175)
    page2.write_text(polnomochie, 176, 221)
    page2.write_text(p_series, 222, 226)
    page2.write_text(p_number, 227, 235)
    page2.write_text(p_receive_date, 236, 243)
    page2.write_text(p_end_of_validity_period, 244, 251)

    im_1 = page1.img.convert('RGB')
    im_2 = page2.img.convert('RGB')

    image_list = [im_2]
    pdf_files = glob.glob('static/output/*.pdf')
    file_number = len(pdf_files)
    name = rf'uvedomlenie_ubitie_result_{file_number + 1}.pdf'
    im_1.save(rf'static/output/{name}', save_all=True, append_images=image_list)

    return name
