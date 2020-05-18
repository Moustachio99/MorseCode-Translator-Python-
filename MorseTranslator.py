morse_en = {
    "A": ".-" ,
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
    "R": "-.-",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",

}

morse_dec = {
         ".-"   :"A",
         "-..." :"B",
         "-.-." :"C",
         "-.."  :"D",
         "."    :"E",
         "..-." :"F",
         "--."  :"G",
         "...." :"H",
         ".."   :"I",
         ".---" :"J",
         ".-."  :"K",
         ".-.." :"L",
         "--"   :"M",
         "-."   :"N",
         "---"  :"O",
         ".--." :"P",
         "--.-" :"Q",
         "-.-"  :"R",
         "..."  :"S",
         "-"    :"T",
         "..-"  :"U",
         "...-" :"V",
         ".--"  :"W",
         "-..-" :"X",
         "-.--" :"Y",
         "--.." :"Z",
         ".----":"1",
         "..---":"2",
         "...--":"3",
         "....-":"4",
         ".....":"5",
         "-....":"6",
         "--...":"7",
         "---..":"8",
         "----.":"9",
         "-----":"0",

}

def morse_encoder(string1):
    text = string1.split()
    text3 = []
    for word in text:
        text2 = []
        for letter in word:
            text2.append(morse_en[letter.upper()])
        text3.append(" ".join(text2))
    string2 = "   ".join(text3)
    print(string2)

def morse_decoder(string1):
    text = string1.split("   ")
    text3= []
    for words in text:
        text2 = words.split()
        text3.append(" ")
        for i in text2:
            text3.append(morse_dec[i])
    string2 = "".join(text3)
    print(string2)

morse_encoder("hello")









