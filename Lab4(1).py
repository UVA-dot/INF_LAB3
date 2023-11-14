def func_check_if_list_or_tag(s: list, t: str, i: int, k: int, cnt_tab: int, cnt_sp: int):
    if i == len(s):
        if k == 2:
            return 0
        else:
            return 1
    elif cnt_tab * '\t' + cnt_sp * ' ' + t in s[i][:s[i].find('<')] :
        return func_check_if_list_or_tag(s, t, i + 1, k + 1, cnt_tab, cnt_sp)
    else:
        return func_check_if_list_or_tag(s, t, i + 1, k, cnt_tab, cnt_sp)


def func_find_end_tag(s: list, t: str, i: int):
    if s[i].count(t) == 1:
        return i
    else:
        return func_find_end_tag(s, t, i + 1)


def func_find_all_list(s: list, t: str, i: int, k: int, cnt_tab: int, cnt_sp: int):
    return 0


def func_rec_parser_xml_to_json(s: list, i: int):
    print('\n'.join([i for i in s]))
    if s[i][:s[i].find('<')].count(' ') < s[i + 1][:s[i + 1].find('<')].count(' ') or s[i][:s[i].find('<')].count('\t') < s[i + 1][:s[i + 1].find('<')].count('\t'):
        if func_check_if_list_or_tag(s, s[i][s[i].find('<') + 1:s[i].find('>')], 0, 0, 0, 0) == 1:
            s[i] = s[i].replace('<', '"', 1).replace('>', '": {', 1)
            end_tag = func_find_end_tag(s, s[i][s[i].find('"') + 1: s[i].rfind('"')], i + 1)
            s[end_tag] = s[end_tag].replace(s[end_tag][s[end_tag].find('<'):], '}', 1)
            if len(s) == i:
                return s
            else:
                return func_rec_parser_xml_to_json(s, i + 1)
        else:
            if len(s) == i:
                return s
            else:
                return func_rec_parser_xml_to_json(s, i + 1)
    else:
        if s[i].count(s[i][s[i].find('<') + 1:s[i].find('>')]) > 1:
            s[i] = s[i].replace(s[i][s[i].rfind('<'):s[i].rfind('>') + 1], '",', 1).replace('<', '"', 1).replace('>', '": "', 1)
            if len(s) == i:
                return s
            else:
                return func_rec_parser_xml_to_json(s, i + 1)
        else:
            s[i] = s[i].replace('<', '"', 1).replace('/>', '": null,')
            if len(s) == i:
                return s
            else:
                return func_rec_parser_xml_to_json(s, i + 1)


f = open("новый 1.xml", 'r', encoding="UTF-8")
xml = ''
for another_string in f:
    xml += another_string
JSON = ''
xml = xml.split('\n')
del xml[0]
print(xml[6].count('\t'), xml[7].count('\t'), xml[6].count(' '), xml[7].count(' '))
print('\n'.join([i for i in func_rec_parser_xml_to_json(xml, 0)]))
