# https://www.tohoho-web.com/python/function.html

### def
def add(x, y):
    print(x + y)
add(3, 5)

# return
def add2(x, y):
    ans = x + y
    return ans

n = add2(3, 5)
print(n)            #=> 8

# 複数の値をreturn
def func():
    return 3, "ABC"

n, s = func()
print(n, s)              #=> 3 ABC
