
s = 'K1KA5CB7'
# s = 'AJKDLSI412K4JSJ9D'

s = list(s)
s.sort()

str_alpha = ''
str_digit = ''
for i, e in enumerate(s):
    if e.isalpha():
        str_digit = str(sum(map(int, s[:i])))
        str_alpha = ''.join(s[i:])
        break

# print(str_alpha, str_digit)
print(str_alpha + str_digit)