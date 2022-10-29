# リスト・タプル・辞書 https://www.tohoho-web.com/python/list.html

### リスト
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
a1 = a[0]       # 0番目: 'A'
a2 = a[2]       # 2番目: 'C'
print(a1, a2)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = a[2:4]     # 2番目から3番目: [2, 3]
a2 = a[2:]      # 2番目から最後: [2, 3, 4, 5, 6, 7, 8, 9]
a3 = a[:4]      # 最初から3番目: [0, 1, 2, 3]
print(a1, a2, a3)

# [n:m:s] は s個とばしで参照します。
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = a[1:8:2]            # 1番目から7番目まで2個とばし: [1, 3, 5, 7]
print(a1)

### タプル
### (...) で要素を並べたものをタプル(tuple)と呼びます。タプルはリストとほぼ同じように使用できますが、要素を変更できない点が異なります。

a1 = [10, 20, 30, 40]
a2 = (10, 20, 30, 40)

a1[2] = 60              # 代入できる
# a2[2] = 60              # エラーとなり、TypeError例外が発生する

### 辞書dict
d = {'Yamada': 30, 'Suzuki': 40, 'Tanaka': 80}
d1 = d['Yamada']
print(d1)

d['Kimura'] = 60
print(d)


# 全ての要素や値を参照するには、items(), keys(), valus(), items() を使用します。参照される要素の順序は**順不同**です。

d = {'Yamada': 30, 'Suzuki': 40, 'Tanaka': 80}

for k, v in d.items():
    print(k, v)            # Tanaka 80, Yamada 30, Suzuki 40

for k in d.keys():
    print(k, d[k])         # Suzuki 40, Yamada 30, Tanaka 80

for v in d.values():
    print(v)               # 80, 30, 40

### リスト関数(map(), filter(), reduce())
# map
# map() はリストの各要素に対して処理を行い、行った結果を返します。下記の例では各要素を2倍にする処理を行います。
a = [1, 2, 3]

def double(x): return x * 2

print(list(map(double, a)))                  #=> [2, 4, 6] : 関数方式
print(list(map(lambda x: x * 2, a)))         #=> [2, 4, 6] : lambda方式
print([x * 2 for x in a])                    #=> [2, 4, 6] : リスト内包表記

# filter
# filter() はリストの各要素に対して処理を行い、処理結果が真となる要素のみを取り出します。下記の例では各要素から奇数のみを取り出します。
a = [1, 2, 3]

def isodd(x): return x % 2
print(list(filter(isodd, a)))              #=> [1, 3] : 関数方式
print(list(filter(lambda x: x % 2, a)))    #=> [1, 3] : lambda方式
print([x for x in a if x % 2])             #=> [1, 3] : リスト内包表記

# reduce
# reduce() はリストの最初の2要素を引数に処理を呼び出し、結果と次の要素を引数に処理の呼び出しを繰り返し、単一の結果を返します。下記の例では、各要素の合計を計算しています。
from functools import reduce

a = [1, 2, 3, 4, 5]

def add(x, y): return x + y
print(reduce(add, a))                  #=> 15 : 関数方式
print(reduce(lambda x, y: x + y, a))   #=> 15 : lambda方式






