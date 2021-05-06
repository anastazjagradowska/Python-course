# Język Python - Lab10
Zad.1 
Proszę utworzyć funkcję sprawdzającą poprawność numeru PESEL 
Parametrami wejściowymi do funkcji są: Pesel, data urodzenia (datetime.date) oraz płeć.
Przykłady:
- 02070803628, 8 lipca 1902, kobieta
- 02270803624, 8 lipca 2002, kobieta
- 02270812350, 8 lipca 2002, mężczyzna

PESEL
- cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
- cyfry 3-4 to dwie cyfry miesiąca urodzenia
- cyfry 5-6 to dwie cyfry dnia urodzenia
- cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
- cyfra 11 suma kontrolna

Do numeru miesiąca dodawane są następujące wartości w zależności od roku:
- dla lat 1800 - 1899 - 80
- dla lat 1900 - 1999 - 0
- dla lat 2000 - 2099 - 20
- dla lat 2100 - 2199 - 40
- dla lat 2200 - 2299 - 60

Suma kontrolna: każdą pozycję numeru ewidencyjnego mnoży się przez odpowiednią wagę, są to kolejno: 1 3 7 9 1 3 7 9 1 3 i sumuje.
Wynik dzieli się modulo 10 i otrzymaną wartość należy odjąć od 10 i znów podzielić przez modulo 10.
Otrzymana wartość powinna być zgodna z ostatnią cyfrą numeru PESEL.

Zad.2
Proszę napisać funkcję zwracającą średni wiek osób, który daty urodzenia zapisane są w plik daty.in. 
Funkcja powinna móc działać w trybie 'restrykcyjnym' - po napotkaniu niepoprawnej daty/wpisu zgłoszenie wyjątku i zakończenie działania, w trybie 'liberalnym' - niepoprawne wpisy są ignorowane.
Linia w pliku jest poprawna, jeśli zawiera dzień, miesiąc i rok,  które tworzą poprawną datę - zgodność liczby dni w miesiącu, w tym odpowiednia długość lutego w zależności od tego czy rok jest przestępny czy nie.
Rok przestępny: podzielny przez 4 i niepodzielny przez 100 lub podzielny przez 400.

Zad.3
Proszę napisać funkcję sprawdzającą czy elementy listy tworzą trójkę (a^2+b^2=c^2)/czwórkę(a^2+b^2+c^2=d^2) pitagorejską (funkcja ma działać dla dowolnej długości "podciągu"!). Proszę zgłosić wyjątek w przypadku niepoprawnej długości listy oraz w przypadku, gdy lista nie zawiera żadnych trójek/czwórek pitagorejskich. Dla każdej trójki/czwórki proszę sprawdzić ile jest w niej wartości parzystych i nieparzystych.
Listy testowe:
- l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
- l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
- l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
- l=(1,2,3,4,5,6,7,8,9)