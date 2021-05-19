# Język Python - Lab10 - Iteratory 

**Zad.1** 
Proszę napisać iterator zwracający kolejne wyrazy ciągu Fibonacciego dwoma sposobami (jedna lub dwie klasy) i porównać ich wykorzystanie.

**Zad.2**
Proszę napisać iterator zwracający kolejne przybliżenie miejsca zerowego metodą Newtona-Raphsona: xn+1=xn-f(xn)/f'(xn) z zadaną dokładnością startując od określonej wartości początkowej, np. f(x)=sin(x)-(0.5x)2, x=1.5 i eps=10^-5 (pochodna - scipy.misc).
Proszę napisać iterator liczb pseudolosowych. Ciąg taki otrzymujemy ze wzoru: Xn+1 = (a * Xn + c) mod m, dla m = 2^31-1, a = 75, c = 0, x0 = 1.
Korzystając z zaimplementowanego iteratora proszę wylosować 10^5 par liczb z przedziału [0,1). Proszę sprawdzić jaki procent wylosowanych par mieści się w kwadracie o boku 0.1*n, gdzie n∈[1,10]. Otrzymany wynik proszę porównać z wynikiem uzyskiwanym z wykorzystaniem generatora liczb pseudolosowych z języka Python.

**Zad.3**
Proszę napisać iterator zwracający kolejne przybliżenie miejsca zerowego metodą Newtona-Raphsona: xn+1=xn-f(xn)/f'(xn) z zadaną dokładnością startując od określonej wartości początkowej, np. f(x)=sin(x)-(0.5x)2, x=1.5 i eps=10^-5 (pochodna - scipy.misc).