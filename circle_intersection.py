from circle_stats import has_intersection
from circles_intersection_draw import draw_data

def main():
    # Definice kružnic (změňte hodnoty pro testování různých případů)
    circle_a = {"x": 0, "y": 0, "r": 3}
    circle_b = {"x": 4, "y": 0, "r": 2}

    # Zjištění výsledku
    result = has_intersection(circle_a, circle_b)

    # Výpis do terminálu
    if result["is_intersection"]:
        print(f"Kružnice se protínají. Počet průniků: {result['intersections_count']}")
    else:
        print("Kružnice se neprotínají (jsou buď příliš daleko, nebo jedna v druhé).")

    # Vykreslení
    draw_data(circle_a, circle_b)

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt


plt.savefig("circle_graph.png")  # uloží graf do súboru
plt.show()  # potom otvorí okno s grafom