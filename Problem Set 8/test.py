# for i in [2, 3]:          # put the output below:
#     for j in range(1, i):
#         print(i, j)
#     print(i, j)


# def foo(a, b):        # put the output below:
#     for i in range(len(a)):
#         a[i] *= 2
#         b += 1
#     print(a[3], b)
# a = 42
# b = [1, 2, 3, 4]
# c = b
# foo(c, a)
# print(b[3], a)

# def scale(grid, scalar):
#     for r in range(len(grid)):
#         for c in range(len(grid[0])):
#             grid[r][c] *= scalar


def sum(a,b):
    ans = [[0 for col in range(len(a[0]))] for row in range(len(a))]
    for r in range(len(a)):
         for c in range(len(a[0])):
             ans[r][c] = a[r][c]+b[r][c]
    return ans

a = [[1, 2, 3], [4, 5, 6]]
b = [[2, 2, 2], [3, 3, 3]]
c = sum(a, b)
print(c)

