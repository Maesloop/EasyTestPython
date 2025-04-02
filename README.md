# EasyTestPython
Testing easy python object function
### Testovací scénáře pro manuální testování:

1. **Testování přidání položky**:
    - Přidejte platnou položku a ověřte, že se přidala správně
    - Pokuste se přidat položku s neplatným názvem (prázdný řetězec)
    - Pokuste se přidat položku s neplatnou cenou (záporné číslo)
    - Přidejte již existující položku a ověřte, že se zvýšilo množství
2. **Testování odebrání položky**:
    - Odeberte celou položku
    - Odeberte část množství položky
    - Pokuste se odebrat neexistující položku
3. **Testování slevových kódů**:
    - Aplikujte platný slevový kód "SLEVA10" a ověřte 10% slevu
    - Aplikujte platný slevový kód "SLEVA20" a ověřte 20% slevu
    - Pokuste se aplikovat neplatný slevový kód
4. **Testování výpočtu celkové ceny**:
    - Ověřte správný výpočet bez slevy
    - Ověřte správný výpočet se slevou
    - Ověřte správný výpočet po změně ceny položky

Odpovědi:
**Testování přidání položky**:
1. True
2. ValueError("Název položky musí být neprázdný řetězec")
3. ValueError: Cena musí být kladné číslo
4. True

**Testování odebrání položky**:
1. Full remove
2. +
3. Nothing happens, No error

**Testování slevových kódů**:
1. True
2. True
3. False

**Testování výpočtu celkové ceny**:
1. +
2. +
3. +
