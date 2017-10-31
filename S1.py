# coding=UTF-8
import random
a = random.randint(0, 63)
a = bin(a)
b = str(a)
new_b = b[2:]
s = new_b.zfill(6)
print '六位二进制为：',s
first = s[0]
last = s[5]
mid = s[1:5]
print first, ' ', last, ' ',mid
hang = int('%s%s' % (first, last), 2)
lie = int('%s' % mid, 2)
print '行数为：',hang,'\n', '列数为：',lie
S1=[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
  15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
]
if hang == 0:
    final = S1[lie]
elif hang == 1:
    final = S1[lie+16]
elif hang == 2:
    final = S1[lie + 32]
elif hang == 3:
    final = S1[lie + 48]
else:
    final = S1[lie + 64]
print '十进制为：', final
final = bin(final)
new_final = final[2:]
new_final = str(new_final)
siwei = new_final.zfill(4)
print '经S1盒置换后的四位二进制数为：',siwei

