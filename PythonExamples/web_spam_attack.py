from threading import Thread, RLock

import requests

url = 'https://forms-il.com/wp-admin/admin-ajax.php'

if __name__ == '__main__':

    headers = {
        'authority': 'forms-il.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryQYoNuLBSzI85gXTr',
        'origin': 'https://forms-il.com',
        'referer': 'https://forms-il.com/',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
        'x-requested-with': 'XMLHttpRequest',
    }

    numbers_locker = RLock()
    number = 1000

    def get_next_number():
        global number
        with numbers_locker:
            ret = number
            number += 1
        return ret

    def execution_func():
        while True:
            a = get_next_number()
            if not a:
                break
            somephonenumber = f'055555{a}'
            somename = f'somename{a}'
            data = '------WebKitFormBoundaryQYoNuLBSzI85gXTr\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n9\r\n------WebKitFormBoundaryQYoNuLBSzI85gXTr\r\nContent-Disposition: form-data; name="form_id"\r\n\r\n350d77d\r\n------WebKitFormBoundaryQYoNuLBSzI85gXTr\r\nContent-Disposition: form-data; name="referer_title"\r\n\r\n\r\n------WebKitFormBoundaryQYoNuLBSzI85gXTr\r\nContent-Disposition: form-data; name="queried_id"\r\n\r\n9\r\n------WebKitFormBoundaryQYoNuLBSzI85gXTr\r\nContent-Disposition: form-data; name="form_fields[name]"\r\n\r\n' + somename + '\r\n------WebKitFormBoundaryQYoNuLBSzI85gXTr\r\nContent-Disposition: form-data; name="form_fields[email]"\r\n\r\n' + somephonenumber + '\r\n------WebKitFormBoundaryQYoNuLBSzI85gXTr\r\nContent-Disposition: form-data; name="action"\r\n\r\nelementor_pro_forms_send_form\r\n------WebKitFormBoundaryQYoNuLBSzI85gXTr\r\nContent-Disposition: form-data; name="referrer"\r\n\r\nhttps://forms-il.com/\r\n------WebKitFormBoundaryQYoNuLBSzI85gXTr--\r\n'
            response = requests.post('https://forms-il.com/wp-admin/admin-ajax.php', headers=headers, data=data)
            print(f'{a} {response}')

    for _ in range(30):
        Thread(target=execution_func, daemon=True).start()

    input('Enter to exit')
