from cheque_builder import *
import json

# Read config from file
with open('config.json') as f:
    config = json.load(f)

'''
Note:
    enter width=0, height=0, color='white' in each function below to change configuration
'''

# main paper setting
page = main_page(width=config['paper_width'], height=config['paper_height'], color=config['paper_color'])

# creating check on the paper for testing cheque box
# cheque_text = cheque_text_page(width=config['cheque_width'], height=config['cheque_height'], color=config['cheque_color'])
# page.image.paste(cheque_text.get_image(), (128 + 347 + 0, 66 + 222 + 0))

# date setting
date_text = date_text(date='0  1  0  1  2  0  2  4', width=config['date_text_box_width'], height=config['date_text_box_height'], color=config['date_text_box_color'], font_size= config['date_text_box_font'])
page.image.paste(date_text.image, (128 + 800 + 0, 66 + 255 + 0))

# account name setting
ac_name_text = payee_text(payee='**MULLER & PHIPPS PAKISTAN (PVT) LTD.**', width=config['ac_name_box_width'], height=config['ac_name_box_height'], color=config['ac_name_box_color'], font_size=config['ac_name_box_font'])
page.image.paste(ac_name_text.get_image(), (128 + 335 + 0, 66 + 280 + 0))

# cash amount in numerics setting
amount_figur = amount_figur_text(amount='=100,000.00/-', width=config['fig_num_box_width'], height=config['fig_num_box_height'], color=config['fig_num_box_color'], font_size=config['fig_num_box_font'])
page.image.paste(amount_figur.get_image(), (128 + 800 + 0, 66 + 300 + 0))

# cash amount in words setting
amount_word = amount_word_text('ONE HUNDRED TWENTY FIVE THOUSAND TWO HUNDRED TWENTY ONE ONLY'
                               , width=config['fig_eng_box_width'], height=config['fig_eng_box_height'], color=config['fig_eng_box_color'], font_size=config['fig_eng_box_font'])
page.image.paste(amount_word.get_image(), (128 + 335 + 0, 66 + 300 + 0))

# stamp setting
stamp = get_image_with_resolution('stamp.png',(40 + 0, 25 + 0))
page.image.paste(stamp, (128 + 800 + 0, 66 + 320 + 0), mask=stamp)

# bearer text setting
bearer_text = bearer(bearer='x' * 6, width=config['bearer_width'], height=config['bearer_height'], color=config['bearer_color'], font_size=config['bearer_font'])
page.image.paste(bearer_text.get_image(), (128 + mm_to_pixels(194) + 0, 66 + 287 + 0))

# signature setting
sign = get_signature()
page.image.paste(sign, (128 + 780 + 0, 66 + 360 + 0), mask=sign)

# horizontal line setting
ac_text_image = get_horizontal_image('A/C PAYEE ONLY', 25)
page.image.paste(ac_text_image, (128 + 340 + 0, 66 + 200 + 0), mask=ac_text_image)
page.show()