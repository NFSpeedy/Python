#! python3
from time import sleep

#printProgressBar is a free solution from Stackoverflow. Credit goes to Greenstick. Thank you.
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + ' ' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

text = input("Your text in Cyrillic: ")
char=0
OtherChar=0
text = text.lower()
LatText=""
UnknownChars=[]
UnknownCharsStr=""
while True:
    Cyrillic = [" ", "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ѝ", "ь", "ю", "я", ".", ",", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-", "_", "%", "+", "=", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "$"]
    ToBe = ["-", "a", "b", "v", "g", "d", "e", "j", "z", "i", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "c", "ch", "sh", "sht", "y", "x", "x", "iu", "q", "-", "-", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-", "_", "%", "+", "=", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "$"]
    if (len(text)-1) >= char:
        testing=""
        if OtherChar > 74:
            if len(UnknownChars) == 0:
                UnknownChars.append(text[char])
                char+=1
                OtherChar = 0
            else:
                testing = text[char]
                print(testing)
                for item in UnknownChars:
                    if item != testing:
                        UnknownChars.append(testing)
                        char+=1
                        OtherChar = 0
                    else:
                        char+=1
                        OtherChar = 0
        elif text[char] == Cyrillic[OtherChar] and OtherChar <= len(Cyrillic):
            LatText += ToBe[OtherChar]
            char+=1
            OtherChar = 0
        else:
            OtherChar+=1
    else:
        break
    printProgressBar(char, len(text), prefix="Progress: ", suffix="done.", length=20)
print(LatText)
if len(UnknownChars) > 0:
    for MissingSymbol in UnknownChars:
        print(MissingSymbol)
        if len(UnknownCharsStr) == 0:
            UnknownCharsStr = UnknownCharsStr + MissingSymbol
        else:
            UnknownCharsStr = UnknownCharsStr + ", " + MissingSymbol
    print("!!!NOTICE!!!: There are some unknown symbols: " + UnknownCharsStr + "\nYou can edit the source code and add them or contact the author at atanas.stoev3@gmail.com. You can fork the source code from https://github.com/NFSpeedy/Python. The add-n is called Latinizator 2.")
