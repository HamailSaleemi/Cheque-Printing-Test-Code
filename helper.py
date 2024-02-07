from drawimage import DrawImage, ImageDraw
from PIL import Image
def mm_to_pixels(mm):
    return int(mm / 25.4 * 96)
def get_image(width=100, height=100, color='white'):
    '''
        This function return image of width*height with a color
        width: to increase or decrease the width of page.
        height: to increase or decrease the height of page.
        color: to change the color of page recommended and default is 'white'
        :return: return Image
        '''
    return DrawImage(width, height, color)

def get_image_with_text(text = 'i am text timage', width=100, height=100, color='white', font_size=18, text_color= 'black'):
    image = get_image(width,height, color)
    image.insert_text(0, 0, text, color= text_color, font_size=font_size)
    return image