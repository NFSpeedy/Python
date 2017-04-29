#! python3

text = input("АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъѝьЮюЯя: ")
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
        else:
            print("Unknown char.")
            break
    else:
        break
print(LatText)
