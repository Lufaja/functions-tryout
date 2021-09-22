getal = int(input("Van welk getal wilt u de tefal zien (1 t/m 10) : "))
def tafelVan(noemer):
    for teller in range(1, 11):
        print(teller, " x ", noemer,  " = ", teller * noemer )

tafelVan(getal)