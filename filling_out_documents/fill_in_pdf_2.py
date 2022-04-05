from util.cell_writer import CellWritter
from PIL import Image, ImageDraw
from util.SETTING import *
import glob

'''img1 = Image.open('pattern/uvedomlenie_ubitie/1.png')
img2 = Image.open('pattern/uvedomlenie_ubitie/2.png')
dir = 'pattern/uvedomlenie_ubitie'
writer_1 = CellWritter('1.png', dir)
print(len(writer_1.cells))
'''

def make_document_2_pdf(data: dict):
    img_name_1 = '../pattern/uvedomlenie_ubitie/1.png'
    img_name_2 = '../pattern/uvedomlenie_ubitie/2.png'

    page1 = CellWritter(img_name_1)
    page2 = CellWritter(img_name_2)

    page1.write_text('Ну вот, кажется, и всё получилось!',0, 40)
    page2.write_text('И на второй странице тоже!',0, 40)

    im_1 = page1.img.convert('RGB')
    im_2 = page2.img.convert('RGB')

    image_list = [im_2]
    pdf_files = glob.glob('../back/static/output/*.pdf')
    file_number = len(pdf_files)
    im_1.save(fr'../back/static/output/uvedomlenie_ubitie_result_{file_number}.pdf', save_all=True, append_images=image_list)

if __name__ == '__main__':
    make_document_2_pdf({})
