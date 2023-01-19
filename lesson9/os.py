import os
# from os import *
# os.makedirs('c:/test/',exist_ok=True)   #создание папки

my_dir = 'c:/test'
content = os.listdir(my_dir)              #список содержимого в папке
print(content)
text_file = []
for item in content:
    if os.path.isfile(os.path.join(my_dir,item)) and item.endswith('.txt'):
        text_file.append(item)
print(text_file)