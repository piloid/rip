def f(h):
    s=0
    mxsum=0
    for e in h:
        s += e
        if s < 0:
            s = 0
        if s > mxsum:
            mxsum = s

    return mxsum



print(f([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

