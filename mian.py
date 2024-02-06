from drawimage import DrawImage, ImageDraw
from PIL import Image, ImageFont


def mm_to_pixels(mm):
    return int(mm / 25.4 * 96)
def main_page():
    width = int(297.4 / 25.4 * 96)
    height = int(215.9 / 25.4 * 96)
    image = DrawImage(width, height,'white')
    # image.insert_text(0, 0, 'white Box', 'black')
    return image

def cheque_page():
    width = int(215.9 / 25.4 * 96)
    height = int(73.66 / 25.4 * 96)
    image = DrawImage(width, height, 'yellow')
    return image

def counter_page():
    width = int(45.72 / 25.4 * 96)
    height = int(73.66 / 25.4 * 96)
    image = DrawImage(width, height, 'red')
    return image

def cheque_text_page():
    width = int(171 / 25.4 * 96)
    height = int(73.66 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    return image

def ac_stemp():
    width = int(50.8 / 25.4 * 96)
    height = int(25.4 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    return image

def date_text(date):
    width = int(40.64 / 25.4 * 96)
    height = int(7 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    image.insert_text(0, 0, date, 'black', font_size=18)
    return image



def payee_text(payee):
    width = int(105 / 25.4 * 96)
    height = int(6 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    name = '    ' + payee
    image.insert_text(0, 0, name, 'black', font_size=18)
    return image

def bearer():
    width = int(16 / 25.4 * 96)
    height = int(6 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    image.insert_text(0, 0, 'x' * 6, 'black', font_size=16)
    return image

def amount_figur_text(amount):
    width = int(35 / 25.4 * 96)
    height = int(7 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    image.insert_text(0, 0, amount, 'black', font_size=17)
    return image

def amount_word_text(figure):
    width = int(112 / 25.4 * 96)
    height = int(14 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    if len(figure) > 32:
        fifth_space_index = figure.index(' ', figure.index(' ', figure.index(' ', figure.index(' ', figure.index(' ') + 1) + 1) + 1) + 1)
        figure = figure[:fifth_space_index] + '\n' + figure[fifth_space_index:]
    figure = '       ' + figure
    image.insert_text(0, 0, figure, 'black', font_size=16)
    return image

def get_stamp_image(image_path, resolution):
    image = Image.open(image_path)
    width = mm_to_pixels(resolution[0])
    height = mm_to_pixels(resolution[1])
    return image.resize((width, height))

def get_horizontal_image(text='', rotate=0):
    image = Image.open('horizontal line.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(70)
    draw.text((50, 20), text, fill='black', font=font)
    image = image.rotate(rotate, expand=True)
    return image
# page.show()
# # # Cheque full paper
# cheque = cheque_page()
# page.image.paste(cheque.get_image(), (128 + 177 + 0, 66 + 222 + 0))
# page.show()
# # # Cheque Counter
# counter = counter_page()
# page.image.paste(counter.get_image(), (128 + 177 + 0, 66 + 222 + 0))
# page.show()
# # Cheque Text Area

# Root image
page = main_page()

# cheque text
cheque_text = cheque_text_page()
page.image.paste(cheque_text.get_image(), (128 + 347 + 0, 66 + 222 + 0))
# page.show()

# ac Payee only or cash only
ac_stemp = ac_stemp()
page.image.paste(ac_stemp.get_image(), (128 + 347 + 0, 66 + 222 + 0))
# page.show()

# date only
date_text = date_text(date='0  1  0  1  2  0  2  4')
page.image.paste(date_text.get_image(), (128 + 800 + 0, 66 + 255 + 0))
# page.show('DATE TEXT')


payee_text = payee_text(payee='**MULLER & PHIPPS PAKISTAN (PVT) LTD.**')
page.image.paste(payee_text.get_image(), (128 + 335 + 0, 66 + 280 + 0))
# page.show('PAYEE TEXT')
# page.save_image('stamp.png')


amount_figur = amount_figur_text(amount='=100,000.00/-')
page.image.paste(amount_figur.get_image(), (128 + 800 + 0, 66 + 300 + 0))
# page.show('AMOUNT FIGURE')

amount_word = amount_word_text('ONE HUNDRED TWENTY FIVE THOUSAND TWO HUNDRED TWENTY ONE ONLY')
page.image.paste(amount_word.get_image(), (128 + 335 + 0, 66 + 300 + 0))
# page.show()
page.save_image('02.png')

# stamp settinng
stamp = get_stamp_image('stamp.png',(40,25))
page.image.paste(stamp, (128 + 800 + 0, 66 + 320 + 0), mask=stamp)

# bearer text setting
bearer_text = bearer()
page.image.paste(bearer_text.get_image(), (128 + mm_to_pixels(194) + 0, 66 + 287 + 0))


# testing here
image = Image.open('sign.png')
image = image.resize((170, 35))
page.image.paste(image, (128 + 780 + 0, 66 + 360 + 0), mask=image)
page.show('testing')
page.save_image('testing.png')

ac_image = get_horizontal_image('A/C PAYEE ONLY', 0)
ac_image