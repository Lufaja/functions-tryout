def fibReeks(aantalLoops:int) -> str:
    a = 0
    b = 1
    reeks = '0, 1'
    for herhaling in range(1, aantalLoops+1):
        c = a + b
        reeks = reeks + ", " + str(c)
        a = b
        b = c
        if herhaling == aantalLoops:
            print(str(reeks))
            return "De gulde snede is dus " + str(c)



x = int(input("Welke gulde snede wilt u weten? (Heel getal): "))

print(fibReeks(x))