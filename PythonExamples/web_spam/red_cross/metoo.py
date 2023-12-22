import time
from threading import Thread

import requests

from PythonExamples.web_spam.red_cross.data import Data

headers = {
    'Referer': 'https://www.metoo-unlessurajew.com/_partials/wix-thunderbolt/dist/clientWorker.315bbd37.bundle.min.js',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Authorization': 'MjdCFQs2dSDuAi0-DqNBr_6t8CStvKPcjtNnyi4Jpc0.eyJpbnN0YW5jZUlkIjoiODEzZTBhODAtOGU5MC00ZDBiLTk2OTQtZjhmZWE5YjQ1MjcwIiwiYXBwRGVmSWQiOiIxNGNlMTIxNC1iMjc4LWE3ZTQtMTM3My0wMGNlYmQxYmVmN2MiLCJtZXRhU2l0ZUlkIjoiOTAzYjQ0M2YtYjMxMS00ZmU0LWI4MzktMWUxODliNGFiNmIzIiwic2lnbkRhdGUiOiIyMDIzLTExLTIwVDE3OjEwOjI5LjI2NVoiLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiJhNTE4MjgzMy1kMDljLTQxMmQtOGFmNC0yNDVlYTIxYzI2OTAiLCJhaWQiOiJjNTY4MzgwZi1lMTdmLTRiZjAtOWY4OC0wM2VjODAyNzVjZmQiLCJiaVRva2VuIjoiMTEwNTRlYmYtM2Q4MS0wMmVmLTJlYWQtZTZlNjMyZmVlNGMzIiwic2l0ZU93bmVySWQiOiI0NmM4YTFlZi05NDEwLTQ0ZGQtODMyZC01NDgxMzI2ZmFlNTEifQ',
    'X-Wix-Client-Artifact-Id': 'wix-form-builder',
    'Content-Type': 'application/json',
}

json_data = {
    'formProperties': {
        'formName': 'עצומה דף הבית',
        'formId': 'comp-lowxhka5',
    },
    'emailConfig': {
        'sendToOwnerAndEmails': {
            'emailIds': [],
        },
    },
    'viewMode': 'Site',
    'fields': [
        {
            'fieldId': 'comp-lowxhka9',
            'label': 'First name',
            'firstName': {
                'value': 'aaaaaaa',
            },
        },
        {
            'fieldId': 'comp-lowxhkal1',
            'label': 'Last name',
            'lastName': {
                'value': 'bbbbbbb',
            },
        },
        {
            'fieldId': 'comp-lowxhkap1',
            'label': 'Email',
            'email': {
                'value': 'my@email.com',
                'tag': 'main',
            },
        },
        {
            'fieldId': 'comp-lowxhkat',
            'label': 'I agree to receive updates about the campaign',
            'additional': {
                'value': {
                    'checkbox': True,
                },
            },
        },
    ],
    'labelKeys': [
        'custom.zwmh-2',
    ],
}

if __name__ == '__main__':
    d = Data()

    def func():
        print('******************* starting thread')
        for a in range(100):
            json_data['fields'][0]['firstName']['value'] = d.get_name()
            json_data['fields'][1]['lastName']['value'] = d.get_name()
            json_data['fields'][2]['email']['value'] = d.get_email(json_data['fields'][0]['firstName']['value'])

            response = requests.post('https://www.metoo-unlessurajew.com/_api/wix-forms/v1/submit-form',
                                     headers=headers,
                                     json=json_data)
            print(f"{a} {json_data['fields'][2]['email']['value']} response{response}")
            time.sleep(4)
    for _ in range(1):
        t = Thread(target=func, daemon=True)
        t.start()

    input('enter to continue')
