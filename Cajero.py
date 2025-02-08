Saldo=0
while True: 
    print('\t.:MENU:.')
    print('1. Ingresar dinero en la cuenta:')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero de la cuenta')
    print('4. Expulsar tarjeta')

    opcion = int(input('Digite una opcion de menu:'))

    print()

    if opcion ==1:
       Saldo==0
       deposito = int(input('Cuanto la cantidad de dinero desea depositar:'))
    else Saldo = deposito
        
    if Saldo >0:
        Saldo += deposito

        print(f'Dinero de la cuenta es : {Saldo}')
    elif opcion == 2:
        retirar = int(input('Ingrese la cantidad a retirar:'))
        if retirar>Saldo:
            print(f'El saldo a retirar es mayor al q usted tiene en la cuenta:')
        else:
            saldo -= retirar

            print(f'El saldo restante es:{saldo}')
    elif opcion == 3:
        print(f'El saldo de su cuenta es:')
        
    elif opcion== 4:
        print(f'Su tarjeta a sido explulsada:')
        break
    else:
        print('Error, se equivocó de opción de menu, ingrese una opción correcta:')
 
print()