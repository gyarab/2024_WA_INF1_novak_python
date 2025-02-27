# 🎮 Game Database

Game Database je webová aplikace vytvořená v Django, která umožňuje uživatelům procházet databázi videoher, přidávat nové hry, upravovat je a mazat. Uživatelé se mohou zaregistrovat, přihlásit a spravovat svůj profil.

## 🛠 Použité technologie

- **Backend:** Django
- **Frontend:** Bootstrap 5 a HTML
- **Databáze:** SQLite
- **Autentizace:** Django Auth
- **Další knihovny:** Pillow (práce s obrázky)

---

## 🗂 Modely a vztahy

### **Game (Hra)**

Reprezentuje jednu hru v databázi. Obsahuje informace jako název, popis, datum vydání, cenu a obrázek.

**Atributy:**

- `name` – název hry
- `description` – krátký popis
- `release_date` – datum vydání
- `price` – cena hry (0 = zdarma)
- `image` – obrázek hry
- `publisher` – vztah k modelu User (vlastník hry)

**Vztahy:**

- Každá hra má **jednoho vydavatele** (`publisher` jako `ForeignKey` na `User`)
- Každý uživatel může být **vydavatelem více her**
- Každá hra může mít **libovolný počet recenzí**

### **Category (Kategorie)**

Kategorie, do kterých mohou být hry zařazeny.

**Atributy:**

- `name` – název kategorie

**Vztahy:**

- Každá kategorie může obsahovat **libovolný počet her**
- Každá hra může být zařazena **do více kategorií**

### **Platform (Platforma)**

Platforma, na které je hra dostupná.

**Atributy:**

- `name` – název platformy

**Vztahy:**

- Každá platforma může obsahovat **libovolný počet her**
- Každá hra může být dostupná **na více platformách**

### **User (Uživatel)**

Uživatelé aplikace, kteří mohou přidávat a spravovat své hry.

**Atributy:**

- `username` – uživatelské jméno
- `email` – e-mailová adresa
- `profile_picture` – profilový obrázek (volitelný)

**Vztahy:**

- Každý uživatel může přidat **libovolný počet her**
- Používá se Django vestavěný model `User`
- Každý uživatel může napsat **libovolný počet recenzí**

### **GameReview (Recenze hry)**

Uživatelé mohou psát recenze k jednotlivým hrám. Každá recenze obsahuje hodnocení a textový popis.

**Atributy:**

- `game` – vztah k modelu Game (recenzovaná hra)
- `author` – vztah k modelu User (autor recenze)
- `rating` – hodnocení hry (1–5)
- `text` – textový popis recenze

**Vztahy:**

- Každá recenze patří **jedné hře** (`game` jako `ForeignKey` na `Game`)
- Každá recenze je **napsána jedním uživatelem** (`author` jako `ForeignKey` na `User`)

---

## 🏁 Instalace a spuštění

1. **Naklonování repozitáře:**
   ```sh
   git clone https://github.com/gyarab/2024_WA_INF1_novak_python.git
   cd 2024_WA_INF1_novak_python
   ```
2. **Vytvoření a aktivace virtuálního prostředí:**
   ```sh
    python -m venv <name>
    .\<name>\Scripts\activate // Windows
    source <name>/bin/activate // Linux
   ```
3. **Instalace závislostí:**
   ```sh
    python -m pip install -r requirements.txt
   ```
4. **Migrace databáze:**
   ```sh
    python manage.py migrate
   ```
5. **Načítání fixtur**
   ```sh
     python manage.py loaddata fixtures/users.json
     python manage.py loaddata fixtures/games.json
     python manage.py loaddata fixtures/reviews.json
   ```
   > Na pořadí načítání záleží, protože některé fixtury mohou záviset na jiných datech.
6. **Spuštění aplikace:**
   ```sh
     python manage.py runserver
   ```
