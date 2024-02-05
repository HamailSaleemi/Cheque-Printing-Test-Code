from PIL import Image, ImageDraw
from PIL import ImageFont

class DrawImage():

    def __init__(self, width: int, height: int, color= 'white',transparent= False):
        self.image =Image.new('RGB', (width, height), (255, 255, 255, 0)) if transparent else Image.new('RGB', (width, height), color)
        self.draw = ImageDraw.Draw(self.image)

    def insert_text(self, x=0, y=0, write_text= 'need attribute write_text to insert text', color = 'white', font_size = 25):
        font = ImageFont.load_default(font_size)
        return self.draw.text((x, y), text=write_text, fill=color, font=font)

    def insert_line(self, x1= 0, y1= 0, x2= 0, y2= 0, color= 'black', width= 3):
        return self.draw.line((x1, y1, x2, y2), fill=color, width=width)

    def save_image(self,image_path):
        return self.image.save(image_path)

    def get_image(self):
        return self.image

    def rotate(self, angle):
        self.image = self.image.rotate(angle, fillcolor=(255, 255, 255, 0))
        return True

    def paste_image(self, image: Image, offset=(0, 0)):
        image = image.convert('RGBA')
        self.image = self.image.convert('RGBA')
        self.image.paste(image, (offset[0], offset[1], image.size[0], image.size[1]), mask=image)
        return True

    def show(self, title='default'):
        self.image.show(title)