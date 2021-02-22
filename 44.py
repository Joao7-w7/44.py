print('{:=^40}'.format('\033[4;33mLOJAS MIGUEl\033[m'))
Preço = float(input('Preço das compras:R$'))
print('''\033[4;36mFORMAS DE PAGAMENTO\033[m
[1] a vista dinheiro/cheque
[2] a vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('\033[4;34mQual e a opção?\033[m'))
if opção == 1:
    total = Preço - (Preço * 10 / 100)
elif opção == 2:
    total = Preço - (Preço * 5 / 100)
elif opção == 3:
    total = Preço
    parcela = total / 2
    print('sua compra sera parcelada em 2x de R${:.2f} \033[4;32msem juros\033[m'.format(parcela))
elif opção == 4:
    total = Preço + (Preço * 20 / 100)
    totparc = int(input('\033[4;35mQuantas parcelas?\033[m '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f} \033[4;31mcom juros\033[m'.format(totparc, parcela))
else:
    total = 0
    print('\033[4;31mOPÇÃO INVALIDA DE PAGAMENTO\033[m')
print('-=-'*20)
print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(Preço, total))