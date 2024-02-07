from cheque_builder import *
import json

# Read config from file
with open('config.json') as f:
    config = json.load(f)

'''
Note:
    enter width=0, height=0, color='white' in each function below to change configuration
'''
def get_cheque_image(date,payee,amount,bearer_chk,stamp_chk,sign_chk,ac_image_chk):
    # main paper setting
    page = main_page(width=config['paper_width'], height=config['paper_height'], color=config['paper_color'])


    # date setting
    if date['enabled']:
        date_text = get_date_text(date=date['text'], width=config['date_text_box_width'], height=config['date_text_box_height'], color=config['date_text_box_color'], font_size= config['date_text_box_font'])
        page.image.paste(date_text.image, (config['cheque_pos_x'] + 800 + config['date_text_box_pos_x'], config['cheque_pos_y'] + 255 + config['date_text_box_pos_y']))

    # account name setting
    if payee['enabled']:
        payee_name_text = payee_text(payee=payee['text'], width=config['payee_name_box_width'], height=config['payee_name_box_height'], color=config['payee_name_box_color'], font_size=config['payee_name_box_font'])
        page.image.paste(payee_name_text.get_image(), (config['cheque_pos_x'] + 335 + config['amount_figur_box_pos_x'], config['cheque_pos_y'] + 280 + config['payee_name_box_pos_y']))

    # cash amount in numerics setting
    if amount['enabled']:
        amount_figur = amount_figur_text(amount=amount['text'], width=config['amount_figur_box_width'], height=config['amount_figur_box_height'], color=config['amount_figur_box_color'], font_size=config['amount_figur_box_font'])
        page.image.paste(amount_figur.get_image(), (config['cheque_pos_x'] + 800 + config['amount_figur_box_pos_x'], config['cheque_pos_y'] + 300 + config['amount_figur_box_pos_y']))
        # cash amount in words setting
        amount_word = amount_word_text('ONE HUNDRED TWENTY FIVE THOUSAND TWO HUNDRED TWENTY ONE ONLY'
                                       , width=config['amount_word_box_width'], height=config['amount_word_box_height'], color=config['amount_word_box_color'], font_size=config['amount_word_box_font'])
        page.image.paste(amount_word.get_image(), (config['cheque_pos_x'] + 335 + config['amount_word_box_pos_x'], config['cheque_pos_y'] + 300 + config['amount_word_box_pos_y']))

    if stamp_chk['enabled']:
    # stamp setting
        stamp = get_image_with_resolution('stamp.png', (config['stamp_width'], config['stamp_height']))
        page.image.paste(stamp, (config['cheque_pos_x'] + 800 + config['stamp_box_pos_x'], config['cheque_pos_y'] + 320 + config['stamp_box_pos_y']), mask=stamp)

    if bearer_chk['enabled']:
    # bearer text setting
        bearer_text = bearer(bearer='x' * 6, width=config['bearer_width'], height=config['bearer_height'], color=config['bearer_color'], font_size=config['bearer_font'])
        page.image.paste(bearer_text.get_image(), (config['cheque_pos_x'] + mm_to_pixels(194) + config['bearer_pos_x'], config['cheque_pos_y'] + 287 + config['bearer_pos_y']))

    if sign_chk['enabled']:
    # signature setting
        sign = get_signature()
        page.image.paste(sign, (config['cheque_pos_x'] + 780 + config['sign_box_pos_x'], config['cheque_pos_y'] + 360 + config['sign_box_pos_y']), mask=sign)

    if ac_image_chk['enabled']:
    # horizontal line setting
        ac_text_image = get_horizontal_image('A/C PAYEE ONLY', 25)
        page.image.paste(ac_text_image, (config['cheque_pos_x'] + 340 + config['ac_text_image_box_pos_x'], config['cheque_pos_y'] + 200 + config['ac_text_image_box_pos_y']), mask=ac_text_image)
        return page
    else:
        ac_text_image = get_horizontal_image('', 25)
        page.image.paste(ac_text_image, (config['cheque_pos_x'] + 340 + config['ac_text_image_box_pos_x'],
                                         config['cheque_pos_y'] + 200 + config['ac_text_image_box_pos_y']),
                         mask=ac_text_image)
        return page