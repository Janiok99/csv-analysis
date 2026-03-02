import pandas as pd
import matplotlib.pyplot as plt

def load_data(path: str) -> pd.DataFrame:
    """Wczytuje dane z pliku CSV."""
    return pd.read_csv(path)

def basic_stats(df: pd.DataFrame):
    """Wyświetla podstawowe statystyki."""
    print("\n--- Podstawowe statystyki ---")
    print(df.describe())

def filter_data(df: pd.DataFrame, min_quantity: int) -> pd.DataFrame:
    """Zwraca produkty o ilości większej niż min_quantity."""
    return df[df["quantity"] > min_quantity]

def sort_data(df: pd.DataFrame) -> pd.DataFrame:
    """Sortuje dane po cenie malejąco."""
    return df.sort_values(by="price", ascending=False)

def group_and_sum(df: pd.DataFrame):
    """Grupuje produkty i sumuje ilości."""
    print("\n--- Suma sprzedanych produktów ---")
    print(df.groupby("product")["quantity"].sum())

def plot_data(df: pd.DataFrame):
    """Tworzy wykres słupkowy sumy sprzedanych produktów."""
    grouped = df.groupby("product")["quantity"].sum()
    grouped.plot(kind="bar", title="Sprzedane produkty")
    plt.xlabel("Produkt")
    plt.ylabel("Ilość")
    plt.tight_layout()
    plt.show()
