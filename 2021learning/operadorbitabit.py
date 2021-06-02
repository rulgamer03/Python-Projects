"""
https://github.com/satuelisa/C/blob/main/Ch2/bin.txt
"""
print(14 & 23)
""" 
01110	14
10111	23
----------	& AND (1 if both are 1, otherwise 0)
00110   6	4 + 2
"""
print(14 | 23)
""" 
01110	14
10111	23
----------	| OR (0 if both are 0, otherwise 1)
11111	31	16 + 8 + 4 + 2 + 1
"""
print(14 ^ 23)
"""
01110	14
10111	23
----------	^ XOR (1 if only one is 1, otherwise 0)
11001	25	16 + 8 + 1
"""
print(14 >> 1)
"""remove the last p bits of x"""
print(14 >> 2)
"""
14 -> 1110
14/2 = 7 -> 111
7/2 = 3.5 -> 3 -> 11
"""
print(14 << 1)
"""add 1 zero to the end of 14"""
print(14 << 2)
"""
14 -> 1110
14*2 = 28 -> 11100 
28*2 = 56 -> 111000
"""
