from PIL import Image
from PIL import ImageDraw
from rect_getter import *
from SETTING import *

def write_letter(image_draw_object : ImageDraw.Draw, rect, character: chr):
    coords = (rect[0][0] - rect[1][0]/4, rect[0][1] - rect[1][1]/2)
    image_draw_object.text(coords, character, font=file_font, fill=(30,30,30))


if __name__ == '__main__':

    # Open an Image
    img_name = 'uvedomlenie_prib-1.png'
    img_path = f'pattern/{img_name}'
    rects = get_rects(img_path)
    print(rects[-1], rects[-2])

    img = Image.open(img_path)

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    
    # Add Text to an image
    last_name = "Ахаха, это работает!!!"
    for i, letter in enumerate(last_name):
        print(i)
        write_letter(I1, rects[-i-1], letter)
    # Save the edited image
    img.save(f"result/reult-{img_name}")
