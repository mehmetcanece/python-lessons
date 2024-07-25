# +,-,*,/

num1 = int(input("Sayı giriniz."))
num2 = int(input("Sayı giriniz."))
islem = input("Yapmak istediğiniz işlemi giriniz. +,-,*,/")

if islem == '+':
    print(num1+num2)
if islem == '-':
    print(num1-num2)
if islem == '*':
    print(num1*num2)
if islem == '/':
    print(num1.__float__()/num2.__float__())





