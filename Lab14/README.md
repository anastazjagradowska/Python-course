# Język Python - Lab14 - Dekoratory
**Zad.1** 
Proszę utworzyć klasę definiującą współrzędne punktu na płaszczyźnie. Obie współrzędne proszę zdefiniować jako własności (metoda inicjalizacyjna bezparametrowa).

**Zad.2** 
Proszę zdefiniować funkcje dodawania i odejmowania współrzędnych (z wykorzystaniem wcześniej zdefiniowanej klasy) oraz opatrzyć je dekoratorem (implementowanym jako funkcja) sprawdzającym czy współrzędne leżą w określonym zakresie, jeżeli nie - proszę zgłosić wyjątek.

**Zad.3** 
Proszę utworzyć klasę z metodami statycznymi obliczającymi obwód i pole trójkąta lub czworokąta (dających się wpisać w okrąg, odpowiednio wzory Herona i Brahmagupty), zdefiniowanych poprzez współrzędne wierzchołków (klasa z zadania 1).

Wzór Herona: P=[p(p-a)(p-b)(p-c)]^1/2, gdzie: a,b,c - długości boków, p - połowa obwodu
Wzór Brahmagupty: P=[(p-a)(p-b)(p-c)(p-d)]^1/2, oznaczenia j.w.

**Zad.4** 
Proszę utworzyć dekorator (implementowany jako klasa) umożliwiający zliczenie liczby wywołań poszczególnych funkcji obłożonych dekoratorem, z metodą statyczną zwracającą wynik.