# 制御構文 https://www.tohoho-web.com/python/control.html

### if, else, elsif
num = 12
if num > 10:
    print('BIG')
elif num == 10:
    print('NORMAL')
else:
    print('SMALL')

### while, else
n = 0
while n < 10:
    print(n)
    n += 1
else:
    print('END')

### for
for n in [1, 2, 3]:          # 配列
    print(n)                 #=> 1, 2, 3

for n in (1, 2, 3):          # タプル
    print(n)                 #=> 1, 2, 3

for c in "ABC":              # 文字列
    print(c)                 #=> A, B, C

for k in {'one': 1, 'two': 2, 'three': 3}:   # 辞書
    print(k)                                 #=> one, two, three

for line in open("./in/sample.txt"):              # ファイルの中身
    print(line)                              # 1行ずつ表示

for n in range(10):
    print(n)

### break
for n in range(10):
    if n == 5:
        break
    print(n)                 # 0, 1, 2, 3, 4

### continue
for n in range(10):
    if n == 5:
        continue
    print(n)                 # 0, 1, 2, 3, 4, 6, 7, 8, 9
