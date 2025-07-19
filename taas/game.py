from get_taas import get_taas

dast = 0
for taas in get_taas:
    print(taas)
    if dast > 5:
        break
    else:
        dast += 1