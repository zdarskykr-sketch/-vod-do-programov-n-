# převodník mezi morseovou abecedou a standartním textem
# Kryštof Žďárský, 3. ročník, GE-KA
# zimní semestr 2025/2026
# Úvod do programování

class MorseTranslator:

    # class for translation between morse code and standart text.
    # the input for the code is a string file and output is also a string file.
    def __init__(self): # initialization of the dictionary for translation.
        self.dictionary: dict[str, str] = {
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

        self.to_reverse_text: dict[str, str] = {code: char for char, code in self.dictionary.items()} # reverse dictionary for reverse translation.
    
    def to_morse(self, text: str) -> str: # translates text to morse code and ignores unknown charakters.
        result = []
        text =text.upper()  # it transforms the text to uppercase to match the keys in the dictionary.

        for char in text:
            if char in self.dictionary:
                result.append(self.dictionary[char])
            else:
                pass

        return ' '.join(result)
    
    def to_text(self, m_k: str) -> str: # it transforms morse code to text and ignores unknown charakters.
        result = []
        codes =m_k.split(' ')

        for code in codes:
            if code in self.to_reverse_text:
                result.append(self.to_reverse_text[code])
            else:
                pass
        return ''.join (result)
    
    def process_file(self, input_file: str, output_file: str, mode: int): # open the file, read the content, translate it and save the result to the output file. It also handles exceptions for file not found and other unexpected errors.
        try:                                                          # the name of the output file is given by user.
            with open(input_file, 'r',encoding = 'utf-8') as s:
                content =s.read()
            if mode == 1:
                translate = self.to_morse(content)

            elif mode ==2:
                translate = self.to_text(content)
            else:
                print ("You have to enter 1 or 2.")
                return
            with open (output_file, 'w', encoding = 'utf-8') as s:
                s.write(translate)
            print(f"Translation saved to {output_file}.")

        except FileNotFoundError:
            print (f"File {input_file} not found - try entering the full path to the file.")

        except Exception as e:
            print(f"Neočekávaná chyba: {e}")

if __name__ == "__main__": # main program loop to get user input for file names and type of translation.
    while True:
        translator = MorseTranslator()
        print("To end the program enter 'end' instead of a file name.") # if the user writes 'end' the program will end.
        input_file = input("Enter full path to input file: ") # user inputs the the whole path to the input file.
        if input_file.lower() == 'end':
            break

        output_file = input("Enter name of output file: ") # user inputs the name of output file.

        try:
            mode = int(input("Enter translation type (1. Text->Morse, 2. Morse->Text): ")) # user chooses the type of translation.
            translator.process_file(input_file, output_file, mode)
        
        except ValueError:
            print("Invalid value for translation type.")