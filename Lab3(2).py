import re

# Вар 3
tests = ["Балакшин П.В. невероятно крутой преподаватель, мне очень нравится слушать его лекции. (Елхимов И.Д.)",
         "Balakshin P.V is insanely cool lecturer, i'm fond of listening to his lectures. (Elkhimov I.D.)",
         "Александр Ревва спел для Меладзе В.Ш. на концерте Киркорова А.Б. Никиты С.П. Дзюбы А.А.",
         "Новый А.П. который А.П. Паспорту а.п. ПалаЧА а.П. Джокер О.И. Бэтмен Н.В.",
         "Папарацци А.А знаю таких сказал Андрей кустарников А.Ж."]
pattern = r"([А-ЯA-Z][а-яa-z]{1,})\s[А-ЯA-Z][.][А-ЯA-Z][.]"
for i in tests:
    match = re.findall(pattern, i)
    match.sort()
    print(match)
