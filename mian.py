from drawimage import DrawImage

def main_page():
    width = int(297.4 / 25.4 * 96)
    height = int(215.9 / 25.4 * 96)
    image = DrawImage(width, height,'white')
    image.insert_text(0, 0, 'white Box', 'black')
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
def date_text():
    width = int(40.64 / 25.4 * 96)
    height = int(7 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    image.insert_text(0, 0, '0  1  0  1  2  0  2  4', 'black', font_size=18)
    return image
def payee_text():
    width = int(105 / 25.4 * 96)
    height = int(6 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    name = '**MULLER & PHIPPS PAKISTAN (PVT) LTD.**'
    name = '    ' + name
    image.insert_text(0, 0, name, 'black', font_size=18)
    return image
def amount_figur_text():
    width = int(35 / 25.4 * 96)
    height = int(7 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    image.insert_text(0, 0, '=100,000.00/-', 'black', font_size=17)
    return image

def amount_word_text():
    width = int(112 / 25.4 * 96)
    height = int(14 / 25.4 * 96)
    image = DrawImage(width, height, 'white')
    figure = 'ONE HUNDRED TWENTY FIVE THOUSAND TWO HUNDRED TWENTY ONE ONLY'
    if len(figure) > 32:
        fifth_space_index = figure.index(' ', figure.index(' ', figure.index(' ', figure.index(' ', figure.index(' ') + 1) + 1) + 1) + 1)
        figure = figure[:fifth_space_index] + '\n' + figure[fifth_space_index:]
    figure = '       ' + figure
    image.insert_text(0, 0, figure, 'black', font_size=16)
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
date_text = date_text()
page.image.paste(date_text.get_image(), (128 + 815 + 0, 66 + 267 + 0))
# page.show('DATE TEXT')


payee_text = payee_text()
page.image.paste(payee_text.get_image(), (128 + 352 + 0, 66 + 318 + 0))
# page.show('PAYEE TEXT')
# page.save_image('01.png')

amount_figur = amount_figur_text()
page.image.paste(amount_figur.get_image(), (128 + 830 + 0, 66 + 330 + 0))
# page.show('AMOUNT FIGURE')

amount_word = amount_word_text()
page.image.paste(amount_word.get_image(), (128 + 352 + 0, 66 + 340 + 0))
page.show()
page.save_image('01.png')