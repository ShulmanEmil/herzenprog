import pyqrcode
import png

def qr_simple(str_input):
    QR = pyqrcode.create(str_input)
    QR.png('qr.png', scale=13)

if __name__ == '__main__':
    input_str = input('Введите строку: ')
    qr_simple(input_str)
