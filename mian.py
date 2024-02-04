from drawimage import DrawImage


image = DrawImage(width=700, height=200)

# upper line upper
x1, y1 = 0, 5
x2, y2 = 100, 5
image.insert_line(x1, y1, x2, y2)

# insert payee only text
payee_text = image.insert_text(5, 7, write_text='AC PAYEE ONLY', color='black')

payee_name = image.insert_text(40, 60, write_text='**Hamail Saleemi**', color='black')

# upper line lower
y1 += 15
y2 += 15
image.insert_line(x1, y1, x2, y2)

image.save_image('main.png')