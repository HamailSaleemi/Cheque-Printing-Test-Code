
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
    'enabled': False,
}
get_cheque_image(date, payee,amount,stamp,bearer,sign,ac_image).show('complete cheque')
