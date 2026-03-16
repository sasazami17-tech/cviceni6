import re


def analyze_password(
        password,
        min_length=8,
        require_digit=True,
        require_upper=True,
        require_symbol=False,
        banned_words=None
):
    """
    Analyzuje sílu hesla na základě zadaných kritérií.
    """
    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']

    symbols = "!@#$%^&*()-_=+[]{};:,.?"
    missing_rules = []
    active_rules_count = 0

    # 1. Kontrola délky
    active_rules_count += 1
    if len(password) < min_length:
        missing_rules.append("min_length")

    # 2. Kontrola číslice
    if require_digit:
        active_rules_count += 1
        if not any(char.isdigit() for char in password):
            missing_rules.append("digit")

    # 3. Kontrola velkého písmene
    if require_upper:
        active_rules_count += 1
        if not any(char.isupper() for char in password):
            missing_rules.append("upper")

    # 4. Kontrola symbolu
    if require_symbol:
        active_rules_count += 1
        if not any(char in symbols for char in password):
            missing_rules.append("symbol")

    # 5. Kontrola zakázaných slov
    active_rules_count += 1
    if any(word.lower() in password.lower() for word in banned_words):
        missing_rules.append("banned_word")

    # Výpočet výsledků
    failed_count = len(missing_rules)
    passed_count = active_rules_count - failed_count

    is_strong = failed_count == 0
    score_percent = int((passed_count / active_rules_count) * 100)

    return is_strong, score_percent, missing_rules


# --- TESTOVACÍ VOLÁNÍ ---

# 1. Čistě poziční argumenty
print(analyze_password("Psw1!", 8, True, True, True))
print(
    "Nevýhoda: Horší čitelnost. Není jasné, co znamenají hodnoty 8, True, True, True bez nahlédnutí do definice funkce.")
print("-" * 20)

# 2. Mix pozičních a pojmenovaných argumentů
print(analyze_password("BezpecneHeslo1", min_length=12, require_digit=True))
print(
    "Výhoda: Lepší srozumitelnost u konfiguračních parametrů. Heslo jako hlavní subjekt zůstává poziční, zbytek je jasně pojmenován.")
print("-" * 20)

# 3. Volání s vypnutým pravidlem pro symbol (použití pojmenovaného argumentu)
print(analyze_password("JenPismenaACisla123", require_symbol=False))
print(
    "Výhoda: Explicitně vidíme, které pravidlo vypínáme. Ostatní parametry využívají své výchozí hodnoty, což zkracuje zápis.")
print("-" * 20)

# 4. Volání s vlastním seznamem banned_words
print(analyze_password("Admin_2024", banned_words=["admin", "root", "prijmeni"]))
print(
    "Výhoda: Vysoká přehlednost. Při předávání složitějších struktur (seznamy) pojmenovaný argument jasně určuje účel dat.")






