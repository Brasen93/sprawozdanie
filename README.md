# 🖱️ Licznik Kliknięć (FastAPI + HTML)

Prosty projekt webowy, który zlicza kliknięcia przycisku. Backend został napisany w Pythonie przy użyciu FastAPI, a frontend to czysty HTML + JavaScript.

---

## 📁 Struktura projektu

```
.
├── main.py         # Backend FastAPI
├── index.html      # Prosty frontend
├── .gitignore      # Ignorowane pliki w repozytorium
├── README.md       # Ten plik
└── venv/           # Środowisko wirtualne Pythona
```

---

## 🚀 Jak uruchomić projekt lokalnie

### 1. Utwórz i aktywuj środowisko

#### 💻 Windows (Git Bash / PowerShell)

```bash
python -m venv venv
source venv/Scripts/activate    # Git Bash
# lub
venv\Scripts\activate           # CMD/PowerShell
```

#### 🐧 Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Zainstaluj zależności

```bash
pip install fastapi uvicorn
```

---

### 3. Uruchom backend FastAPI

```bash
uvicorn main:app --reload
```

Backend działa domyślnie pod adresem:  
http://127.0.0.1:8000

Dostępne endpointy:
- `GET /count` — zwraca aktualną wartość licznika
- `POST /click` — zwiększa licznik o 1

Dokumentacja Swagger:  
http://127.0.0.1:8000/docs

---

### 4. Uruchom frontend

Otwórz plik `index.html` w przeglądarce (dwuklik lub przeciągnięcie do okna przeglądarki).

---

## Przykładowe działanie

1. Otwórz backend pod adresem http://127.0.0.1:8000  
2. Otwórz `index.html` w przeglądarce  
3. Kliknij przycisk — licznik rośnie 

---

## Technologie

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **HTML + JavaScript**

---

## 🧑‍💻 Autor

Daria Krupińska  
[GitHub – Brasen93](https://github.com/Brasen93)