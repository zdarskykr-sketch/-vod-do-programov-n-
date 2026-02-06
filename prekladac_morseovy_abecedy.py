# převodník mezi morseovou abecedou a standartním textem
# Kryštof Žďárský, 3. ročník, GE-KA
# zimní semestr 2025/2026
# Úvod do programování

class MorsePrekladac:

    # třída umožňuje převod mezi morseovou abecedou a standartním textem a naopak.
    # Kód zpracovává soubory obsahující tex nebo morseovu abecedu a ukládá výsledek do nového souboru jehož název zadává sám uživatel.

    def __init__(self): # inicializace slovníku pro převod
        self.abeceda: dict[str, str] = {
            'A': '.-',      'B': '-...',      'C': '-.-.', 
            'D': '-..',      'E': '.',        'F': '..-.',
            'G': '--.',      'H': '....',     'I': '..', 
            'J': '.---',     'K': '-.-',      'L': '.-..', 
            'M': '--',       'N': '-.',       'O': '---', 
            'P': '.--.',     'Q': '--.-',     'R': '.-.', 
            'S': '...',      'T': '-',        'U': '..-',    
            'V': '...-',     'W': '.--',      'X': '-..-', 
            'Y': '-.--',     'Z': '--..',

            '0': '-----',    '1': '.----',    '2': '..---', 
            '3': '...--',    '4': '....-',    '5': '.....', 
            '6': '-....',    '7': '--...',    '8': '---..', 
            '9': '----.',    '.': '.-.-.-',   ',': '--..--', 
            '?': '..--..',   '!': '-.-.--',   ';': '-.-.-.', 
            ':': '---...',   ' ': '/' 
        }

        self.na_text_otoceny: dict[str, str] = {kod: znak for znak, kod in self.abeceda.items()} # obrácení slovníku pro převod z morseovy abecedy na text
    
    def na_morse(self, text: str) -> str: # pčevádí text na morseovu abecedu a neznámé znaky ignoruje
        vysledek = []
        text =text.upper()  # ochrana proti malým písmenům

        for znak in text:
            if znak in self.abeceda:
                vysledek.append(self.abeceda[znak])
            else:
                pass

        return ' '.join(vysledek)
    
    def na_text(self, m_k: str) -> str: # převádí morseovu abecedu na text a neznámé znaky ignoruje. Jednotlivé znaky musí být odděleny mezerou.
        vysledek = []
        kody =m_k.split(' ')

        for kod in kody:
            if kod in self.na_text_otoceny:
                vysledek.append(self.na_text_otoceny[kod])
            else:
                pass
        return ''.join (vysledek)
    
    def zpracuj_soubor(self, vstupni_soubor: str, vystupni_soubor: str, prevod: int): # otevře vstupní soubor, provede jeho překlad dle volby uživatele a překlad uloží do nového souboru.
        try:                                                          # Název souboru vybírá sám uživatel.
            with open(vstupni_soubor, 'r',encoding = 'utf-8') as s:
                obsah =s.read()
            if prevod == 1:
                preklad = self.na_morse(obsah)

            elif prevod ==2:
                preklad= self.na_text(obsah)
            else:
                print ("Musíš zadat 1 nebo 2.")
                return
            with open (vystupni_soubor, 'w', encoding = 'utf-8') as s:
                s.write(preklad)
            print(f"Překlad uložen do {vystupni_soubor}.")

        except FileNotFoundError:
            print (f"Soubor {vstupni_soubor} nebyl nalezen - zkus zadat celou cestu k souboru.")

        except Exception as e:
            print(f"Neočekávaná chyba: {e}")

if __name__ == "__main__": # hlavní program provádějící interakci s uživatelem.
    while True:
        prekladac = MorsePrekladac()
        print("Pro ukončení programu zadejte místo názvu souboru 'end'.") # zadály uživatel 'end' program se ukončí.
        vstupni_soubor = input("Zadejte název vstupního souboru (zadejte celou cestu k souboru): ") # uživatel zadává celou cestu k souboru.
        if vstupni_soubor.lower() == 'end':
            break

        vystupni_soubor = input("Zadejte název výstupního souboru: ") # uživatel napíše název výstupního souboru.

        try:
            prevod = int(input("Zadejte typ převodu (1. Text->Morse, 2. Morse->Text): ")) # uživatel volí směr převodu 
            prekladac.zpracuj_soubor(vstupni_soubor, vystupni_soubor, prevod)
        
        except ValueError:
            print("neplatná hodnota pro typ převodu.")