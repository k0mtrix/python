# python
# Kafe uchun hisobchi tizim
# 05.10.2025
# muallif: Komiljon

menu=[]
narxlar=[]
narx=0

status=input('Statusingizni kiriting:')
status=status.lower()
if status=='admin':
    boshqaruv=input('\nNima ish qilammiz:\nBuyurtmani hisoblash uchun 1 ni yuboring\nMenuga mahsulot qo\'shish uchun 2 ni yuboring\n>>>')
    if boshqaruv=='1':
        for i in range(len(menu)):
            soni=int(input(f'{menu[i]}dan nechta:'))
            narx+=narxlar[i]*soni
        print(f'Jami: {narx} so\'m')
    elif boshqaruv=='2':
        maxsulot=input('Taom nomi:')
        maxsulot=maxsulot.lower()
        narxi=int(input(f'{maxsulot} narxini kiriting:'))
        menu.append(maxsulot)
        narxlar.append(narxi)
        print('Maxsulot muoffaqiyatli qo\'shildi')
    else:
        print('Bunday amal mavjud emas. DASTUR TUGADI!!!')
elif status=='mijoz':
    for j in range(len(menu)):
        print(f'{menu[j]}-----{narxlar[j]} so\'m')
else:
    print('DASTUR TUGADI!!!')
