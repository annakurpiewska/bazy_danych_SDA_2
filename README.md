1. Wczytanie danych z API - https://randomuser.me/ do bazy danych. Co zapisać do bazy danych:
  * Pole NAME
  * Pole LASTNAME
  * Pole AGE
  * Pole Gender
  * Pole PHONE_NUMBER - oczyść numer telefonu ze znaków specjalnych (powinny zostać same cyfry)
  * Pole DAYS_TO_BIRTHDAY stwórz dodatkowe pole z liczbą dni pozostałych do urodzin danej osoby
  * Pole CITY
  * Pole BIRTHDAY
  
2. Na podstawie danych zapisanych w bazie wyświetl:
  * procent kobiet i mężczyzn
  * średnią wieku:
    * ogólną
    * kobiet
    * mężczyzn
  * **N** najbardziej popularnych miast w formacie: miasto, liczba wystąpień, gdzie **N** to liczba - parametr przekazywany do programu przez użytkownika, czyli np. dla **N** = 5 powinno wyświetlić się 5 miast
  * wszystkich użytkowników którzy urodzili się w zakresie dat podanym jako parametr (format daty jest dowolny, może być np. *YYYY-MM-DD*)

Zaprojektowanie interfejsu linii poleceń to część tego zadania. Każdy z tych punktów powinien być zrealizowany jako osobna komenda wywoływana z tego samego skryptu, np.:

*python script.py -average-age male*

powinno zwrócić średni wiek mężczyzn z bazy danych,


Wymagania techniczne:
* Python 3.6+
* README z opisem jak postawić projekt oraz spisem dostępnych komend
* kod napisany obiektowo

Zadania dodatkowe:
* napisać testy jednostkowe z użyciem pytest

Prośba o umieszczenie rozwiązania w publicznie dostępnym repozytorium systemu kontroli wersji git (github, bitbucket, gitlab itp.).
Proszę nie skupiać się na pisaniu “ekstra optymalnego” kodu - w pierwszej kolejności będzie oceniana jakość kodu (czytelność, rozszerzalność, łatwość modyfikowania).
Na ocenę również wpłynie gitflow.
