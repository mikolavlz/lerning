import re

txt = """
    Ауди стоит 1000
    BMW стоит 900
    Audi стоит 800
"""
# первый пример
regex_rool = re.compile('\d+')
print(regex_rool.findall(txt))

#втрой прмер
# print(regex_rool.search(txt))
# s = regex_rool.search(txt)
# print('первый индекс ', s.start())
# print("последний индекс",s.end())
# print(txt[s.start():s.end()])

#замена 
print(regex_rool.sub('...',txt))
#
text = '24.01.2023'
print(findall('\D+',text))