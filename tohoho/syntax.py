# https://www.tohoho-web.com/python/syntax.html

### Hello world
print('hello world')

### 文・式
# 文を数行に分けて記述
total = 123 \
      + 456 \
      + 789
print(total)

### インデント
a = 3
if a == 5:
    print("AAA")        # if文の対象
    print("BBB")        # if文の対象
print("CCC")            # if文の対象ではない

### print
print(3)                   #=> 3
print([1, 2, 3])           #=> [1, 2, 3]
print((1, 2, 3))           #=> (1, 2, 3)
print({'k1':10, 'k2':20})  #=> {'k2': 20, 'k1': 10}

# 改行
print("AAA", end="")        # 改行しない
print("BBB")                # 改行する

# フォーマット
print("My name is %s." % "Tanaka")
print("%s is %d years old." % ("Tanaka", 28))
print("%(name)s is %(age)d years old." % {'name': "Tanaka", 'age': 28})

f = open("./test.txt", "w")
print("Hello world!", file=f)
f.close()
