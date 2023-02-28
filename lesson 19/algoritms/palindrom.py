def Palindrome(s):
    rev = ''.join(reversed(s))

    if (s == rev):
        print('Полиндром')
    else:
        print('НЕ Полиндром')


s = "анна"
ans = Palindrome(s)