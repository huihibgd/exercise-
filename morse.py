morse_code_dict={"A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",}

def morse_translator():
    original_text=input("Enter your text:  ")
    text=original_text.upper()
    results=[]
    for character in text:
        if character in morse_code_dict:
         x=morse_code_dict[character]
         results.append(x)
        elif character==" ":
         x="/"
         results.append(x)  
    results_string=" ".join(results)
    print(results_string)

morse_translator()
    

