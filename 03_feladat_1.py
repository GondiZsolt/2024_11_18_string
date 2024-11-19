"""
1.1/2 Feladat
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú!
(kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
"""
folytat = True
megadott_mondat = input("Adj meg egy mondatot!")
while folytat:
    if megadott_mondat == "":
        folytat = False
        print("program vége")
    elif megadott_mondat[-1] == ".":
        print("Ez a mondat kijelentő.")
        megadott_mondat = input("Adj meg egy mondatot!")
    elif megadott_mondat[-1] == "?":
        print("Ez a mondat kérdő.")
        megadott_mondat = input("Adj meg egy mondatot!")
    elif megadott_mondat[-1] == "!":
        print("Ez a mondat felkiáltó/felszótító/óhajtó.")
        megadott_mondat = input("Adj meg egy mondatot!")
    else:
        print("Nem adtál meg mondatvégi írásjelet!")
        megadott_mondat = input("Adj meg egy mondatot!")