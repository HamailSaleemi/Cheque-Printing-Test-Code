from cheque_builder import *
import json

# Read config from file
with open('config.json') as f:
    config = json.load(f)

'''
Note:
    enter width=0, height=0, color='white' in each function below to change configuration
'''
def get_cheque_image(date):
    # main paper setting
    page = main_page(width=config['paper_width'], height=config['paper_height'], color=config['paper_color'])


    # date setting
    if date['enabled']:
        date_text = get_date_text(date=date['text'], width=config['date_text_box_width'], height=config['date_text_box_height'], color=config['date_text_box_color'], font_size= config['date_text_box_font'])
        page.image.paste(date_text.image, (config['cheque_pos_x'] + 800 + config['date_text_box_pos_x'], config['cheque_pos_y'] + 255 + config['date_text_box_pos_y']))

    # account name setting
    ac_name_text = payee_text(payee='**MULLER & PHIPPS PAKISTAN (PVT) LTD.**', width=config['ac_name_box_width'], height=config['ac_name_box_height'], color=config['ac_name_box_color'], font_size=config['ac_name_box_font'])
    page.image.paste(ac_name_text.get_image(), (config['cheque_pos_x'] + 335 + 0, config['cheque_pos_y'] + 280 + 0))

    # cash amount in numerics setting
    amount_figur = amount_figur_text(amount='=100,000.00/-', width=config['fig_num_box_width'], height=config['fig_num_box_height'], color=config['fig_num_box_color'], font_size=config['fig_num_box_font'])
    page.image.paste(amount_figur.get_image(), (config['cheque_pos_x'] + 800 + 0, config['cheque_pos_y'] + 300 + 0))

    # cash amount in words setting
    amount_word = amount_word_text('ONE HUNDRED TWENTY FIVE THOUSAND TWO HUNDRED TWENTY ONE ONLY'
                                   , width=config['fig_eng_box_width'], height=config['fig_eng_box_height'], color=config['fig_eng_box_color'], font_size=config['fig_eng_box_font'])
    page.image.paste(amount_word.get_image(), (config['cheque_pos_x'] + 335 + 0, config['cheque_pos_y'] + 300 + 0))

    # stamp setting
    stamp = get_image_with_resolution('stamp.png',(40 + 0, 25 + 0))
    page.image.paste(stamp, (config['cheque_pos_x'] + 800 + 0, config['cheque_pos_y'] + 320 + 0), mask=stamp)

    # bearer text setting
    bearer_text = bearer(bearer='x' * 6, width=config['bearer_width'], height=config['bearer_height'], color=config['bearer_color'], font_size=config['bearer_font'])
    page.image.paste(bearer_text.get_image(), (config['cheque_pos_x'] + mm_to_pixels(194) + 0, config['cheque_pos_y'] + 287 + 0))

    # signature setting
    sign = get_signature()
    page.image.paste(sign, (config['cheque_pos_x'] + 780 + 0, config['cheque_pos_y'] + 360 + 0), mask=sign)

    # horizontal line setting
    ac_text_image = get_horizontal_image('A/C PAYEE ONLY', 25)
    page.image.paste(ac_text_image, (config['cheque_pos_x'] + 340 + 0, config['cheque_pos_y'] + 200 + 0), mask=ac_text_image)
    return page