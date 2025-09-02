# 🏠 SafeHouse

**SafeHouse** je fiktivní pojišťovací aplikace vytvořená v Django.  
Slouží jako ukázkový projekt pro správu klientů a pojišťovacích produktů.

---

## ✨ Funkcionality

- **CRUD správa klientů**  
- **CRUD správa pojišťovacích produktů**  
- Zobrazení **detailů klientů** a jejich podepsaných smluv  
- Sekce **Smlouvy**:  
  - přehled všech podepsaných smluv  
  - zobrazení celkového **měsíčního inkasa pojišťovny**  
- Sekce **Historie**:  
  - záznam všech událostí v aplikaci  
  - vytvoření/úpravy/smazání klientů a smluv  
  - přiřazení smlouvy ke klientovi  

---

## 🚀 Jak projekt spustit

### 1. Klonování repozitáře
```bash
https://github.com/VaclavNekolny/SafeHouse.git
cd safehouse
```

### 2.Instalace
``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3.Spuštění
``` bash
python manage.py runserver
```

