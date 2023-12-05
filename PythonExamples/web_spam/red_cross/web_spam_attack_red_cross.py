import random
from threading import Thread
import requests

from PythonExamples.web_spam.red_cross.data import Data

# https://www.icrc.org/en/contact/

cookies = {
    'ICRCAppGwAffinityCORS': 'a1d09764a05c45e4f6c1968a400f8ea6',
    'ICRCAppGwAffinity': 'a1d09764a05c45e4f6c1968a400f8ea6',
    'userVisitedBefore': '1',
    'cookieAlertAccepted': '1',
}

headers = {
    'authority': 'www.icrc.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'ICRCAppGwAffinityCORS=a1d09764a05c45e4f6c1968a400f8ea6; ICRCAppGwAffinity=a1d09764a05c45e4f6c1968a400f8ea6; userVisitedBefore=1; cookieAlertAccepted=1',
    'origin': 'null',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

message_red_cross = []
message_red_cross.append(
    """To the Red Cross Our hearts ache. After surviving one of the worst massacres in modern Jewish history, hundreds of our innocent civilians were forcibly taken hostage and dragged kicking and screaming into the underground hell tunnels of Gaza: babies, children, teens, young men and women, mothers, fathers, grandmothers, grandfathers. Surely the Red Cross cannot fail to recognize these events as War Crimes against humanity! We call upon the Red Cross to fulfill their mission to protect the lives and dignity of these helpless victims, and to provide them with assistance.""")
message_red_cross.append(
    """Surely the Red Cross is not going to reprise their historic abandonment of Jewish victims of acts of terror and War Crimes? Hundreds of innocent Israeli civilians and those of other nations were taken hostage and dragged into the underground hell tunnels of Gaza: babies, children, teens, young men and women, mothers, fathers, grandmothers, grandfathers. We call on the Red Cross NOW to fulfill its mission: to protect the lives and dignity of victims of armed conflict and other situations of violence and to provide them with assistance. NOW is the time for the Red Cross to demonstrate to the Jewish people and to the world that it is truly an impartial, neutral and independent organization with an exclusively humanitarian mission.""")
message_red_cross.append(
    """What is happening to our babies and children, youth, young men and women, mothers and fathers, grandmothers and grandfathers, there in the hell tunnels of Gaza, where they have been held hostage for weeks on end? Where is the Red Cross, whose stated mission is to protect the lives and dignity of such victims to provide them with assistance? We call on the Red Cross: DEMAND to visit, to comfort, to care for, to act to RELEASE our hostages! TODAY!""")
message_red_cross.append(
    """In the aftermath of one of the most devastating massacres in contemporary Jewish history, our hearts are heavy with sorrow. The relentless horror continues as hundreds of our innocent civilians, ranging from infants to grandparents, are forcefully held captive, their cries echoing in the subterranean depths of Gaza's hellish tunnels. We implore the Red Cross to unequivocally acknowledge these heinous acts as War Crimes against humanity. Our desperate plea echoes the principles of the Red Cross, urging them to fulfill their sacred mission by protecting the lives and preserving the dignity of these vulnerable victims, extending the hand of assistance they so desperately need.""")
message_red_cross.append(
    """As the specter of history threatens to repeat itself, we stand on the precipice of another tragic abandonment of Jewish victims subjected to acts of terror and War Crimes. Countless lives, spanning generations and nationalities, now languish in the underground abyss of Gaza. The urgency of this moment demands immediate action from the Red Cross. We call upon them, in no uncertain terms, to honor their mission without delay: safeguard the lives and dignity of those ensnared in the brutality of armed conflict and violence. The time is now for the Red Cross to prove its impartiality, neutrality, and independence, demonstrating an unwavering commitment to an exclusively humanitarian cause that transcends borders and prejudices.""")
message_red_cross.append(
    """In the harrowing depths of Gaza's hell tunnels, our babies, children, youth, mothers, fathers, and grandparents endure weeks of unimaginable captivity. The Red Cross, charged with the noble responsibility to protect lives and uphold human dignity, seems absent in this critical hour. We urgently beseech the Red Cross to act decisively: demand access, provide solace, offer care, and actively work towards the swift release of our hostages. The plea is clear and immediate – the Red Cross must fulfill its mandate TODAY, embodying the essence of its humanitarian mission to alleviate the suffering of the innocent.""")
message_red_cross.append(
    """In the shadows of despair, a tragedy unfolds as the innocent souls of our community endure one of the darkest chapters in their history. Stripped of their freedom, hundreds of civilians, spanning every generation, have become captives in the subterranean labyrinths of Gaza. The Red Cross, guardian of humanity's conscience, must rise to the occasion. Recognize this plea, respond to the cries for justice, and fulfill your sacred duty to safeguard lives and uphold the dignity of those ensnared in this relentless conflict.""")
message_red_cross.append(
    """As the echoes of tragedy reverberate through the hearts of our people, we find ourselves ensnared in a nightmare where the youngest and oldest among us suffer in the depths of Gaza's underground prisons. The Red Cross, an emblem of hope, must not turn a blind eye to this humanitarian crisis. In the spirit of impartiality, neutrality, and independence, we implore the Red Cross to act swiftly, break the chains that bind our loved ones, and restore the dignity that has been cruelly stolen from the victims of this unconscionable warfare.""")
message_red_cross.append(
    """Within the oppressive silence of Gaza's subterranean confinement, the cries of our beloved echo through the darkness. Innocent lives, from the cradle to the twilight years, held captive in the hellish tunnels. The Red Cross, charged with the noble duty of protecting humanity, we beseech you to heed our call. Let the principles of your mission guide you to intervene, to comfort, to liberate the hostages who await the light of freedom. Today, let the world witness the strength of your impartiality and the resolve of your humanitarian mission.""")

if __name__ == '__main__':
    def func():
        print('******************* starting thread')
        data = {
            'subject': 'OTHER',
            'country_code': 'DE',
            'name': 'aaaaaaaaaaaaaaaaa',
            'email': 'aaaa@bbb.com',
            'message': 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
            'formSubmit': 'submit',
            'g-recaptcha-response': '03AFcWeA41eYcnmkFREO6lRRGWxz5zx93OwKCowbMpHrtOZhzBEdB5lYjjpWLb9N71YQsZXnJ2Zg0VDNrfGBXEpx7fjUJk97VpjcLZcMP6v_EXT57w4kMdUSjsfM_cOi5cPqRRdOD3PeSyG-yDOPHEDJHI-BfJsjBcRmK-GByOp3gT4npgwif05vsTQFcAjdN-VZc2upX9SzqFNi2_3dahwWbJO0n7yLfkkq_bZ3zCKh_BoyhoNtuZvGF3avu7xNi3MVpazRLkdpWl4yZjiJV8jKl-9JEAEeZF2pr5PjChugWAV1TsaFNVJzM557-jEcH9zJYJrrecYnuA61RynVa4RwCAYGM0sOtJNvsWontJ2n3JgQhu3T2C5KmYC9jg9Oqcv6jaanLC8VNAmANI5clcdy8XLZL93YyPDZPv5hI0SHv8y5QGg03vjHUuBFwK1f6cZptsseFeu2h9n3DnkiBKV2t7emBJcdaoSvwuQypzxpuRIBzWmz-GiBH19GfLhg8wdr10KEl4DjcW4vYwQP2nB1IHKBqEfUcGluRETZu2HxXpPtiQt298lD5FopbzPLBbwp0bCXWzhxWN_C31DcDBcNt7nPxZgV1ZiA',
        }
        for a in range(100):
            d = Data()
            data['country_code'] = d.get_country_code()
            data['name'] = d.get_name()
            data['email'] = d.get_email(data['name'])
            data['message'] = random.choice(message_red_cross)

            # print(data)
            response = requests.post('https://www.icrc.org/en/contact/', cookies=cookies, headers=headers, data=data)
            print(f"{a} {data['name']} response{response}")
            # print('-------------------------------------------------------------')

    for _ in range(10):
        t = Thread(target=func, daemon=True)
        t.start()

    input('enter to continue')
