from PIL import ImageDraw, Image
from util.SETTING import *
import util.rect_getter as rect_getter

class CellWritter:
    def __init__(self, img_name: str) -> None:
        self.img_name = img_name
        img_path = f'../pattern/{img_name}'

        self.img = Image.open(img_path)
        self.draw_object = ImageDraw.Draw(self.img)
        self.cells = rect_getter.get_rects(img_path)

    def write_letter(self, cell, character: chr):
        # cell: ( (x0,y0), (w,h), angle )
        x_position = cell[0][0] + 10
        y_position = cell[0][1] - 5

        cell_width = max(cell[1][1], cell[1][0])
        cell_height = min(cell[1][1], cell[1][0])

        coordinates = (x_position - cell_width/2, y_position - cell_height/4)

        self.draw_object.text(coordinates, character, font=file_font, fill=(30,30,30))

    def write_text(self, text: str, start, end):
        # [start ... end]
        zipped = zip(self.cells[start:end+1], text)
        for cell, letter in zipped:
            self.write_letter(cell, letter)

    def write_text_in_cell(self, text:str, cell_index: int):
        self.write_letter(self.cells[cell_index], text)

    def save(self):
        self.img.save(f"../back/static/output/celled-{self.img_name}")

