# -*- coding: utf-8 -*
import random
def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
mingwen = raw_input('请输入明文：')

#将明文转化为二进制
firstChange = encode(mingwen).replace(' ','')
firstChange =firstChange.zfill(64)
#print firstChange
ipList = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
    ]
ipList1 = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41,  9, 49, 17, 57, 25,
    ]
#IP初始置换
firstChange1 = []
for i in range(1, 65):
    a = ipList[i - 1]
    #print a
    firstChange1.append(firstChange[a - 1])
    i += 1
#print firstChange1
#分为前后32位两部分
firstChange11 = firstChange1[:32]
firstChange12 = firstChange1[32:]
#print firstChange11 , '\n', firstChange12

#扩展E变换
eList = [
    32,  1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
    ]
extendR = []
for j in range(48):
    extendR.append(firstChange12[eList[j] - 1])
    j += 1
print extendR
