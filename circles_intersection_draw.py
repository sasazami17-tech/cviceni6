import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):
    """Vykreslí dvě kružnice do grafu."""
    fig, ax = plt.subplots()

    # Vytvoření objektů kružnic
    c1 = plt.Circle((circle_1['x'], circle_1['y']), circle_1['r'], fill=False, color="blue", label="Kružnice 1")
    c2 = plt.Circle((circle_2['x'], circle_2['y']), circle_2['r'], fill=False, color="red", label="Kružnice 2")

    ax.add_patch(c1)
    ax.add_patch(c2)

    # Automatické nastavení mezí grafu
    all_x = [circle_1['x'] + circle_1['r'], circle_1['x'] - circle_1['r'],
             circle_2['x'] + circle_2['r'], circle_2['x'] - circle_2['r']]
    all_y = [circle_1['y'] + circle_1['r'], circle_1['y'] - circle_1['r'],
             circle_2['y'] + circle_2['r'], circle_2['y'] - circle_2['r']]

    ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
    ax.set_ylim(min(all_y) - 1, max(all_y) + 1)

    ax.set_aspect("equal")
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.title("Vizualizace průniku kružnic")
    plt.show()