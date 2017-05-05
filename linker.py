#!python3
from random import *
import fileinput


def ask():
    answer = input("Опции: Добави, изтрий, подай. \n  | Добави - добавяне на запис. \n  | Подай  - подаване на неподаван запис. \n  | Изход  - за излизане от скрипта. \nИзбор: ")
    answer = answer.lower()
    if answer == "добави":
        addlink()
    elif answer == "подай":
        givelink()
    elif answer == "изход":
        print("\nЛек ден!\n\n- - - - - - - - - - - - - - - - - - - - - -\n")
        quit()
    else:
        print("\nМоля изберете от позволените опции. \n |!|Забележка: Програмата не толерира правописни грешки и писане на български с латинската азбука.")
        ask()

#Adding a link
def addlink():
    print("\nПодсказка: Можете по всяко едно време да се върнете назад като напишете \"Назад\".")
    link = input("Моля, подайте вашия линк: ")
    if link[0:4] == "http":
        try:
            readfile = open('links.txt','r').readlines()
            same = 0
            for line in readfile:
                if line == (link + " 1") or line == (link + " 0") or line == (link + " 1\n") or line == (link + " 0\n"):
                    same = same + 1

            if same >= 1:
                print("Този линк вече присъства.")
                addlink()
            elif same == 0:
                appendfile = open('links.txt','a')
                append = "\n" + link + " 1"
                appendfile.write(append)
                appendfile.close()
                print("Добавено.")
                addlink()
        except FileNotFoundError:
            writefile = open('links.txt','w')
            write = link + " 1"
            writefile.write(write)
            writefile.close()
            addlink()

    elif link == "назад" or link == "Назад":
        ask()
    else:
        print("\nФормата на вашия линк е неточен. Трябва да започва с http://")
        addlink()

def givelink():
    readfile = open('links.txt', 'r').readlines()
    length = len(readfile)
    index = randint(0,length)
    item = readfile[index]
    lastchar = item[-1:]
    if item[-1:] == "1":
        print("Вашия линк: ", item[:-1])
        #appendChange = open('links.txt', 'a')
        #appendChange.write(readfile[index] - item[-1:] + "0")
        itemToReplace = item[:-1] + "0"
        with fileinput.FileInput('links.txt', inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(item, itemToReplace), end='')

                #Тук нещо гърми...

print("\n- - - - - - - - - - - - - - - - - - - - - -\n               Linker v0.1\n- - - - - - - - - - - - - - - - - - - - - -\n")
ask()
