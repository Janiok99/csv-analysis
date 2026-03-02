# CSV Data Analysis (Python + Pandas)

Projekt przedstawia kompletny proces analizy danych zapisanych w pliku CSV.  
Zawiera wczytywanie danych, generowanie statystyk opisowych, filtrowanie, sortowanie, grupowanie oraz wizualizację wyników na wykresie słupkowym.

Całość opiera się na bibliotekach **pandas** i **matplotlib**, dzięki czemu projekt stanowi praktyczne wprowadzenie do analizy danych w Pythonie.

## Struktura projektu
    csv-analysis/
    └── src/
        ├── main.py          # Główny skrypt uruchamiający analizę
        ├── analysis.py      # Moduł z funkcjami przetwarzającymi dane
    └── data/
        ├──sales.csv    # Plik wejściowy z danymi sprzedaży
    └──README.md

## Funkcjonalności

    ### ✔ Wczytywanie danych  
    Za pomocą `pandas.read_csv()`.

    ### ✔ Wyświetlanie statystyk opisowych  
    Średnia, min, max, odchylenie standardowe itd.

    ### ✔ Filtrowanie danych  
    Np. produkty o ilości większej niż zadany próg.

    ### ✔ Sortowanie danych  
    Sortowanie po cenie malejąco.

    ### ✔ Grupowanie i agregacja  
    Sumowanie sprzedanych ilości dla każdego produktu.

    ### ✔ Wizualizacja danych  
    Wykres słupkowy przedstawiający sumę sprzedanych produktów.

## Jak działa projekt

    ### **main.py**
    Odpowiada za cały przepływ:

        - wczytuje plik CSV,
        - wyświetla dane,
        - pokazuje statystyki,
        - filtruje dane,
        - sortuje dane,
        - grupuje i sumuje ilości,
        - generuje wykres.

    ### **analysis.py**
    Zawiera funkcje pomocnicze:

        - `load_data(path)` – wczytuje dane z CSV  
        - `basic_stats(df)` – wyświetla statystyki opisowe  
        - `filter_data(df, min_quantity)` – filtruje dane  
        - `sort_data(df)` – sortuje po cenie  
        - `group_and_sum(df)` – grupuje po produkcie i sumuje ilości  
        - `plot_data(df)` – tworzy wykres słupkowy  

## Wymagania

    Zainstaluj wymagane biblioteki:
    pip install pandas matplotlib

## Uruchamianie projektu

    1. W katalogu głównym projektu uruchom:
        python main.py
    2. Upewnij się, że plik CSV znajduje się w:
        data/sales.csv

## Przykładowy plik CSV (sales.csv)

    product,price,quantity
    Laptop,3500,4
    Mouse,50,20
    Keyboard,120,10
    Monitor,900,5
    Laptop,3500,2
    Mouse,50,15

    Kolumny:

    - **product** – nazwa produktu  
    - **price** – cena  
    - **quantity** – sprzedana ilość  

## Przykładowe wyniki

    ### Statystyki opisowe  
    Wyświetlane przez `df.describe()`.

    ### Filtrowanie  
    Produkty z ilością > 5.

    ### Sortowanie  
    Dane posortowane po cenie malejąco.

    ### Grupowanie  
    Suma sprzedanych ilości dla każdego produktu.

    ### Wykres  
    Wykres słupkowy przedstawiający sumę sprzedanych produktów.


