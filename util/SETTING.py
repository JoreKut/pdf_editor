import imp
from PIL import ImageFont
import numpy as np

hsv_min = np.array((0, 0, 0), np.uint8)
hsv_max = np.array((179, 255, 220), np.uint8)

file_font_size = 25
font_fill = (30,30,30)
file_font = ImageFont.truetype("arial.ttf", file_font_size)
