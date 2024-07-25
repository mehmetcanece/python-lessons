# 18 yaşından büyük, okula gitmiyor ise. askere gelme yaşınız geldi. okula gidiyor, 18 yaşından büyük ise, okul bittiğinde askere gideceksiniz. hiçbiri değilse askerlik yaşınz gelmedi.


yas = int(input("Yaşınız?"))

if int(yas) >= 18:
    yas = True
else:
    yas = False

okul = input("Okulunuz halen devam ediyor mu? EVET/HAYIR")

if str(okul).lower() == 'evet':
    okul = True
else:
    okul = False



if yas and not okul:
        print("Askere gitme yaşınız geldi.")
elif okul and yas:
        print("Okulunuz bittiğinde askere geleceksiniz!")
else:
        print("Askerlik yaşınız gelmedi.")

        email = """
        Hi Mehmetcan,

        Here is your first code block.

        Best Regards.
        """

        print(email)