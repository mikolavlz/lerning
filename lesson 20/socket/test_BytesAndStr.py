s = 'Python'
bs = b'Python'
# ba = bytearray(bs)
# # print(ba)

s2 = bs.decode('cp1251') #из строки в байты
print(s2)
bs2 = s.encode('koi8-r')# из байтов в строку
print(bs2)