from analysis import (
    load_data,
    basic_stats,
    filter_data,
    sort_data,
    group_and_sum,
    plot_data
)

def main():
    # Wczytanie danych
    df = load_data("../data/sales.csv")
    print("\nDane wczytane poprawnie!")
    print(df)

    # Statystyki
    basic_stats(df)

    # Filtrowanie
    filtered = filter_data(df, min_quantity=5)
    print("\n--- Produkty z ilością > 5 ---")
    print(filtered)

    # Sortowanie
    sorted_df = sort_data(df)
    print("\n--- Dane posortowane po cenie ---")
    print(sorted_df)

    # Grupowanie
    group_and_sum(df)

    # Wykres
    plot_data(df)

if __name__ == "__main__":
    main()
