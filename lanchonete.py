print("\n",  '-' *20 ," STOP GOOD",'-' *20 ,)
print(' '   *22 ,  " Menu",' ' *20 ,)
print('\n',' ' *9,'1','|',    "       coxinha       " '|' ,'R$ 3,00')
print( ' '   *9 ,' 2','|',    "       rissoles      " '|','R$ 3,00')
print( ' '   *9 ,' 3','|',    "       bolinhão      " '|','R$ 4,00')
print( ' '   *9 ,' 4','|',   "       fogazza       " '|','R$ 4,00')
print( '\n',' '   *21 ,"BEBIDAS")
print(  '\n',' '   *9 ,'5','|',   "  Coca-cola R$ 5,00  "'|','R$ 5,00')
print(   ' '   *9 ,' 6', '|',   "  suco R$ 5,00       " '|','R$ 7,00')
print( '\n \n ',' '   *17 ,"0 / enter = valor a pagar ")

total = 0
while True:
   op = int(input('\n' '  -->' "      escolha qual opção?  "))

   if   ( op == 1):
        qtd =int(input('\n' '  -->'"    unidades?  "))
        total = total + qtd * 3.00
   elif ( op == 2):
        qtd =int(input('\n' '  -->'"    unidades?  "))
        total = total + qtd * 3.00
   elif ( op == 3):
        qtd =int(input('\n' '  -->'"     unidades?  "))
        total = total + qtd * 4.00
   elif (op == 4):
        qtd = int(input('\n' '  -->'"    unidades?  "))
        total = total + qtd * 4.00
   elif (op == 5):
        qtd = int(input('\n' '  -->'"    unidades?  "))
        total = total + qtd * 5.00
   elif (op == 6):
        qtd = int(input('\n' '  -->'"    unidades?  "))
        total = total + qtd * 7.00
   elif(op== 0):
        break

print( '  \n   '  f"  TOTAL=     R${total} ")
print('\n''volte sempre!!')