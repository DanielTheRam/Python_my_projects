from random import choice
def hra():
    while True:
        čísla =[1,2,3,4,5,6,7,8,9,10]
        hadej = choice(čísla)
        pokusy = 0

        while True:
            tip = int(input("Zkuste uhodnout správné číslo od 1-10: "))
            pokusy += 1
            if tip == hadej:
                print(f"""Uhodl jsi správné číslo
    počet pokusů byl {pokusy}""")
                znovu = input("Chcete hrát znovu? napište(ANO/NE): ")
                if znovu == "ANO":
                    break
                elif znovu == "NE":
                    return
                else:
                    print("Špatně zadaný výraz")
            elif tip > hadej:
                print("Vaše číslo je vyšší")
            elif tip < hadej:
                print("Vaše číslo je nižší")
