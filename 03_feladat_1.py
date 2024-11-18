"""
1.1 Feladat
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú!
(kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
"""

megadott_mondat = input("Adj meg egy mondatot!")

if megadott_mondat[-1] == ".":
    print("Ez a mondat kijelentő.")
elif megadott_mondat[-1] == "?":
    print("Ez a mondat kérdő.")
elif megadott_mondat[-1] == "!":
    print("Ez a mondat felkiáltó/felszótító/óhajtó.")
else:
    print("Nem adtál meg mondatvégi írásjelet!")