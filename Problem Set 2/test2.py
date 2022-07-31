def mystery(a, b):
    if a == b:
        return a
    else:
        myst_rest = mystery(a + 1, b - 2)
        return b + myst_rest

print(0.9)