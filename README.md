# Projekt: Průnik kružnic

## Popis projektu
Cílem tohoto projektu bylo vytvořit program, který zjistí, zda se dvě kružnice protínají a kolik mají průniků. Program také umožňuje vizualizaci kružnic v grafu.

V rámci úkolu jsme:

1. **Vytvořili modul `circle_stats.py`**  
   - Funkce `radius_sum(r1, r2)` – vypočítá součet poloměrů dvou kružnic.  
   - Funkce `euclid_distance(x1, y1, x2, y2)` – spočítá vzdálenost mezi dvěma středy kružnic.  
   - Funkce `has_intersection(circle_1, circle_2)` – zjistí, zda se kružnice protínají a vrátí slovník s informací o počtu průniků.

2. **Testovali funkce**  
   - Navrhli jsme 5 testovacích případů pro `has_intersection`:
     - 2 běžné případy (dva průniky a jeden průnik).  
     - 2 hraniční případy (dotyk uvnitř a kružnice uvnitř druhé).  
     - 1 negativní případ (kružnice se neprotínají).  
   - Přidali jsme 1 test pro `radius_sum`, abychom ověřili správnost součtu poloměrů.  
   - Testy nám pomáhají rychle zjistit, zda funkce fungují správně a zda se nezměnila logika výpočtů.

3. **Vytvořili modul `circles_intersection_draw.py`**  
   - Funkce `draw_data(circle_1, circle_2)` vykresluje obě kružnice do grafu pomocí knihovny `matplotlib`.  
   - Graf vizualizuje, jak kružnice spolu interagují: zda se dotýkají, mají dva průniky nebo jsou od sebe vzdálené.

4. **Napsali hlavní skript `circle_intersection.py`**  
   - Naimportovali funkci `has_intersection` a `draw_data`.  
   - Definovali dvě kružnice jako slovníky s klíči `x`, `y` a `r`.  
   - Zavolali funkci `has_intersection` a podle výsledku vypisovali, zda se kružnice protínají a kolik mají průniků.  
   - Zavolali funkci `draw_data`, která otevřela grafické okno s vizualizací kružnic.

5. **Vizualizace grafu**  
   - Modrá kružnice = první kružnice.  
   - Červená kružnice = druhá kružnice.  
   - Pokud se kružnice dotýkají, vidíme pouze jeden bod průniku.  
   - Pokud mají dva průniky, kruhy se překrývají.  
   - Pokud se neprotínají, kruhy jsou od sebe vzdálené.

6. **Postup práce**  
   - Nejprve jsme vytvořili funkce pro výpočty (součet poloměrů a vzdálenost).  
   - Otestovali jsme funkce s několika jednoduchými hodnotami.  
   - Poté jsme napsali funkci `has_intersection`, která rozhoduje o průniku kružnic.  
   - Nakonec jsme přidali kreslení kružnic pro vizualizaci a ověřili, že graf odpovídá výpočtům.

---

