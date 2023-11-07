import re
# Вар 0
tests = ['sSTUDSUDUSsd_d__sd.spam@yandex.ru',
         'AnaNAS@@mail.ru',
         'Flappybirdposh___ds@gmailru',
         'Ananas@ananas',
         'AAA_TRain__@mail.ru',
         'AA_STRAIN_@dot.com.com']
pattern = r"[a-zA-Z0-9._]{1,}(@[a-zA-Z.]{1,}[.](?:com|ru))"
for i in tests:
    match = re.findall(pattern, i)
    if len(match) == 0:
        print('Fail!')
    else:
        for j in match:
            print(j)
