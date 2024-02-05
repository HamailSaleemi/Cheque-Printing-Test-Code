from drawimage import DrawImage

def cheque_image():
    cheque_width = int(297 / 25.4 * 96)
    cheque_height = int(210 / 25.4 * 96)
    cheque = DrawImage(cheque_width, cheque_height,'white')
    cheque.insert_text(0,0, 'hello world', 'black')
    return cheque

def payee_header():
    # cheque_width = int(297 / 25.4 * 96) # 1122
    # cheque_height = int(210 / 25.4 * 96) # 793
    header = DrawImage(400, 400, 'white', transparent=True)
    # line points
    x1, y1 = 150, 400
    x2, y2 = 250, 400
    header.insert_line(x1, y1, x2, y2)
    y1 += 50
    y2 += 50
    header.insert_line(x1, y1, x2, y2)
    header.insert_text(400, 410, 'A/C PAYEE ONLY','black')
    return header