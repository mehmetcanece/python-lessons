
ehliyet = input("Ehliyetin var mı?")
araba = input("Araban var mı?")

if str(ehliyet) == 'var':
    ehliyet = True
else:
    ehliyet = False

if str(araba) == 'var':
    araba = True
else:
    araba = False

if bool(araba) and bool(ehliyet):
    print("Araba sürmek için daha ne bekliyorsun!")

if bool(araba) and not bool(ehliyet):
    print("Ehliyet olmadan süremezsin..")

if bool(ehliyet) and not bool(araba):
    print("Para biriktir de araba al knk.")

if not bool(ehliyet) and not bool(araba):
    print("Sürme")
