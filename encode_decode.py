import base64
from os.path import splitext


def encode_file():
    print("[+] Encoding file...")
    with open(file_en_de, "rb") as f:
        file_encode_txt(base64.b64encode(f.read()))


def decode_file():
    print("[+] Decoding file...")
    with open(file_en_de, "rb") as f:
        file_decode_create(base64.b64decode(f.read()))


def file_decode_create(decoded_data):
    with open(splitext(file_en_de)[0], 'wb') as dec_file:
        dec_file.write(decoded_data)


def file_encode_txt(encode_data_text):
    with open(f'{file_en_de}.txt', 'wb') as enc_file:
        enc_file.write(encode_data_text)


def credits():
    print("""
               ANY FILE ENCODER AND DECODER
    """)
    print("""
     ██▀███   ▄▄▄       ██░ ██  █    ██  ██▓    
    ▓██ ▒ ██▒▒████▄    ▓██░ ██▒ ██  ▓██▒▓██▒    
    ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▀▀██░▓██  ▒██░▒██░    
    ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█ ░██ ▓▓█  ░██░▒██░    
    ░██▓ ▒██▒ ▓█   ▓██▒░▓█▒░██▓▒▒█████▓ ░██████▒
    ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░
      ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░▒░ ░░░▒░ ░ ░ ░ ░ ▒  ░
      ░░   ░   ░   ▒    ░  ░░ ░ ░░░ ░ ░   ░ ░   
       ░           ░  ░ ░  ░  ░   ░         ░  ░ code generated by Rahul.p
       """)


def main():
    global file_en_de
    print("""
            ********************
            *       Menu       *
            ********************
            *   [1] Encoding   *
            *   [2] Decoding   *
            ********************
    """)
    choice = int(input("[*] choose options :- "))
    file_en_de = input("[+] Enter file or drag and drop :- ").replace('"', '')
    if choice == 1:
        encode_file()
    else:
        decode_file()


try:
    credits()
    main()
except Exception as fail:
    print("[-] Error :- ", fail)
