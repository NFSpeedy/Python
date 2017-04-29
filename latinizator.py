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
text = text.lower()
LatText=""
while True:
    if (len(text)-1) >= char:
        if text[char] == "а":
            LatText = LatText + "a"
            char+=1
        elif text[char] == "б":
            LatText = LatText + "b"
            char+=1
        elif text[char] == "в":
            LatText = LatText + "v"
            char+=1
        elif text[char] == "г":
            LatText = LatText + "g"
            char+=1
        elif text[char] == "д":
            LatText = LatText + "d"
            char+=1
        elif text[char] == "е":
            LatText = LatText + "e"
            char+=1
        elif text[char] == "ж":
            LatText = LatText + "j"
            char+=1
        elif text[char] == "з":
            LatText = LatText + "z"
            char+=1
        elif text[char] == "и":
            LatText = LatText + "i"
            char+=1
        elif text[char] == "й":
            LatText = LatText + "i"
            char+=1
        elif text[char] == "к":
            LatText = LatText + "k"
            char+=1
        elif text[char] == "л":
            LatText = LatText + "l"
            char+=1
        elif text[char] == "м":
            LatText = LatText + "m"
            char+=1
        elif text[char] == "н":
            LatText = LatText + "n"
            char+=1
        elif text[char] == "о":
            LatText = LatText + "o"
            char+=1
        elif text[char] == "п":
            LatText = LatText + "p"
            char+=1
        elif text[char] == "р":
            LatText = LatText + "r"
            char+=1
        elif text[char] == "с":
            LatText = LatText + "s"
            char+=1
        elif text[char] == "т":
            LatText = LatText + "t"
            char+=1
        elif text[char] == "у":
            LatText = LatText + "u"
            char+=1
        elif text[char] == "ф":
            LatText = LatText + "f"
            char+=1
        elif text[char] == "х":
            LatText = LatText + "h"
            char+=1
        elif text[char] == "ц":
            LatText = LatText + "c"
            char+=1
        elif text[char] == "ч":
            LatText = LatText + "ch"
            char+=1
        elif text[char] == "ш":
            LatText = LatText + "sh"
            char+=1
        elif text[char] == "щ":
            LatText = LatText + "sht"
            char+=1
        elif text[char] == "ъ":
            LatText = LatText + "y"
            char+=1
        elif text[char] == "ь":
            LatText = LatText + "x"
            char+=1
        elif text[char] == "ю":
            LatText = LatText + "iu"
            char+=1
        elif text[char] == "я":
            LatText = LatText + "q"
            char+=1
        elif text[char] == "ѝ":
            LatText = LatText + "i"
            char+=1
        elif text[char] == " ":
            LatText = LatText + "-"
            char+=1
        elif text[char] == "\"":
            char+=1
        elif text[char] == ",":
            char+=1
        elif text[char] == ".":
            char+=1
        elif text[char] == ":":
            char+=1
        elif text[char] == ";":
            char+=1
        else:
            print("Unnown char.")
            break
    else:
        break
    printProgressBar(char, len(text), prefix="Progress: ", suffix="done.", length=20)
print(LatText)
