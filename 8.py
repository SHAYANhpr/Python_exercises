mablagh = int(input('enter your mablagh: '))
if mablagh > 50000:
    takhfif = (mablagh*20)//100
elif 20000 <= mablagh <= 50000:
    takhfif = (mablagh*10)//100
elif mablagh < 20000:
    print("takhfif emal nmishavad")
else:
    takhfif = mablagh

n_mablagh = mablagh - takhfif
print(n_mablagh) 