# vizualiyace kochovy pomocí turtle grafiky
# Kryštof Žďárský, 3. ročník, GE-KA
# zimní semestr 2025/2026
# Úvod do programování

import turtle
class KochVlocka:
    def __init__(self, zelva_objekt, delka_strany, stupen): # funkce pro kontrolu stupně rekurze a inicializaci proměnných
        self.t = zelva_objekt
        self.delka_strany = delka_strany
        
        if stupen > 5: # kontrola platnosti vstupu stupně rekurtze
            print("Hodnota byla snížena na 5")
            self.stupen = 5
        elif stupen < 0:
            print("Hodnota nemůže být menší než 0, nastavena na 0")
            self.stupen = 0
        else:
            self.stupen = stupen

    def konch_posloupnost(self, delka, moment_stupen): # rekurzivní funkce kochovy posloupnosti, která vykreaslí jednu stranu vločky
        if moment_stupen == 0:
            self.t.forward(delka)
        else:
            nova_delka = delka / 3
            self.konch_posloupnost(nova_delka, moment_stupen - 1)
            self.t.left(60)
            self.konch_posloupnost(nova_delka, moment_stupen - 1)
            self.t.right(120)
            self.konch_posloupnost(nova_delka, moment_stupen - 1)
            self.t.left(60)
            self.konch_posloupnost(nova_delka, moment_stupen - 1)
    
    def vlocka(self): # tato funkce pouze opakuje kochovu posloupnost třikrát, aby se uzavřela vločka
        self.t.penup()
        self.t.goto(-self.delka_strany / 2, self.delka_strany / 3) # vycentrování vločky naobrazovce
        self.t.pendown()

        for _ in range(3):
            self.konch_posloupnost(self.delka_strany, self.stupen)
            self.t.right(120)

if __name__ == "__main__": # hlavní program provádějící interakci s uživatelem

    delka_strany = int(input("Zadejte délku strany vločky: "))  # uživatelský vstup pro délky strany
    stupen = int(input("Zadejte stupeň vločky (1-5): "))        # uživatel si zvolí stupeň rekurze
    rychlost = int(input("Zadejte rychlost kreslení (1-11): ")) # uživatel má volbu si zvolit rychlost kreslení želvy
    screen = turtle.Screen()
    t = turtle.Turtle()
    screen.title("Kochova vločka")
    t.speed(rychlost)

    moje_vlocka = KochVlocka(t, delka_strany, stupen)
    moje_vlocka.vlocka()
    screen.exitonclick()