
print("1: de dolares a euros")
print("2: de euros a dolares")
print("3: de pesos mexicanos a dolares")
print ("")
hl=int(input("Elije una opcion: "))
print ("")


if hl==1:
    dol3=int(input("introduce cantidad de dolares: "))
    euros=dol3*18.57
    print("")
    print("euros=", euros)
if hl==2:
    euros1=int(input("introduce cantidad de euros: "))
    dol4=euros1*17.27
    print("")
    print("dolares=", dol4)
if hl==3:
    pesm=int(input("Introduce cantidad de pesos : "))
    dol5=pesm*17.27
    print("")
    print("dolares=", dol5)
