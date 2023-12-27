import random

class Data:
    def __init__(self):
        self.names = self._read_names()
        self.country_code = ['AF', 'AL', 'DZ', 'AD', 'AO', 'AG', 'AR', 'AM', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB',
                             'BY', 'BE', 'BZ', 'BJ', 'BT', 'BO', 'BA', 'BW', 'BR', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM',
                             'CA', 'CV', 'CF', 'TD', 'CL', 'CN', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU',
                             'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FJ',
                             'FI', 'FR', 'GA', 'GM', 'GE', 'DE', 'GH', 'GR', 'GD', 'GT', 'GN', 'GW', 'GY', 'HT', 'VA',
                             'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IL', 'IT', 'JM', 'JP', 'JO', 'KZ',
                             'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MK',
                             'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MR', 'MU', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME',
                             'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'KP', 'MP',
                             'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PL', 'PT', 'QA', 'RO', 'RU',
                             'RW', 'KN', 'LC', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SK', 'SI',
                             'SB', 'SO', 'ZA', 'KR', 'SS', 'ES', 'LK', 'SD', 'SR', 'SZ', 'SE', 'CH', 'SY', 'PF', 'TW',
                             'TJ', 'TZ', 'TH', 'TL', 'TG', 'TO', 'TT', 'TN', 'TR', 'TM', 'TV', 'UG', 'UA', 'AE', 'GB',
                             'US', 'UY', 'UZ', 'VU', 'VE', 'VN', 'EH', 'YE', 'ZM', 'ZW']

        self._emails = ['gmail.com', 'hotmail.com', 'yahoo.com']

    def generate_cell_number(self):
        s = '05'
        r = random.randint(10000000, 99999999)
        return f'{s}{r}'

    def get_country_code(self):
        c = random.choice(self.country_code)
        return c

    def get_name(self):
        n = random.choice(self.names)
        return n

    def get_email(self, name=None):
        if not name:
            name = self.get_name()
        email = random.choice(self._emails)
        return f'{name}@{email}'

    def _read_names(self) -> list:
        ret = []
        with open('names.txt', 'r+') as file:
            lines = file.readlines()
            for line in lines:
                ret.append(line[0:-1])
        return ret

if __name__ == '__main__':
    d = Data()
    print(d.get_country_code())
    print(d.generate_cell_number())
    print(d.get_name())
    print(d.get_email('aaa'))
    print(d.get_email())
