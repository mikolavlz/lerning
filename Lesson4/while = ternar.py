# суммаа неччетных чисе от 0 до 50
#
s,i = 0,0
# while i < 50:
#     if i % 2 != 0 :
#         s += 1
#     i += 1
# print(s)

while i < 50 :
    s = s + ( i if i % 2 == 1 else 0)
    i += 1
print(s)

