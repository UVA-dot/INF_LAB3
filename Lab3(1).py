import re

# 8<O
# 1 - 2 смайлика, 2 - 2 смайлика, 3 - 1 смайлик, 4 - 0 смайликов, 5 - 5 смайликов
tests = ['8<OSDSAD8<0 SJADSJADSADADDASDL888<8<O',
         '8<00000SDADA8JVVF8>O8<O0008888<<<<OOO',
         '8<OooOOo',
         '8<oOO',
         '88>>OOO000 8<oooOOOO88<OOo8<O8<O8<O8<O']
pattern = r"8<O"
for i in tests:
    match = re.findall(pattern, i)
    print(len(match))
