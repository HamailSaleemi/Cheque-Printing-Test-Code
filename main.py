
from cheque_provider import get_cheque_image

date = {
    'enabled': True,
    'text': '0  1  0  1  2  0  2  4'
}

get_cheque_image(date).show('complete cheque')
