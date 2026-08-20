import os
from Cuenta import Cuenta
cuentas = []
while True:
    print("1. crear Cuenta")
    print("2. consignar")
    print("3. retirar")
    print("4. saldo")
    print("5. salir")
    opcion = input ("Digite opcion:")
    if opcion == "1":
        numero  = int(input("numero Cuenta:"))
        tipo    = input("numero tipo:")
        valor   = float(input("numero valor Inicial:"))
        o = Cuenta(numero, tipo, valor)
        cuentas.append(o)
    elif opcion == "2":
        numero  = int(input("numero Cuenta:"))
        for x in cuentas:
            if x.getNumero() == numero:
                monto   = float(input("Monto a consignar:"))
                x.consignar(monto)
                break
    elif opcion == "3":
        numero  = int(input("numero Cuenta:"))
        for x in cuentas:
            if x.getNumero() == numero:
                monto   = float(input("Monto a retirar:"))
                x.retirar(monto)
                break
    elif opcion == "4":
        numero  = int(input("numero Cuenta:"))
        for x in cuentas:
            if x.getNumero() == numero:
                print(f"El saldo actual es {x.getSaldo()}")
    input("digite enter")
    os.system("cls")

