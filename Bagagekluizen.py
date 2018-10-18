import re

input2 = eval(input('1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \nEnter optie:'))


def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    text = infile.read()
    infile.close()
    aantal = text.split('\n')
    return 12-len(aantal)


def nieuwe_kluis():
    infile2 = open('kluizen.txt', 'r')
    text2 = infile2.read()
    infile2.close()
    aantal2 = re.split('\n|;', text2)
    list_ints = []
    for i in range(0, 12 - (toon_aantal_kluizen_vrij())):
        list_ints.append(aantal2[2 * i])
    list_ints = [int(i) for i in list_ints]
    list_all = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for j in list_ints:
        if j in list_all:
            list_all.remove(j)
    number = list_all[0]
    if number == 13:
        print('Alle kluizen zijn bezet')
    else:
        print('Jij hebt kluis', number)
        code = input('Wat wil je als code?')
        appendfile = open('kluizen.txt', 'a')
        appendfile.write('\n')
        appendfile.write(str(number))
        appendfile.write(';')
        appendfile.write(code)
        appendfile.close()


def kluis_openen(kluis, code2):
    infile3 = open('kluizen.txt', 'r')
    text3 = infile3.read()
    infile3.close()
    aantal3 = re.split('\n|;', text3)

    for i in range(0, 12 - (toon_aantal_kluizen_vrij())):
        a = 2 * i
        b = 2 * i + 1
        if kluis == aantal3[a] and code2 == aantal3[b]:
            print('Correcte combinatie!')
            break
        else:
            pass
        print('Dat klopt niet')


if input2 == 1:
    print(toon_aantal_kluizen_vrij(), 'kluizen zijn er nog vrij')
if input2 == 2:
    nieuwe_kluis()
if input2 == 3:
    kluis = input('Wat is je kluisnummer?')
    code2 = input('Wat is je code?')
    kluis_openen(kluis, code2)
else:
    print('Dat is geen optie')
