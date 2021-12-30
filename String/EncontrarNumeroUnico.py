def unique(a):
    
    k=0
    while k < len(a):
        if a[k] in a[k+1:]:
            a.pop(k)
        else:
            k=k+1

    return a
