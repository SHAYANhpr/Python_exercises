def skyline(*args):
    if not args:
        return 0
    else:
        return max(args)
    
print(skyline(3, 15, 2, 9))
print(skyline(1, 1, 1, 1))
print(skyline())