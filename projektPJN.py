print("*******************************************************")
print("\n P R O J E K T")
print("Ekstrakcja informacji z ogłoszeń o samochodach.")
print(" autor : Szymon Kwidzinski")
print("\n*******************************************************")
print("\n 1. Wczytywanie bibliotek")



print("      - import spacy")
import spacy
from spacy.matcher import Matcher

print("      - import pip")
import pip

print("      - import wget")
import wget

print("      - import numpy")
import numpy as np

print("      - import matplotlib")
import matplotlib.pyplot as plt

print("      - import csv")
import csv

print("      - import torch")
import torch
from sklearn.model_selection import train_test_split

print("      - import os")
import os

print("      - import sys")
import sys



print(" 2. Zastosowane modele do ekstrakcji informacji z ogłoszeń o samochodach")
print("    2.1 pl_core_news_sm - Polski pipeline zoptymalizowany pod kątem CPU. Brak vectorow słów")
print("    2.2 pl_core_news_md - Polski pipeline zoptymalizowany pod kątem CPU. 20tys. vectorow słów")
print("    2.3 pl_core_news_lg - Polski pipeline zoptymalizowany pod kątem CPU. 500tys. vectorow słów")
print("    Komponenty modeli: tok2vec, morphologizer, parser, lemmatizer, tagger, senter, attribute_ruler, ner")
print(" 3. Przygotowanie zbioru danych uczących model")
print(" 4. Wykorzystanie biblioteki SpaCy do konstrukcji wzorców dla każdego elementu informacji:")
print("    4.1 Rodzaj ogłoszenia")
print("    4.2 Marka samochodu")
print("    4.3 Model samochodu")
print("    4.4 Rok produkcji")
print("    4.5 Cena samochodu")
print("    4.6 Opis samochodu")
print("    4.7 Lokalizacja")
print("    4.8 Kontakt")
print(" 5. Dołaczenie wzorców do Matcher")
print(" 6. Ekstrakcja danych")
print(" 7. Podsumowanie")



def kontynuacja():
    char = " "
    while char != "n" and char != "N" and char != "t" and char != "T":
        char = input("\nKontynuować? (t,n): ")
    if char == "n" or char == "N":
        kontynuacja = False
    else:
        kontynuacja = True
    return kontynuacja


if not kontynuacja():
    print("Kończenie programu...")
    os._exit(0)

print("\n******** W Y B O R  M O D E L I  D O  E K S T R A K C J I ********\n")

print("DOSTEPNE MODELE SIECI:")
print("   1. pl_core_news_sm")
print("   2. pl_core_news_md")
print("   3. pl_core_news_lg")

char = " "
while char == " ":
  while char != "n" and char != "N" and char != "t" and char != "T":
    char = input("\nCzy wyświetlić statystyki modeli grupy Explosion? (t,n): ")
  if char == "t" or char == "T":
    from Modele import *
    Wyswietlenie_statystyk()
    Wyswietlenie_statystyk2()
    char = " "
    while char != "n" and char != "N" and char != "t" and char != "T":
        char = input("\nCzy wyświetlić miary i wzory? (t,n): ")
    if char == "t" or char == "T":
        from Miary import *
        Wyswietlenie_miar()
        char = " "

def bar_progress(current, total, width=80):
  progress_message = "Pobieranie: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
  sys.stdout.write("\r" + progress_message)
  sys.stdout.flush()

wybor = " "
while wybor != "1" and wybor != "2" and wybor != "3":
    wybor = input("\nWybierz model (1,2,3): ")
if wybor == "1":
    print("Wybrano model: pl_core_news_sm")
    if not os.path.exists("pl_core_news_sm-3.8.0-py3-none-any.whl"):
        url = 'https://github.com/explosion/spacy-models/releases/download/pl_core_news_sm-3.8.0/pl_core_news_sm-3.8.0-py3-none-any.whl'
        filename = wget.download(url,bar = bar_progress)
        print("\nPobieranie ukończone")
        pip.main(['install', 'pl_core_news_sm-3.8.0-py3-none-any.whl'])
    nlp = spacy.load('pl_core_news_sm')
    nr_model = 0

    print(nlp)

elif wybor == "2":
    print("Wybrano model: pl_core_news_md")
    if not os.path.exists("pl_core_news_md-3.8.0-py3-none-any.whl"):
        url = 'https://github.com/explosion/spacy-models/releases/download/pl_core_news_md-3.8.0/pl_core_news_md-3.8.0-py3-none-any.whl'
        filename = wget.download(url,bar = bar_progress)
        print("\nPobieranie ukończone")
        pip.main(['install', 'pl_core_news_md-3.8.0-py3-none-any.whl'])
    nlp = spacy.load("pl_core_news_md")
    nr_model = 1

    print(nlp)

else:
    print("Wybrano model: pl_core_news_lg")
    if not os.path.exists("pl_core_news_lg-3.8.0-py3-none-any.whl"):
        url = 'https://github.com/explosion/spacy-models/releases/download/pl_core_news_lg-3.8.0/pl_core_news_lg-3.8.0-py3-none-any.whl'
        filename = wget.download(url, bar = bar_progress)
        print("\nPobieranie ukończone")
        pip.main(['install', 'pl_core_news_lg-3.8.0-py3-none-any.whl'])
    nlp = spacy.load("pl_core_news_lg")
    nr_model = 2

    print(nlp)


print("\n********* P R Z Y G O T O W A N I E  D A N Y C H  U C Z Ą C Y C H **********\n")

from Ogloszenia import *

print("Usuwanie zbędnych spacji...")
print("Dopisywanie znaków interpunkcyjnych...")
for i in range(len(cars)):
    cars[i].replace("    ", " ")
    cars[i].replace("   ", " ")
    cars[i].replace("  ", " ")

print("\nLiczba ogłoszeń: ", len(cars))

char = " "
while char != "n" and char != "N" and char != "t" and char != "T":
    char = input("Czy wyświetlić ogłoszenia? (t,n): ")
    if char == "t" or char == "T":
        for i in range(len(cars)):
            doc = nlp(cars[i])
            print("#", f"{i + 1}.", doc.text, "\n")

cars_train, cars_test = train_test_split(cars, test_size=0.25)
print("Rozmiar zbioru treningowego: ", len(cars_train))

char = " "
while char != "n" and char != "N" and char != "t" and char != "T":
    char = input("Czy wyświetlić zbiór treningowy? (t,n): ")
    if char == "t" or char == "T":
        for i in range(len(cars_train)):
            doc = nlp(cars_train[i])
            print("#", f"{i + 1}.", doc.text, "\n")

print("Rozmiar zbioru testowego: ",len(cars_test))
char = " "
while char != "n" and char != "N" and char != "t" and char != "T":
    char = input("Czy wyświetlić zbiór testowy? (t,n): ")
    if char == "t" or char == "T":
        for i in range(len(cars_test)):
            doc = nlp(cars_test[i])
            print("#", f"{i + 1}.", doc.text, "\n")

print("***** W C Z Y T A N I E  P O J E D Y Ń C Z Y C H  O G Ł O S Z E Ń *****\n")

num = int(input(f"Które ogłoszenie wyświetlić? (1-{len(cars)}, 0 by anulować): "))
if num > len(cars):
    num = len(cars)
    print("NUMER POZA ZASIĘGIEM!")
    print("Wyświetlam ogłoszenie z ostatnim numerem: ", num,"\n")
elif num < 0:
    num = 0
    print("NUMER PONIŻEJ 0!")
    print("Anuluje wyświetlanie ogłoszenia...")
else:
    print("Wyświetlam ogłoszenie: ", num, "\n")

if num > 0:
    doc = nlp(cars[num-1])
    print(doc.text)
    for token in doc:
        print(token.text, token.pos_, token.shape_,token.lemma_, token.is_alpha, token.is_stop)

if not kontynuacja():
    print("Kończenie programu...")
    os._exit(0)

print("\n***** K O N S T R U K C J A  W Z O R C O W *****\n")

print("Kategorie kluczowych informacji z ogłoszeń:")
print("     -Rodzaj ogłoszenia")
print("     -Marka samochodu")
print("     -Model samochodu")
print("     -Rok produkcji")
print("     -Cena")
print("     -Lokalizacja")
print("     -Opis samochodu")
print("     -Kontakt")

patternR = [{"TEXT":{"FUZZY": {"IN":["Sprzedam","Kupię", "Szukam"]}}, "POS":"VERB", "OP":"{1}"}]

patternA = [{"TEXT":{"FUZZY": {"IN":["Sprzedam","Kupię", "Szukam", "Okazja", "Odstapie"]}}, "OP":"{1}"}, {"POS":{"IN": ["PROPN", "NOUN"]},"OP":"?"},
            {"TEXT":{"REGEX":{"IN":["[A-Za-z]*[0-9]*[-]?[0-9]*[A-Za-z]","[A-Za-z]*[0-9]+[.][0-9]+"]}},"OP":"*","ORTH":{"NOT_IN":["Model","model",",",". "]}},
            {"ORTH":{"IN":["Model","model",". ",","]}}]

patternM = [{"TEXT":{"REGEX": {"IN":["Model", "model"]}}}, {"ORTH":{"NOT_IN":[".",","]},"OP":"*"},
            {"TEXT":{"REGEX":{"IN":["[0-9]+[.][0-9]+"]}},"OP":"*"},
            {"ORTH":{"IN":[".",","]}}]

patternRokP = [{"LEMMA":{"IN": ["rok", "Rok","wyprodukować"]}, "OP":"+"},{"ORTH":{"IN": ["produkcji","w"," "]},"OP":"?"},{"ORTH":":","OP":"?"}, {"LIKE_NUM": True,"SHAPE": "dddd","OP":"{1}"}]

patternC =  [{"LOWER": {"IN":["cena", "za"]}},{"ORTH":{"IN": ["od","do",":","w"]},"OP":"?"}, {"LOWER":"przedziale","OP":"?"}, {"LIKE_NUM": True,"OP":"+"},{"ORTH":"-","OP":"?" },
             {"LIKE_NUM":True,"OP":"?"},{"ORTH":{"IN":["pln","PLN","Euro",".",","]}}]

patternL = [{"LOWER": {"IN":["w","miejscowość"]}},{"POS":"ADJ","LIKE_NUM": False, "OP":"?"},{"POS":{"IN":[ "PROPN", "NOUN"]}}, {"POS": "ADJ","LIKE_NUM": False,"OP":"?"},{"ORTH":{"IN":[".",","]}} ]

patternP = [{"TEXT": {"REGEX":{"IN": ["Parametry", "Opis"]}}},{"TEXT": {"REGEX": "[0-9]*[,:;]?[A-Za-z]*"}, "OP":"+","ORTH":{"NOT_IN":["."]}}, {"ORTH":"."}]

patternK = [
           [{"LOWER":{"IN": ["email","mail","e-mail"]}, "OP":"?"},{"LIKE_EMAIL": True}],
           [{"LOWER":{"IN": ["kontakt","telefon","tel"]}},{"ORTH":".","OP":"?"},{"LIKE_NUM": True,"OP":"+"},{"ORTH":"-","OP":"?"},{"LIKE_NUM": True,"OP":"?"}]
           ]

if not kontynuacja():
    print("Kończenie programu...")
    os._exit(0)

print("\n********* D O D A N I E  W Z O R C O W  D O  M A T C H E R **********\n")
print("Dodawanie wzorców do Matchera")
matcher = Matcher(nlp.vocab)
print("   Rodzaj - patternR")
matcher.add("Rodzaj:", [patternR])
print("   Auto - patternA")
matcher.add("Auto:", [patternA])
print("   Model - patternM")
matcher.add("Model:", [patternM])
print("   Rok produkcji - patternRokP")
matcher.add("Rok produkcji:", [patternRokP])
print("   Cena - patternC")
matcher.add("Cena:", [patternC])
print("   Lokalizacja - patternL")
matcher.add("Lokalizacja:",[patternL])
print("   Opis - patternP")
matcher.add("Opis:", [patternP])
print("   Kontakt - patternK")
matcher.add("Kontakt:", patternK)
print("Ukończono dodawanie")

if not kontynuacja():
    print("Kończenie programu...")
    os._exit(0)

print("\n********* E K S T R A K C J A  I N F O R M A C J I **********\n")

test = 0
while test < 2:
  wynik = [0,0,0,0,0,0,0,0]
  if test == 0:
    data = cars_train
  else:
    data = cars_test

  for i in range(len(data)):
    doc = nlp(data[i])
    print("#", f"{i + 1}.", doc.text, "\n")
    matches = matcher(doc)
    for match_id, start, end in matches:

        if doc.vocab.strings[match_id] == "Rodzaj:":
            if len(doc[start:end]) > 0:
                print(doc.vocab.strings[match_id], doc[start:end])
                wynik[0] = wynik[0] + 1
        if doc.vocab.strings[match_id] == "Auto:":
            if (doc[start + 1].text == "auto" or doc[start + 1].text == "samochód"):
                start = start + 1
            if len(doc[start:end]) > 1:
                if doc[start + 1].text != doc[start + 1].lemma_:
                    print(doc.vocab.strings[match_id], doc[start + 1:end - 1].lemma_.capitalize())
                else:
                    print(doc.vocab.strings[match_id], doc[start + 1:end - 1])
                wynik[1] = wynik[1] + 1
        if doc.vocab.strings[match_id] == "Model:":
            if len(doc[start:end]) > 0:
                print(doc.vocab.strings[match_id], doc[start + 1:end - 1])
                wynik[2] = wynik[2] + 1
        if doc.vocab.strings[match_id] == "Rok produkcji:":
            if len(doc[start:end]) > 2:
                print(doc.vocab.strings[match_id], doc[end - 1:end])
                wynik[3] = wynik[3] + 1
        if doc.vocab.strings[match_id] == "Cena:":
            if (doc[start + 1].text == ":" or doc[start + 1].text == " "):
                start = start + 1
            if doc[end - 1].text == ".":
                end = end - 1
            print(doc.vocab.strings[match_id], doc[start + 1:end])
            wynik[4] = wynik[4] + 1
        if doc.vocab.strings[match_id] == "Opis:":
            if len(doc[start + 2:end]) > 0:
                print(doc.vocab.strings[match_id], doc[start + 2:end])
                wynik[5] = wynik[5] + 1
        if doc.vocab.strings[match_id] == "Lokalizacja:":
            if len(doc[start + 1:end - 1]) > 0:
                print(doc.vocab.strings[match_id], doc[start + 1:end - 1].lemma_)
                wynik[6] = wynik[6] + 1
        if doc.vocab.strings[match_id] == "Kontakt:":
            if (doc[start].text == "kontakt" or doc[start].text == "Kontakt"):
                start = start + 1
            if len(doc[start:end]) > 0:
                print(doc.vocab.strings[match_id], doc[start:end])
                wynik[7] = wynik[7] + 1
    print("\n")
  test += 1
prec = [0,0,0,0,0,0,0,0]
acc = [0,0,0,0,0,0,0,0]
spec = [0,0,0,0,0,0,0,0]

with open('wyniki.csv','a',encoding='utf-8',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    file_size = os.path.getsize('wyniki.csv')
    if file_size == 0:
        csvwriter.writerow(['acc','prec','spec','acc','prec','spec','acc','prec','spec'])
        for row in range(len(matcher)):
            csvwriter.writerow([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

w_kat_sm = np.zeros(shape=(len(matcher),3))
w_kat_md = np.zeros(shape=(len(matcher),3))
w_kat_lg = np.zeros(shape=(len(matcher),3))

with open('wyniki.csv','r',encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    i = 0
    for row in csvreader:
        if i > 0:
            w_kat_sm[i-1][0] = row[0]
            w_kat_sm[i-1][1] = row[1]
            w_kat_sm[i-1][2] = row[2]
            w_kat_md[i-1][0] = row[3]
            w_kat_md[i-1][1] = row[4]
            w_kat_md[i-1][2] = row[5]
            w_kat_lg[i-1][0] = row[6]
            w_kat_lg[i-1][1] = row[7]
            w_kat_lg[i-1][2] = row[8]
        i = i+1

for i in range(len(matcher)):
    prec[i] = 100*wynik[i]/len(cars_test)
    suma = wynik[0]+wynik[1]+wynik[2]+wynik[3]+wynik[4]+wynik[5]+wynik[6]+wynik[7]
    acc[i] = 100*suma/(len(cars_test)*len(matcher))
    spec[i] = 100 * (suma-wynik[i]) / (len(cars_test) * len(matcher)-1)
    if nr_model == 0:
        w_kat_sm[i][0] = acc[i]
        w_kat_sm[i][1] = prec[i]
        w_kat_sm[i][2] = spec[i]
    elif nr_model == 1:
        w_kat_md[i][0] = acc[i]
        w_kat_md[i][1] = prec[i]
        w_kat_md[i][2] = spec[i]
    else:
        w_kat_lg[i][0] = acc[i]
        w_kat_lg[i][1] = prec[i]
        w_kat_lg[i][2] = spec[i]

with open('wyniki.csv','w',encoding='utf-8',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['acc','prec','spec','acc','prec','spec','acc','prec','spec'])
    for row in range(len(matcher)):
        csvwriter.writerow([w_kat_sm[row][0],w_kat_sm[row][1],w_kat_sm[row][2],w_kat_md[row][0],w_kat_md[row][1],w_kat_md[row][2],w_kat_lg[row][0],w_kat_lg[row][1],w_kat_lg[row][2]])

models = ["pl_core_news_sm",  "pl_core_news_md", "pl_core_news_lg"]
wynikiTa = [" ACCURACY ",  "PRECISION ", "SPECIFICITY"]
wynikiT  = ["DOKŁADNOŚĆ",  " PRECYZJA ", "SWOISTOŚĆ "]
print("                                                 Wyniki ostatnich testów modeli          ")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"|      MODEL      |           {models[0]}           ||           {models[1]}           ||           {models[2]}            |")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"|    KATEGORIA    | {wynikiT[0]} | {wynikiT[1]} | {wynikiT[2]}|| {wynikiT[0]} | {wynikiT[1]} | {wynikiT[2]}|| {wynikiT[0]} | {wynikiT[1]} | {wynikiT[2]} |")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"|Rodzaj ogłoszenia|   {w_kat_sm[0][0]: >6.2f}   |   {w_kat_sm[0][1]: >6.2f}   |   {w_kat_sm[0][2]: >6.2f}  ||   {w_kat_md[0][0]: >6.2f}   |   {w_kat_md[0][1]: >6.2f}   |   {w_kat_md[0][2]: >6.2f}  ||   {w_kat_lg[0][0]: >6.2f}   |   {w_kat_lg[0][1]: >6.2f}   |   {w_kat_lg[0][2]: >6.2f}   |")
print(f"| Marka samochodu |   {w_kat_sm[1][0]: >6.2f}   |   {w_kat_sm[1][1]: >6.2f}   |   {w_kat_sm[1][2]: >6.2f}  ||   {w_kat_md[1][0]: >6.2f}   |   {w_kat_md[1][1]: >6.2f}   |   {w_kat_md[1][2]: >6.2f}  ||   {w_kat_lg[1][0]: >6.2f}   |   {w_kat_lg[1][1]: >6.2f}   |   {w_kat_lg[1][2]: >6.2f}   |")
print(f"| Model samochodu |   {w_kat_sm[2][0]: >6.2f}   |   {w_kat_sm[2][1]: >6.2f}   |   {w_kat_sm[2][2]: >6.2f}  ||   {w_kat_md[2][0]: >6.2f}   |   {w_kat_md[2][1]: >6.2f}   |   {w_kat_md[2][2]: >6.2f}  ||   {w_kat_lg[2][0]: >6.2f}   |   {w_kat_lg[2][1]: >6.2f}   |   {w_kat_lg[2][2]: >6.2f}   |")
print(f"|  Rok produkcji  |   {w_kat_sm[3][0]: >6.2f}   |   {w_kat_sm[3][1]: >6.2f}   |   {w_kat_sm[3][2]: >6.2f}  ||   {w_kat_md[3][0]: >6.2f}   |   {w_kat_md[3][1]: >6.2f}   |   {w_kat_md[3][2]: >6.2f}  ||   {w_kat_lg[3][0]: >6.2f}   |   {w_kat_lg[3][1]: >6.2f}   |   {w_kat_lg[3][2]: >6.2f}   |")
print(f"|      Cena       |   {w_kat_sm[4][0]: >6.2f}   |   {w_kat_sm[4][1]: >6.2f}   |   {w_kat_sm[4][2]: >6.2f}  ||   {w_kat_md[4][0]: >6.2f}   |   {w_kat_md[4][1]: >6.2f}   |   {w_kat_md[4][2]: >6.2f}  ||   {w_kat_lg[4][0]: >6.2f}   |   {w_kat_lg[4][1]: >6.2f}   |   {w_kat_lg[4][2]: >6.2f}   |")
print(f"|      Opis       |   {w_kat_sm[5][0]: >6.2f}   |   {w_kat_sm[5][1]: >6.2f}   |   {w_kat_sm[5][2]: >6.2f}  ||   {w_kat_md[5][0]: >6.2f}   |   {w_kat_md[5][1]: >6.2f}   |   {w_kat_md[5][2]: >6.2f}  ||   {w_kat_lg[5][0]: >6.2f}   |   {w_kat_lg[5][1]: >6.2f}   |   {w_kat_lg[5][2]: >6.2f}   |")
print(f"|   Lokalizacja   |   {w_kat_sm[6][0]: >6.2f}   |   {w_kat_sm[6][1]: >6.2f}   |   {w_kat_sm[6][2]: >6.2f}  ||   {w_kat_md[6][0]: >6.2f}   |   {w_kat_md[6][1]: >6.2f}   |   {w_kat_md[6][2]: >6.2f}  ||   {w_kat_lg[6][0]: >6.2f}   |   {w_kat_lg[6][1]: >6.2f}   |   {w_kat_lg[6][2]: >6.2f}   |")
print(f"|     Kontakt     |   {w_kat_sm[7][0]: >6.2f}   |   {w_kat_sm[7][1]: >6.2f}   |   {w_kat_sm[7][2]: >6.2f}  ||   {w_kat_md[7][0]: >6.2f}   |   {w_kat_md[7][1]: >6.2f}   |   {w_kat_md[7][2]: >6.2f}  ||   {w_kat_lg[7][0]: >6.2f}   |   {w_kat_lg[7][1]: >6.2f}   |   {w_kat_lg[7][2]: >6.2f}   |")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print("*wyniki podane w %")
print(" ")


char = " "
while char == " ":
  while char != "n" and char != "N" and char != "t" and char != "T":
    char = input("Czy wyświetlić wykresy ostatnich wyników (zastaną one zapisane w folderze 'wykresy')? (t,n): ")
  if char == "t" or char == "T":
    if not os.path.exists("wykresy"):
        os.makedirs("wykresy")
    w_kat_sm2 = [w_kat_sm[0][2],w_kat_sm[1][2],w_kat_sm[2][2],w_kat_sm[3][2],w_kat_sm[4][2],w_kat_sm[5][2],w_kat_sm[6][2],w_kat_sm[7][2]]
    w_kat_md2 = [w_kat_md[0][2],w_kat_md[1][2],w_kat_md[2][2],w_kat_md[3][2],w_kat_md[4][2],w_kat_md[5][2],w_kat_md[6][2],w_kat_md[7][2]]
    w_kat_lg2 = [w_kat_lg[0][2],w_kat_lg[1][2],w_kat_lg[2][2],w_kat_lg[3][2],w_kat_lg[4][2],w_kat_lg[5][2],w_kat_lg[6][2],w_kat_lg[7][2]]
    barWidth = 0.2
    fig = plt.figure(figsize =(15, 6))
    br2 = [1, 2, 3, 4, 5, 6, 7, 8]
    br1 = [x - barWidth for x in br2]
    br3 = [x + barWidth for x in br2]
    wyniki = ["RODZAJ",  "MARKA", "MODEL", "ROK PR", "CENA", "OPIS", "LOKALIZACJA", "KONTAKT"]
    plt.bar(br1, w_kat_sm2, color = 'red', width = 0.1)
    plt.bar(br2, w_kat_md2, color = 'blue', width = 0.1)
    plt.bar(br3, w_kat_lg2, color = 'orange', width = 0.1)
    plt.xlabel(f"{wyniki[0]}                 {wyniki[1]}                  {wyniki[2]}                   {wyniki[3]}                   {wyniki[4]}                     {wyniki[5]}                 {wyniki[6]}             {wyniki[7]}",
                fontsize = 10, color = 'blue')

    plt.ylabel('procent', fontsize = 14)
    plt.title('SPECIFICITY - wyniki dla modeli pl_core_news_*',fontsize = 16) #, fontweight ='bold')
    plt.xlim([0,9])
    plt.ylim([0,100])
    plt.legend(('sm', 'md','lg'), loc = 'upper left')
    plt.savefig('./wykresy/specificity.png')
    plt.show( )



    w_kat_sm1 = [w_kat_sm[0][1],w_kat_sm[1][1],w_kat_sm[2][1],w_kat_sm[3][1],w_kat_sm[4][1],w_kat_sm[5][1],w_kat_sm[6][1],w_kat_sm[7][1]]
    w_kat_md1 = [w_kat_md[0][1],w_kat_md[1][1],w_kat_md[2][1],w_kat_md[3][1],w_kat_md[4][1],w_kat_md[5][1],w_kat_md[6][1],w_kat_md[7][1]]
    w_kat_lg1 = [w_kat_lg[0][1],w_kat_lg[1][1],w_kat_lg[2][1],w_kat_lg[3][1],w_kat_lg[4][1],w_kat_lg[5][1],w_kat_lg[6][1],w_kat_lg[7][1]]
    barWidth = 0.2
    fig = plt.figure(figsize =(15, 6))
    br2 = [1, 2, 3, 4, 5, 6, 7, 8]
    br1 = [x - barWidth for x in br2]
    br3 = [x + barWidth for x in br2]
    wyniki = ["RODZAJ",  "MARKA", "MODEL", "ROK PR", "CENA", "OPIS", "LOKALIZACJA", "KONTAKT"]
    plt.bar(br1, w_kat_sm1, color = 'red', width = 0.1)
    plt.bar(br2, w_kat_md1, color = 'blue', width = 0.1)
    plt.bar(br3, w_kat_lg1, color = 'orange', width = 0.1)
    plt.xlabel(f"{wyniki[0]}                 {wyniki[1]}                  {wyniki[2]}                   {wyniki[3]}                   {wyniki[4]}                     {wyniki[5]}                 {wyniki[6]}             {wyniki[7]}",
                fontsize = 10, color = 'blue')

    plt.ylabel('procent', fontsize = 14)
    plt.title(' PRECISION - wyniki dla modeli pl_core_news_*',fontsize = 16) #, fontweight ='bold')
    plt.xlim([0,9])
    plt.ylim([0,100])
    plt.legend(('sm', 'md','lg'), loc = 'upper left')
    plt.savefig('./wykresy/precision.png')
    plt.show( )


    w_kat_sm0 = [w_kat_sm[0][0],w_kat_sm[1][0],w_kat_sm[2][0],w_kat_sm[3][0],w_kat_sm[4][0],w_kat_sm[5][0],w_kat_sm[6][0],w_kat_sm[7][0]]
    w_kat_md0 = [w_kat_md[0][0],w_kat_md[1][0],w_kat_md[2][0],w_kat_md[3][0],w_kat_md[4][0],w_kat_md[5][0],w_kat_md[6][0],w_kat_md[7][0]]
    w_kat_lg0 = [w_kat_lg[0][0],w_kat_lg[1][0],w_kat_lg[2][0],w_kat_lg[3][0],w_kat_lg[4][0],w_kat_lg[5][0],w_kat_lg[6][0],w_kat_lg[7][0]]
    barWidth = 0.2
    fig = plt.figure(figsize =(15, 6))
    br2 = [1, 2, 3, 4, 5, 6, 7, 8]
    br1 = [x - barWidth for x in br2]
    br3 = [x + barWidth for x in br2]
    wyniki = ["RODZAJ",  "MARKA", "MODEL", "ROK PR", "CENA", "OPIS", "LOKALIZACJA", "KONTAKT"]
    plt.bar(br1, w_kat_sm0, color = 'red', width = 0.1)
    plt.bar(br2, w_kat_md0, color = 'blue', width = 0.1)
    plt.bar(br3, w_kat_lg0, color = 'orange', width = 0.1)
    plt.xlabel(f"{wyniki[0]}                 {wyniki[1]}                  {wyniki[2]}                   {wyniki[3]}                   {wyniki[4]}                     {wyniki[5]}                 {wyniki[6]}             {wyniki[7]}",
                fontsize = 10, color = 'blue')

    plt.ylabel('procent', fontsize = 14)
    plt.title('  ACCURACY  - wyniki dla modeli pl_core_news_*',fontsize = 16) #, fontweight ='bold')
    plt.xlim([0,9])
    plt.ylim([0,100])
    plt.legend(('sm', 'md','lg'), loc = 'upper left')
    plt.savefig('./wykresy/accuracy.png')
    plt.show( )


print("\n******************** KONIEC ********************\n")
