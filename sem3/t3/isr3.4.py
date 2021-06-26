def rot13(letter):
    if ord("a") + 13 > ord(letter) >= ord("a"):
        return chr(ord(letter) + 13)
    elif ord("z") >= ord(letter) >= ord("a") + 13:
        return chr(ord(letter) - 13)
    else:
        return letter

def main():
    text_to_encrypt = input("Введите текст для шифрования: ")
    cipher_text = "".join(list(map(rot13, text_to_encrypt)))
    print("Результат: ", cipher_text)

main()