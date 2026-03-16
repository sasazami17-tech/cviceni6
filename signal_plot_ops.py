import matplotlib.pyplot as plt


def load_signal_from_txt(path):
    """Načte hodnoty ze souboru .txt (jedna hodnota na řádek) a vrátí list[float]."""
    values = []
    try:
        with open(path, 'r') as file:
            for line in file:
                # Odstranění bílých znaků a převod na float
                stripped_line = line.strip()
                if stripped_line:
                    values.append(float(stripped_line))
    except FileNotFoundError:
        print(f"Chyba: Soubor {path} nebyl nalezen.")
    return values


def signal_min(values):
    """Vrátí minimální hodnotu ze seznamu."""
    return min(values) if values else None


def signal_max(values):
    """Vrátí maximální hodnotu ze seznamu."""
    return max(values) if values else None


def signal_avg(values):
    """Vrátí průměrnou hodnotu ze seznamu."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def plot_signal(values):
    """Vykreslí čárový graf signálu."""
    plt.figure(figsize=(10, 4))
    plt.plot(values, color='red', linewidth=0.8)
    plt.title("Vizualizace EKG signálu")
    plt.xlabel("Vzorek")
    plt.ylabel("Amplituda")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()


# TESTOVACÍ BLOK
if __name__ == "__main__":
    print("--- Spuštěno přímo jako modul signal_plot_ops.py ---")
    file_path = "ekg_signal.txt"
    data = load_signal_from_txt(file_path)

    if data:
        print(f"Minimum: {signal_min(data)}")
        print(f"Maximum: {signal_max(data)}")
        print(f"Průměr:  {signal_avg(data):.4f}")
        plot_signal(data)