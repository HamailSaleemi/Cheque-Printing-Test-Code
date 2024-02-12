
from cheque_provider import get_cheque_image

date = {
    'enabled': True,
    'text': '0  1  0  1  2  0  2  4'
}

payee = {
    'enabled': True,
    'text': '**MULLER & PHIPPS PAKISTAN (PVT) LTD.**'
}

amount = {
    'enabled': True,
    'text': '=100,000.00/-'
}
bearer = {
    'enabled': True,
}
stamp = {
    'enabled': True,
}

sign = {
    'enabled': True,
}
ac_image = {
    'enabled': True,
    'text' : ''
}
option = 2  # Assuming the option is 1, 2, 3, or 4
options_map = ['', 'A/C PAYEE ONLY', 'CASH ONLY', 'Clearing only', 'Cash WithDrawal only']
ac_image['text'] = options_map[option]
# if option == 0:
#     ac_image['text'] = ''
# elif option == 1:
#     ac_image['text'] = 'A/C PAYEE ONLY'
# elif option == 2:
#     ac_image['text'] = 'CASH ONLY'
# elif option == 3:
#     ac_image['text'] = 'Clearing only'
# elif option == 4:
#     ac_image['text'] = 'Cash WithDrawal only'

print(ac_image['text'])
get_cheque_image(date, payee,amount,stamp,bearer,sign,ac_image).show('complete cheque')
