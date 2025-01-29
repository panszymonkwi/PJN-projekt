cars = [
     """Sprzedam auto Opel model Mokka Cosmo 1_6 CDTI, rok produkcji 2016, cena 44000 PLN.  Opis: paliwo Diesel, przebieg 148340, skrzynia biegów manualna, typ nadwozia SUV, pojemność 1548cm3, moc 136kM, kolor Czarny. Miejscowość Kielce, kontakt tel. 664477900 .""",

     """Sprzedam Lexus ES 300h Business Edition, wyprodukowany w 2020 roku, cena od 162300 PLN.  Parametry: paliwo Hybryda, przebieg 98600, skrzynia biegów Automat, typ nadwozia Sedan, pojemność 2487cm3, moc 178kM, Kolor Biały. Kontakt tel. 608346322, miejscowość Błonie.""",

     """Kupię Mercedesa Model Klasa E 2_2, rok produkcji 1994, cena 20000-22220 PLN.  Opis: paliwo Benzyna, przebieg 344200, skrzynia biegów manualna, typ nadwozia Kombi, pojemność 2199, moc 150kM, kolor Szary metalik.  Kontakt tel.727930795   Miejscowość Białystok.""",

     """Sprzedam Audi Model A3 1_4 TFSI Edycja Specjalna,  rok produkcji 2014,  za 59000 PLN. Parametry: paliwo Benzyna, przebieg 130739, Skrzynia biegów  Manualna, typ nadwozia Kompakt, pojemność 1393cm3, moc 125kM, kolor Srebrny.  Kontakt xxx@gmail.com,  miejscowość Radom.""",

     """Szukam Mazdy model CX-5 2_5 Skypassion AWD. Rok produkcji 2017.  Cena 85900 PLN. Opis: Paliwo Benzyna  Przebieg 199000   Skrzynia biegów  Automatyczna  Typ nadwozia SUV  Pojemność  2488cm3   Moc 195kM  Kolor  Czarny.  Kontakt tel. 601406593   Miejscowość Warszawa.""",

     """Sprzedam Chrysler Pacifica, rok produkcji 2018.  Cena: 109900 PLN. Opis Paliwo Hybryda  Przebieg 127780   Skrzynia biegów  Automatyczna Typ nadwozia MiniVan  Pojemność  3605cm3   Moc 264kM  Kolor  Niebieski.  Kontakt tel. 698622866.  Miejscowość Łapy.""",

     """Sprzedam Volvo Model XC90. Rok produkcji 2008, cena 31500 PLN. Parametry: Paliwo Benzyna  Przebieg 350000   Skrzynia biegów  Automatyczna Typ nadwozia SUV  Pojemność  4414cm3   Moc 315kM  Kolor  Szary. Kontakt tel. 500176527.  Miejscowość Gdynia.""",

     """Sprzedam Porsche Model Cayenne, rok produkcji 2012, cena 71900 PLN. Opis: Paliwo Benzyna  Przebieg 364000   Skrzynia biegów  Automatyczna Typ nadwozia SUV  Pojemność  3598cm3   Moc 300kM  Kolor  Czarny.  Kontakt tel. 578902658.   Miejscowość Kielce.""",

     """Sprzedam Toyota model Corolla 1.8. Rok produkcji 2021.  Cena 87945 PLN. Parametry: Paliwo Hybryda  Przebieg 90000   Skrzynia biegów  Automatyczna Typ nadwozia Kombi  Pojemność  1798cm3   Moc 98kM  Kolor  Biały.  Kontakt tel.784669099.   Miejscowość Chorzów.""",

     """Sprzedam Audi Model A5. Rok produkcji 2014.  Cena 57900 PLN. Opis: Paliwo Diesel  Przebieg 266000   Skrzynia biegów  Manualna Typ nadwozia Coupe  Pojemność  1968cm3   Moc 177kM  Kolor  Czarny.  Kontakt tel.693122998.   Miejscowość Augustów.""",

     """Sprzedam Hyundai Model i20. Rok produkcji 2012.  Cena 20900 PLN. Parametry:  Paliwo Benzyna  Przebieg 129000   Skrzynia biegów  Manualna Typ nadwozia Sedan  Pojemność  1248cm3   Moc 78kM  Kolor  Grafitowo-szary.  Kontakt tel.690500806.   Miejscowość Warszawa.""",

     """Sprzedam Mazda Model 6. Rok produkcji 2018.  Cena 81000 PLN.   Parametry: Paliwo Benzyna  Przebieg 35548   Skrzynia biegów  Manualna Typ nadwozia Sedan  Pojemność  1998cm3   Moc 165kM  Kolor Bordowy.  Kontakt tel.500109446.   Miejscowość Poznań.""",

     """Sprzedam Opel Model Mokka 1.6 CDTI. Rok produkcji 2017. Cena 48900 PLN. Parametry: Paliwo Benzyna  Przebieg 212000   Skrzynia biegów  Manualna Typ nadwozia SUV  Pojemność  1598cm3   Moc 136kM  Kolor Szary.  Kontakt tel.508144360.   Miejscowość Górczyna.""",

     """Sprzedam Audi Model Q5. Rok produkcji 2020. Cena 124800 PLN. Parametry: Paliwo Diesel  Przebieg 80900   Skrzynia biegów  Automatyczna Typ nadwozia SUV Pojemność  1968cm3   Moc 163kM  Kolor Czarny.  Kontakt tel.604948086.   Miejscowość Płock.""",

     """Sprzedam Toyota Model RAV4. Rok produkcji 2020. Cena 129800 PLN. Parametry: Paliwo Hybryda  Przebieg 131800   Skrzynia biegów  Automatyczna Typ nadwozia SUV  Pojemność  2487cm3   Moc 177kM  Kolor Biały.  Kontakt tel.604948086.   Miejscowość Płock.""",

     """Sprzedam Volkswagen Model Passat 2.0 TDI. Rok produkcji 2018. Cena 53999 PLN. Parametry: Paliwo Diesel  Przebieg 130000   Skrzynia biegów  Manualna Typ nadwozia Kombi  Pojemność  1968cm3   Moc 150kM  Kolor Szary.  Kontakt tel.516495718.   Miejscowość Lębork.""",

     """Sprzedam Honda Model Accord 2.0 Comfort. Rok produkcji 2007. Cena 29000 PLN. Parametry: Paliwo Benzyna  Przebieg 87000   Skrzynia biegów  Manualna Typ nadwozia Sedan  Pojemność  1998cm3   Moc 155kM  Kolor Szary.  Kontakt tel.508174534.   Miejscowość Warszawa.""",

     """Sprzedam Nissan Model Qashqa 1.2. Rok produkcji 2014. Cena 54900 PLN.  Opis: Paliwo Benzyna  Przebieg 121300   Skrzynia biegów  Manualna Typ nadwozia Sedan  Pojemność  1197cm3   Moc 115kM  Kolor Brązowy.  Kontakt tel.531357525.   Miejscowość Kraków.""",

     """Sprzedam BMW Model 320i. Rok produkcji 2008. Cena 28700 PLN.   Opis: Paliwo Benzyna  Przebieg 204000   Skrzynia biegów  Manualna Typ nadwozia Sedan  Pojemność  1995cm3   Moc 170kM  Kolor Czarny.  Kontakt tel.600617266.   Miejscowość Września.""",

     """Sprzedam Audi Model Q7. Rok produkcji 2007. Cena 31000 PLN.  Opis:  Paliwo Benzyna  Przebieg 192000   Skrzynia biegów  Automatyczna Typ nadwozia SUV  Pojemność  3597cm3   Moc 280kM  Kolor Czarny.  Kontakt tel.601781765.   Miejscowość Ryki.""",

     """Sprzedam Kia Model Ceed 1.4 CVVT. Rok produkcji 2008. Cena 15500 PLN.  Opis:  Paliwo Benzyna  Przebieg 168000   Skrzynia biegów  Manualna Typ nadwozia Kombi  Pojemność  1396cm3   Moc 109kM  Kolor Srebrny.  Kontakt tel.573505054.   Miejscowość Warszawa.""",

     """Sprzedam Ford Model Mondeo. Rok produkcji 2017. Cena 49500 PLN.  Opis: Paliwo Diesel  Przebieg 239000   Skrzynia biegów  Automatyczna Typ nadwozia Sedan  Pojemność  1997cm3   Moc 180kM  Kolor Grafit ciemny.  Kontakt tel.459055525.   Miejscowość Siechnice.""",

     """Sprzedam Opel Model Astra. Rok produkcji 2004. Cena 6000 PLN.  Opis:  Paliwo Benzyna  Przebieg 230000   Skrzynia biegów  Manualna Typ nadwozia Sedan  Pojemność  1598cm3   Moc 105kM  Kolor Srebrny.  Kontakt tel.7536659889.   Miejscowość Łukowice Brzeskie.""",

     """Sprzedam Toyota Model Yaris. Rok produkcji 2018. Cena 53800 PLN.  Opis:  Paliwo Hybryda  Przebieg 48800  Skrzynia biegów  Auyomatyczna Typ nadwozia Kompakt  Pojemność  1497cm3  Moc 100kM  Kolor Biały.  Kontakt tel.782124587.  Miejscowość Kielce.""",

     """Szybko sprzedam Ford Model: Kuga, rok produkcji: 2009. Opis: Paliwo: Diesel Typ nadwozia: SUV Przebieg: 290000 km  Kolor: Inny kolor Poj. silnika: 2 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Moc silnika: 136 KM Napęd: 4x4 (stały). Lokalizacja Gdańsk. kontakt: alicja.s@wp.pl Cena 18500.""",

"""sprzedam Toyota Model: Yaris, Rok produkcji: 2017. Opis: Paliwo: Benzyna Typ nadwozia: Hatchback Przebieg: 34 000 km Kolor: Czerwony Poj. silnika: 998 cm³ Skrzynia biegów: Manualna Moc silnika: 70 KM Napęd: Na przednie koła. Cena 35000.""",

"""Pilnie sprzedam Ford Cena 30000 Numer VIN: WF0EXXWPCEGK39413 Model: Mondeo Rok produkcji: 2016 Paliwo: Diesel Typ nadwozia: Hatchback Przebieg: 290 580 km Kolor: Czarny Poj. silnika: 1997 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna  Kraj pochodzenia: Polska  Moc silnika: 180 KM""",

"""Sprzedam Honda Model: CR-V Cena 19000 Rok produkcji: 2007 Paliwo: Benzyna Typ nadwozia: SUV Przebieg: 188 000 km Kolor: Srebrny Poj. silnika: 2 000 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska Kraków tel. 567980123 Moc silnika: 150 KM""",

"""Sprzedam Ferrari 308 GTS Quattrovalvole Rok: 1984 Silnik: 2927 cm3 Moc 241 KM Skrzynia biegów: Manualna Przebieg: 42 318 Mil Samochód zarejestrowany jako zabytek Cena: 239 000 tyś zł. Do negocjacji!""",

"""Firma sprzeda Mercedes Cena 16000 Model: Pozostałe Mercedes Rok produkcji: 1977 Paliwo: Diesel Typ nadwozia: Coupe Przebieg: 250 000 km Kolor: Czarny Poj. silnika: 3 000 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Automatyczna Moc silnika: 79 KM""",

"""Sprzedam Renault Model: Scenic Cena 23000 Rok produkcji: 2014 Paliwo: Benzyna Typ nadwozia: Minivan Przebieg: 120 000 km Kolor: Niebieski Poj. silnika: 1 197 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska  Moc silnika: 115 KM""",

"""Firmowe auto na sprzedaż Skoda Cena 31000 Model: RAPID Rok produkcji: 2018 Paliwo: Benzyna Typ nadwozia: Sedan Przebieg: 55 000 km Kolor: Szary Poj. silnika: 1 000 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna kontakt +48 58 3871234 Gdańsk Moc silnika: 110 KM""",

"""Sprzedam Infiniti Cena 14500 Numer VIN: JNKDA31A63T108292 Model: I35 Rok produkcji: 2002 Paliwo: LPG Typ nadwozia: Sedan Przebieg: 220 000 km Kolor: Srebrny Poj. silnika: 3 495 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Automatyczna Kraj pochodzenia: Stany Zjednoczone Moc silnika: 255 KM""",

"""Okazja Volkswagen Cena 12000 Model: Sharan Rok produkcji: 2005 Paliwo: Diesel Typ nadwozia: Minivan Przebieg: 295 000 km Kolor: Inny kolor Poj. silnika: 1 896 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Niemcy Moc silnika: 115 KM""",

"""Sprzedam Skoda Cena 21000 Model: Octavia Rok produkcji: 2014 Paliwo: Diesel Typ nadwozia: Kombi Przebieg: 292 000 km Kolor: Srebrny Poj. silnika: 1 600 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska Kontakt 501234543""",

"""Pilnie odstąpię Mazda Cena 17 900 Model: 5 Rok produkcji: 2009 Paliwo: Benzyna Typ nadwozia: Kombi Przebieg: 145 000 km Kolor: Inny kolor Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska Olsztyn Kontakt mail ziutek@onet.pl Moc silnika: 145 KM""",

"""Sprzedam Nissan Cena 27700 Numer VIN: VSKDAAC13U0035933 Model: Pulsar Rok produkcji: 2015 Paliwo: Diesel Typ nadwozia: Sedan Przebieg: 160 050 km Kolor: Czerwony Poj. silnika: 1 500 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna  Kraj pochodzenia: Austria Moc silnika: 110 KM Kontakt Wrocław tel 345678012""",

"""OKazja Ford Cena 54500 Numer VIN: WF0JXXWPCJHJ71971 Model: S-Max Rok produkcji: 2017 Paliwo: Diesel Typ nadwozia: SUV Przebieg: 211 000 km Kolor: Inny kolor Poj. silnika: 2 000 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Automatyczna Kraj pochodzenia: Niemcy  Moc silnika: 180 KM Pierwszy właściciel Kraków tel. 304567098""",

"""Sprzedam Audi Cena 27900 Numer VIN: WAUZZZ8E43A321682 Model: A4 Rok produkcji: 2003 Paliwo: LPG+Benzyna Typ nadwozia: Sedan Przebieg: 234 680 km Kolor: Szary Poj. silnika: 2 393 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Niemcy Moc silnika: 170 KM Tel. 234123432""",

"""Pilnie sprzedam Fiat Cena 14900 Model: Panda Rok produkcji: 2012 Paliwo: Benzyna Typ nadwozia: Hatchback Przebieg: 222 000 km Kolor: Inny kolor Poj. silnika: 900 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kontakt tel. 345654098""",

"""Okazja Renault Cena 9900  Numer VIN: VF1JK0AC642388910 Model: Grand Espace IV Rok produkcji: 2009 Paliwo: Benzyna+LPG Typ nadwozia: Minivan Przebieg: 274 519 km Kolor: Czarny Poj. silnika: 2 000 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Holandia Moc silnika: 170 KM Kontakt Warszawa tel. 456782321""",

"""Sprzedam Toyota Cena 38000 Numer VIN: VNKKL3D350A248915 Model: Yaris III Rok produkcji: 2017 Paliwo: Benzyna Typ nadwozia: Hatchback Przebieg: 34 000 km Kolor: Czerwony Poj. silnika: 998 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska Moc silnika: 70 KM Miejscowość Bydgoszcz tel, 567432123""",

"""Sprzdaż Opel Cena 2500 Model: Zafira Rok produkcji: 2000 Paliwo: Diesel Typ nadwozia: Minivan Przebieg: 447 km Kolor: Srebrny Poj. silnika: 1 906 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska Moc silnika: 101 KM Kontakt mail d.kowalski@wp.pl""",

"""Sprzedam Kia cena 3500 Numer VIN: KNEJA5535VD0100593500 Model: Sportage Rok produkcji: 1998 Paliwo: Benzyna Typ nadwozia: SUV Przebieg: 222 239 km Kolor: Zielony Poj. silnika: 1 998 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska Moc silnika: 10 KM Miejscowość Katowice tel.807976543""",

"""Sprzedam Volvo Cena 9000 Numer VIN: YV1MW384962165189 Model: V50 Rok produkcji: 2005 Paliwo: Benzyna Typ nadwozia: Kombi Przebieg: 363 423 km Kolor: Inny kolor Poj. silnika: 2 435 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Automatyczna Moc silnika: 125 KM Tel. 456764324""",

"""Okazja sprzedam Subaru Cena77777 Model: Forester Rok produkcji: 2015 Paliwo: Benzyna Typ nadwozia: SUV Przebieg: 112 000 km Kolor: Inny kolor Poj. silnika: 1 995 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska Moc silnika: 150 KM telefon 765890123""",

"""Sprzedam Peugeot Model: 308 Cena 31900 Rok produkcji: 2015 Paliwo: Benzyna Typ nadwozia: Kombi Przebieg: 145 000 km Kolor: Biały Poj. silnika: 1 199 cm³ Stan techniczny: Nieuszkodzony Skrzynia biegów: Manualna Kraj pochodzenia: Polska Moc silnika: 135 KM Miasto Kielce Telefon +48 345234887""",

"""Sprzedam Mazda Cena53500 Model: 3 Rok produkcji: 2017 Paliwo: Benzyna Typ nadwozia: Hatchback Przebieg: 55 000 km  Kolor: Brązowy – Beżowy Poj. silnika: 2 000 cm³ Stan techniczny: Nieuszkodzony  Skrzynia biegów: Manualna  Kraj pochodzenia: Niemcy  Moc silnika: 143 KM Kontakt Gdynia tel.435678009""",

"""Szybko sprzedam Ford, Model: Mondeo, Rok produkcji: 2011, Paliwo: Diesel, Typ nadwozia: Kombi, Przebieg: 150000 km , Kolor: Szart, Poj. silnika: 2000, cm³
Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Niemcy, Moc silnika: 136 KM, Napęd: 4x4, Lokalizacja Gdynia,
kontakt: ala.s@wp.pl,Cena 28000""",

     """Okazja sprzedam Toyota, Numer VIN: VNKKL3D350A248915, Model: Yaris II, Rok produkcji: 2015, Paliwo: Benzyna, Typ nadwozia: Hatchback, Przebieg: 94 000 km,
Kolor: Biały, Poj. silnika: 998 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska, Moc silnika: 55 KM,
Napęd: Na przednie koła, Cena 15000""",

     """Sprzedam  Ford, Cena 35000, Numer VIN: WF0EXXWrWEGK39413, Model: Kona, Rok produkcji: 2017, Paliwo: Benzyna, Typ nadwozia: Hatchback, Przebieg: 190 580 km,
Kolor: Czarny, Poj. silnika: 1600 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska, Moc silnika: 180 KM,""",

     """Sprzedam Honda, Cena 29000, Model: Civic, Rok produkcji: 2009, Paliwo: Benzyna, Typ nadwozia: Sedan, Przebieg: 150 000 km, Kolor: Szary, Poj. silnika: 13000 cm³,
Stan techniczny: Nieuszkodzony, Skrzynia biegów: Automat, Kraj pochodzenia: Polska Kraków, tel. 567980657, Moc silnika: 133 KM""",

     """Sprzedam Fiat, Model 1500PL, Rok: 1984 Silnik: 1200cm3, Moc 55 KM, Skrzynia biegów: Manualna, Przebieg: 242 222km, 
Samochód zarejestrowany jako zabytek, Cena: 2500 zł., """,

     """Sprzedam Skoda, Model: Fabia, Rok produkcji: 2012, Paliwo: Diesel, Typ nadwozia: Kombi, Przebieg: 150 000 km,
Kolor: Nibieski, Poj. silnika: 1600 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manual, Moc silnika: 79 KM, Cena 17999,""",

     """Sprzedam Renault Model: Megane, Cena 26000, Rok produkcji: 2016, Paliwo: Benzyna, Typ nadwozia: Sedan, Przebieg: 125 000 km, Kolor: Niebieski,
Poj. silnika: 1 597 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska Wrocław,  Moc silnika: 85 KM,""",

     """Auto na sprzedaż Skoda, Cena 24000, Model: Octawia, Rok produkcji: 2017 Paliwo: Benzyna, Typ nadwozia: Sedan, Przebieg: 75 000 km, Kolor: Szary metalik,
Poj. silnika: 1 300 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, kontakt +48 58 2231234 Gdańsk, Moc silnika: 130 KM,""",

     """Sprzedam Ford, Model Mustang, Cena 24500, Rok produkcji: 2012, Paliwo: Benzyna, Typ nadwozia: Sedan, Przebieg: 120 000 km,
Kolor: Srebrny, Poj. silnika: 1495 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Automatyczna, Kraj pochodzenia: Stany Zjednoczone,
Moc silnika: 255 KM, Kontakt Szczecin mail: roman_wasik@onet.pl,""",

     """Okazja Volkswagen, Cena 32000, Model: Passat, Rok produkcji: 2009, Paliwo: Diesel, Typ nadwozia: Sedan, Przebieg: 202 000 km, Kolor: Zielony,
Poj. silnika: 1 896 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Niemcy, Moc silnika: 115 KM, Kontakt Gorzów Wlkp. tel. 345654321,""",

     """Sprzedam Skoda, Cena 24000, Model: Octavia Rok produkcji: 2015, Paliwo: Diesel, Typ nadwozia: Kombi, Przebieg: 302 000 km ,Kolor: Szary metalic,
Poj. silnika: 1 800 cm³, Stan techniczny: Lekko uszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska Wałcz, Kontakt 501321213,""",

     """Odstąpię Mazda, Cena 37 900 Model: 6, Rok produkcji: 2012, Paliwo: Benzyna, Typ nadwozia: Kombi, Przebieg: 245 000 km, Kolor: Biały, 
Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna,Kraj pochodzenia: Polska Olsztyn, Kontakt mail zenon.kloc@onet.pl, Moc silnika: 105 KM,""",

     """Sprzedam KIA, Cena 47700, Model: Civic, Rok produkcji: 2012, Paliwo: Diesel, Typ nadwozia: Sedan, Przebieg: 60 050 km,
Kolor: Czerwony, Poj. silnika: 1 500 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Moc silnika: 100 KM,
Kontakt Wrocław tel 501234456,""",

     """OKazja Ford, Cena 34500, Model: Mondeo, Rok produkcji: 2016, Paliwo: Diesel,Typ nadwozia: SUV, Przebieg: 233 000 km, Kolor: Grafitowy,
Poj. silnika: 1300 cm³, Kontakt Kraków tel. 602345123,""",

     """Sprzedam Audi, Cena 47900, Model: A3, Rok produkcji: 2009, Paliwo: LPG+Benzyna, Typ nadwozia: Sedan,,Przebieg: 134 680 km,
Kolor: Szary, Poj. silnika: 2 005 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Niemcy, Moc silnika: 170 KM,
Kontakt R.Chudy Tel. 234123432,""",

     """Pilnie sprzedam Fiat, Cena 4900, Model: Croma, Rok produkcji: 2007, Paliwo: Benzyna, Typ nadwozia: Hatchback, Przebieg: 322 000 km, Kolor: Biały,
Poj. silnika: 1100 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kontakt Warszawa tel. 345654098,""",

     """Pilnie sprzedam Renault, Cena 19900, Model: Megane, Rok produkcji: 2011, Paliwo: Benzyna, Typ nadwozia: Minivan, Przebieg: 220000km,
Kolor: Czarny, Poj. silnika: 2 000 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Holandia,
Moc silnika: 125 KM, Kontakt Warszawa tel. 234213453,""",

     """Sprzedam Toyota, Cena 24000, Model: Yaris II, Rok produkcji: 2014, Paliwo: Benzyna, Typ nadwozia: Hatchback, Przebieg: 134 000 km,
Kolor: Czarny, Poj. silnika: 998 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska, Moc silnika: 75 KM,
Miejscowość Bydgoszcz tel, 604234567,""",

     """Sprzdam Opel, Cena 22500, Model: Zafira, Rok produkcji: 20009, Paliwo: Diesel, Typ nadwozia: Minivan, Przebieg: 254000 km, Kolor: Srebrny,
Poj. silnika: 1 506 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska, Moc silnika: 125 KM,
Kontakt mail d.kwiatkowski@wp.pl,""",

     """Sprzedam Kia, cena 33500, Numer VIN: KZZSE5535VD0234593500, Model: Civic, Rok produkcji: 2009, Paliwo: Benzyna, Typ nadwozia: Kombi, Przebieg: 178000km,
Kolor: Złoty metalik, Poj. silnika: 1 998 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska, Moc silnika: 123KM,
Miejscowość Katowice tel.234987453,""",

     """Sprzedam Volvo, Cena 29000, Model: V90, Rok produkcji: 2015, Paliwo: Benzyna, Typ nadwozia: Kombi, Przebieg: 250000km,
Kolor: Szary, Poj. silnika: 2005 cm³, Stan techniczny: Mały remont, Skrzynia biegów: Automatyczna, Moc silnika: 135 KM,Kontakt Opole, Tel. 602343231,""",

     """Okazja sprzedam Hundai, Cena 27000, Model: I30, Rok produkcji: 2013, Paliwo: Benzyna, Typ nadwozia: SUV, Przebieg: 212 000 km, Kolor: Brązowy,
Poj. silnika: 1 200 cm³, Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska, Moc silnika: 120 KM, telefon 609453213,""",

     """Sprzedam Peugeot, Model: 407, Cena 13000, Rok produkcji: 2005, Paliwo: Benzyna, Typ nadwozia: Kombi, Przebieg: 345 000 km, Kolor: Biały, Poj. silnika: 1485 cm³,
Stan techniczny: Nieuszkodzony, Skrzynia biegów: Manualna, Kraj pochodzenia: Polska, Moc silnika: 90 KM, Miasto Kielce Telefon +48 045678093,""",

     """Sprzedam Mazda, Cena 43500, Model: 6, Rok produkcji: 2016, Paliwo: Benzyna ,Typ nadwozia: SUV, Przebieg: 155 000 km,  Kolor: Beżowy,
Poj. silnika: 2 100 cm³, Stan techniczny: Nieuszkodzony,  Skrzynia biegów: Manualna, Kraj pochodzenia: Niemcy,  Moc silnika: 123 KM,
Kontakt Gdynia tel.234567654,""",

     """Sprzedam Opel, Model Omega, Rok produkcji 1995, Cena 4000, Paliwo Diesel, Przebieg 348340, Skrzynia biegów Manualna, Typ nadwozia Sedan,
Pojemność 150048cm3, Moc 105kM, Kolor Czarny, Kontakt tel.664321432, Miejscowość Kraków,""",

     """Sprzedam Lexus, Model XS 120z, Rok produkcji 2018, Cena 100300, Paliwo Hybryda, Przebieg 102000, Skrzynia biegów Automat,
Typ nadwozia Sedan, Pojemność 2487cm3, Moc 178kM, Kolor Biały, Kontakt tel.608678920, Miejscowość Błonie,""",

     """Sprzedam Mercedes, Model Klasa CE 1.8, Rok produkcji 1999, Cena 25220, Paliwo Benzyna, Przebieg 300200, Skrzynia biegów Manualna,
Typ nadwozia Kombi, Pojemność 2199, Moc 150kM, Kolor Szary metalik, Kontakt tel.501234562, Miejscowość Białystok,""",

     """Sprzedam Audi, Model A4, Rok produkcji 2013, Cena 49000, Paliwo Benzyna, Przebieg 160000, Skrzynia biegów Manualna, 
Typ nadwozia Kombi, Pojemność 1560cm3, Moc 155kM, Kolor Srebrny, Kontakt tel.506600432, Miejscowość Radom,""",

     """Sprzedam Mazda, Model CX-3, Rok produkcji 2014, Cena 55900, Paliwo Benzyna, Przebieg 299000, Skrzynia biegów Automatyczna, 
Typ nadwozia SUV, Pojemność 1488cm3, Moc 135kM, Kolor Czarny, Kontakt tel.601342768, Miejscowość Warszawa,""",

     """Sprzedam Chrysler, Model Pacifica, Rok produkcji 2015, Cena 82900, Paliwo Benzyna, Przebieg 157000, Skrzynia biegów Automatyczna,
Typ nadwozia SUV, Pojemność 2800cm3, Moc 200kM, Kolor Biel, Kontakt tel.698900234, Miejscowość Okonek,""",

     """Sprzedam Volvo, Model XC30, Rok produkcji 2009, Cena 35000, Paliwo Benzyna, Przebieg 370000, Skrzynia biegów Automatyczna,
Typ nadwozia SUV, Pojemność 3800cm3, Moc 275kM, Kolor Szary, Kontakt tel.500456765, Miejscowość Gdańsk,""",

     """Sprzedam Porsche, Model Sport, Rok produkcji 2011, Cena 61900, Paliwo Benzyna, Przebieg 264000, Skrzynia biegów Automatyczna, 
Typ nadwozia Sedan, Pojemność 32800cm3, Moc 250kM, Kolor Czerwony, Kontakt tel.501234654, Miejscowość Kud0wa Zdrój,""",

     """Sprzedam Toyota, Model Corolla 1.4, Rok produkcji 2018, Cena 45900, Paliwo Benzyna, Przebieg 190000, Skrzynia biegów Automatyczna,
Typ nadwozia Kombi, Pojemność 1400cm3, Moc 102kM, Kolor Biały, Kontakt tel.601456765, Miejscowość Chojnice,""",

     """Sprzedam Audi, Model A3, Rok produkcji 2004, Cena 27900, Paliwo Diesel, Przebieg 366000, Skrzynia biegów Manualna, 
Typ nadwozia Kombi, Pojemność 1498cm3, Moc 150kM, Kolor Czarny, Kontakt tel.608784912, Miejscowość Aleksandrów kujawski,""",

     """Sprzedam Hyundai, Model i30, Rok produkcji 2010, Cena 18900, Paliwo Benzyna, Przebieg 229000, Skrzynia biegów Manualna, 
Typ nadwozia Sedan, Pojemność 1100cm3, Moc 98kM, Kolor Grnatowy, Kontakt tel.609231099, Miejscowość Warszawa-Ochota,""",

     """Sprzedam Mazda, Model 3, Rok produkcji 2016, Cena 61000, Paliwo Benzyna, Przebieg 120500, Skrzynia biegów Manualna,
Typ nadwozia Sedan, Pojemność 1650cm3, Moc 125, Kolor Czarny, Miejscowość Zawoja, tel. 602667554,""",

     """Sprzedam Opel, Model SENATOR, Rok produkcji 2015, Cena 34500, Paliwo Benzyna, Przebieg 164000, Skrzynia biegów Manualna,
Typ nadwozia SUV,  Pojemność  1800cm3, Moc 118kM, Kolor Srebrny, Kontakt tel.505564700, Miejscowość Gdańsk,""",

     """Sprzedam Audi, Model Q3, Rok produkcji 2018, Cena 89000, Paliwo Diesel, Przebieg 123000, Skrzynia biegów Automatyczna, 
Typ nadwozia SUV, Pojemność  1968cm3, Moc 155kM, Kolor Czarny, Kontakt tel.602456654, Miejscowość Poznań,""",

     """Sprzedam Toyota, Model Camry, Rok produkcji 2009, Cena 35000, Paliwo Diesel, Przebieg 230000, Skrzynia biegów Automatyczna,
Typ nadwozia Sedan, Pojemność 1800cm3, Moc 145kM, Kolor Biały, Kontakt tel.501211980, Miejscowość Puławy,""",

     """Sprzedam Volkswagen, Model Passat, Rok produkcji 2014, Cena 34000, Paliwo Diesel, Przebieg 180000, Skrzynia biegów Manualna, 
Typ nadwozia Kombi, Pojemność 1968cm3, Moc 125k, Kolor Srebrny, Kontakt tel.504433955, Miejscowość Lędyczek Zdrój,""",

     """Sprzedam Honda, Model Civic, Rok produkcji 2009, Cena 19000   Paliwo Benzyna  Przebieg 87000   Skrzynia biegów  Manualna 
Typ nadwozia Sedan, Pojemność 1600cm3, Moc 155kM, Kolor Szary, Kontakt tel.507099231, Miejscowość Warszawa,""",

     """Sprzedam Nissan, Model Qashqai, Rok produkcji 2012, Cena 44900, Paliwo Benzyna, Przebieg 165000, Skrzynia biegów Manualna, 
Typ nadwozia Sedan, Pojemność 1098cm3, Moc 115kM, Kolor Beżowy, Kontakt tel.501230034, Miejscowość Kraków,""",

     """Sprzedam BMW, Model 501, Rok produkcji 2000, Cena 18700, Paliwo Benzyna, Przebieg 304000, Skrzynia biegów Manualna,
Typ nadwozia Sedan, Pojemność 1600cm3, Moc 155kM, Kolor Czarny, Kontakt tel.601232122, Miejscowość Wrocław,""",

     """Sprzedam Audi, Model Q3, Rok produkcji 2002, Cena 21000,  Paliwo Benzyna, Przebieg 230000, Skrzynia biegów Automatyczna,
Typ nadwozia Sedan, Pojemność 2300cm3, Moc 205kM, Kolor Czarny, Kontakt tel.601456789, Miejscowość Rzeszów,""",

     """Sprzedam Kia, Model Sportage, Rok produkcji 2009, Cena 25500, Paliwo Benzyna, Przebieg 141680, Skrzynia biegów Manualna, 
Typ nadwozia Kombi, Pojemność 1196cm3, Moc 110kM, Kolor Szary metalik, Kontakt tel.501877658, Miejscowość Warszawa,""",

     """
Sprzedam Ford, Model Mustang, Rok produkcji 2005, Cena 29500, Paliwo Diesel, Przebieg 320000, Skrzynia biegów Automatyczna,
Typ nadwozia Sedan, Pojemność 1650cm3, Moc 155kM, Kolor Biały, Kontakt tel.609332564, Miejscowość Szczecin,""",

     """Sprzedam Opel, Model Mokka, Rok produkcji 2014, Cena 46000, Paliwo Benzyna, Przebieg 330000, Skrzynia biegów Manualna,
Typ nadwozia Sedan, Pojemność  1398cm3, Moc 125kM, Kolor Srebrny, Kontakt tel.604540980, Miejscowość Ełk,""",

     """Sprzedam Toyota, Model Yaris 3, Rok produkcji 2019, Cena 43500, Paliwo Hybryda, Przebieg 68800, Skrzynia biegów Auyomatyczna,
Typ nadwozia Kompakt, Pojemność 1497cm3, Moc 100kM, Kolor Biało-Czarny, Kontakt tel.701988344, Miejscowość Biała Podlaska,""",
     ]