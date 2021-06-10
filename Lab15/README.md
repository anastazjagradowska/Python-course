# Język Python - Lab15 - Extending Python
**Zad.1** <br />
Proszę zapisać plik rozszerzenia (mod.c) oraz skrypt instalacyjny (setup.py). Proszę tak zmodyfikować plik rozszerzenia, aby otrzymywany wynik był poprawny, tj. np.: <br />
met(1,2)                 #3 <br />
met(1,2,5)               #8 <br />
met(1,2,5,[2,3,4])       #17<br /> 

**Zad.2** <br />
Proszę zaimplementować w Pythonie i w C funkcję dokonującą sortowania przez wstawianie jednowymiarowej tablicy liczb całkowitych, jako parametr do funkcji należy podać tablicę. Funkcję napisaną w C proszę wywołać z programu w Pythonie. Proszę porównać czasy wykonania obu funkcji dla takiej samej listy wartości losowych o rozmiarze  [10, 102, 103, 104] przy czym liczby losujemy z zakresu [0, rozmiar].

Sortowanie przez wstawianie (A, n) <br />

1:  for i=2 to n : <br />
2:  &nbsp;&nbsp;&nbsp;&nbsp;# Wstaw A[i] w posortowany ciąg A[1 ... i-1] <br />
3:  &nbsp;&nbsp;&nbsp;&nbsp;wstawiany_element = A[i] <br />
4:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;j = i - 1 <br />
5:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while j>0 and A[j]>wstawiany_element: <br />
6:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A[j + 1] = A[j] <br />
7:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;j = j - 1 <br />
8:  &nbsp;&nbsp;&nbsp;&nbsp;A[j + 1] = wstawiany_element <br />

**Zad.3** <br />
Proszę zmodyfikować plik rozszerzenia tak, aby była w nim funkcja, do której jako parametr będziemy przekazywać z Pythona słownik (klucze i wartości - liczby losowe z przedziału [10,100]). Dla każdej pary (klucz,wartość) proszę wywołać napisaną w języku C funkcję zwracającą największy wspólny dzielnik (poniżej) dwóch liczb przekazanych jako parametr, a wynik proszę zapisać w słowniku, który proszę zwrócić do Pythona.

AlgorytmEuklidesa(a, b) <br />

1: if b = 0 then <br />
2: return a <br />
3: else <br />
4: return AlgorytmEuklidesa(b, a mod b) <br />
5: end if <br />