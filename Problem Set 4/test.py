# def mystery(x, y):
#     if y > x:
#         return y - 1
#     # print(x, y)
#     return 3 + mystery(x // 2, y + 1)


# def sum(lst):
#     if lst==[]:
#         return 0
#     else:
#         rest = sum(lst[1:])
#         if lst[0]%2==1:
#             return rest+lst[0]
#         else:
#             return rest

# print(sum([1,3,2,88,2,2,0,2,1]))


def double(s):
    if s == '':
        return ''
    else:
        rest = double(s[1:])
        if s[0] in ['a','e','i','o','u']:
            return s[0]*2+rest
        else:
            return s[0]+rest


# print(double('time'))


def mystery(x):
    lc = [y % 3 for y in range(x)]
    return sum(lc)

x = 4
y = 2
print(x, y)
y = mystery(y)
print(x, y)
x = mystery(x)
print(x, y)

