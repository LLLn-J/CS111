def mystery(values):
    count = 0
    for i in range(len(values)):
        if values[i] > values[i - 1]:
            count += 1
    return count


# for x in [2, 4, 6]:
#     for y in range(1, x):
#         print(x + y)
# print(x, y)


# a = 12
# b = 4
# print(a, b)
#
# while a > 2:
#     a -= b
#     b -= 1
#     print(a, b)


# num = 5
# while num > 2:
#     num = num-1
#     print(num, end=' ')
def count_spaces(s):
    ans = 0
    for ch in s:
        if ch == ' ':
            ans += 1
    return ans

def most_spaces(lst):
    ans = [[count_spaces(s),s] for s in lst]
    return max(ans)[1]

print(most_spaces(['a b c', 'd e', 'f g h i']))

def count_below(lst,threshold):
    count = 0
    for x in lst:
        if x < threshold:
            count+=1
    return count

# print(count_below([1, 4, 8, 3, 10], 8))


# def alternates(lst):
#     for i in range(len(lst)-1):
#         if lst[i]%2 == lst[i+1]%2:
#             return False
#     return True
#
#
# print(alternates([0,2]))
