from drawimage import DrawImage, ImageDraw
from PIL import Image, ImageFont

from helper import get_image, get_image_with_text
def mm_to_pixels(mm):
    return int(mm / 25.4 * 96)
def main_page(width=0, height=0, color='white'):
    '''
    This function return the main page to maintain
    the size of page.
    width: to increase or decrease the width of page.
    height: to increase or decrease the height of page.
    color: to change the color of page recommended and default is 'white'
    :return: return main page
    '''
    return get_image(mm_to_pixels(297.4) + width, mm_to_pixels(215.9) + height, color)

def cheque_text_page(width=0, height=0, color='white'):
    '''
    This function return the cheque image to maintain
    the size of cheque.
    width: to increase or decrease the width of page.
    height: to increase or decrease the height of page.
    color: to change the color of page recommended and default is 'white'
    :return: return main page
    '''
    return get_image(mm_to_pixels(171) + width, mm_to_pixels(73.6) + height, color)

def date_text(date= '0  0  0  0  0  0  0  0',width=0, height=0, color='white', font_size= 18):
    '''
    This function return the date image to maintain
    the size of date.
    date: date in the format"D  D  M  M  Y  Y  Y  Y"
    width: to increase or decrease the width of page.
    height: to increase or decrease the height of page.
    color: to change the color of page recommended and default is 'white'
    :return: return main page
    '''
    return get_image_with_text(text=date, width=mm_to_pixels(40.64) + width,
                               height=mm_to_pixels(7) + height, color=color, font_size=font_size)

def payee_text(payee, width=0, height=0, color='white', font_size=18):
    '''
    This function return the payee image to maintain
    the size of payee.
    payee: is the name of the account to be printed on cheque
    width: to increase or decrease the width of page.
    height: to increase or decrease the height of page.
    color: to change the color of page recommended and default is 'white'
    :return: return main page
    '''
    name = '    ' + payee
    return get_image_with_text(text=name, width=mm_to_pixels(105) + width,
                               height=mm_to_pixels(6) + height, color=color, font_size=font_size)


def amount_figur_text(amount='100,000.00/-', width=0, height=0, color='white', font_size=17):
    '''
    This function return the amount image to maintain
    the size of amount.
    amount: is the amount in digits to print on cheque
    width: to increase or decrease the width of page.
    height: to increase or decrease the height of page.
    color: to change the color of page recommended and default is 'white'
    :return: return main page
    '''
    return get_image_with_text(text=amount, width=mm_to_pixels(35) + width,
                               height=mm_to_pixels(7) + height, color=color, font_size=font_size)

def amount_word_text(figure='TWO HUNDRED TWENTY ONE ONLY', width=0, height=0, color='white', font_size=16):
    '''
    This function return the figure image to maintain
    the size of figure.
    figure: is the amount in words to print on cheque
    width: to increase or decrease the width of page.
    height: to increase or decrease the height of page.
    color: to change the color of page recommended and default is 'white'
    :return: return main page
    '''
    if len(figure) > 32:
        fifth_space_index = figure.index(' ', figure.index(' ', figure.index(' ', figure.index(' ', figure.index(' ') + 1) + 1) + 1) + 1)
        figure = figure[:fifth_space_index] + '\n' + figure[fifth_space_index:]
    figure = '       ' + figure
    return get_image_with_text(text=figure, width=mm_to_pixels(112) + width,
                               height=mm_to_pixels(14) + height, color=color, font_size=font_size)

def get_image_with_resolution(image_path, resolution):
    '''
    This function return the cheque image to maintain
    the size of cheque.
    '''
    image = Image.open(image_path)
    width = mm_to_pixels(resolution[0])
    height = mm_to_pixels(resolution[1])
    return image.resize((width, height))
def bearer(bearer='x' * 6, width=0, height=0, color='white', font_size=16):
    '''
    This function return the bearer(xxxxxx) image to maintain
    the size of bearer.
    bearer: is the text to print on bearer
    width: to increase or decrease the width of page.
    height: to increase or decrease the height of page.
    color: to change the color of page recommended and default is 'white'
    :return: return main page
    '''
    return get_image_with_text(text=bearer, width=mm_to_pixels(16) + width,
                               height=mm_to_pixels(6) + height, color=color, font_size=font_size)


def get_horizontal_image(text='', rotate=0, width=0, height=0, font_size=70, size=(0, 0)):
    '''
    This function return the horizontal image with text to maintain
    the size of horizontal image with text.
    text: is the text to print on bearer
    width: to change text direction.
    height: to change text direction.
    font_size: to change text font.
    size: to increase or decrease the size of horizontal line
    :return: return main page
    '''
    image = Image.open('horizontal_line-.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(font_size)
    draw.text((50 + width, 20 + height), text, fill='black', font=font)
    image = image.resize((mm_to_pixels(30) + size[0], mm_to_pixels(10) + size[1]))
    return image.rotate(rotate, expand=True)

def get_signature():
    image = Image.open('sign.png')
    return image.resize((170, 35))
