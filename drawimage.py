from PIL import Image, ImageDraw
import math

class DrawImage():

    def __init__(self, width: int, height: int, color = 'white'):
        self.image = Image.new('RGB', (width, height), color)
        self.draw = ImageDraw.Draw(self.image)

    def insert_text(self, x=0, y=0, write_text= 'need attribute write_text to insert text', color = 'white'):
        return self.draw.text((x, y), text=write_text, fill=color)

    def insert_line(self, x1= 0, y1= 0, x2= 0, y2= 0, color= 'black', width= 3):
        return self.draw.line((x1, y1, x2, y2), fill=color, width=width)

    def save_image(self,image_path):
        return self.image.save(image_path)

    # def insert_rotated_text(self, x, y, write_text, angle, color='white'):
    #     """Inserts rotated text into the image."""
    #
    #     # Create a temporary image with transparent background
    #     text_image = Image.new('RGBA', self.draw.textsize(write_text, font=self.draw.getfont()), (0, 0, 0, 0))
    #     text_draw = ImageDraw.Draw(text_image)
    #
    #     # Draw the text onto the temporary image
    #     text_draw.text((0, 0), write_text, font=self.draw.getfont(), fill=color)
    #
    #     # Rotate the temporary image
    #     rotated_text_image = text_image.rotate(angle, expand=True)  # Expand to accommodate rotated text
    #
    #     # Paste the rotated text onto the main image
    #     self.image.paste(rotated_text_image, (x, y), rotated_text_image)  # Use alpha blending