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

## Deployment – GitHub Actions + AWS EC2

Aplikacja jest automatycznie wdrażana na instancję EC2 po każdym `push` do gałęzi `main`.

### Wymagania:
- Konto AWS
- Utworzona instancja EC2 (Ubuntu)
- Zainstalowany Docker i Git na EC2
- Skonfigurowane GitHub Secrets:
  - `EC2_HOST` – publiczny adres IP EC2
  - `EC2_USER` – np. `ubuntu`
  - `EC2_KEY` – zawartość klucza `.pem` (surowy tekst)

### Deployment automatyczny:
1. Zmiany commitowane i wypchnięte do `main`
2. GitHub Actions uruchamia workflow `deploy.yml`
3. Workflow:
   - Łączy się z EC2 przez SSH
   - Pobiera/zaktualizuje repozytorium
   - Buduje obraz Dockera
   - Uruchamia kontener z aplikacją

Po kilku sekundach aplikacja będzie dostępna na `http://<EC2_IP>`.

## GitHub Actions – Workflow

### Plik: `.github/workflows/deploy.yml`

#### Trigger:
- Automatyczne uruchomienie przy pushu do `main`

#### Kroki workflowa:
1. **Checkout repozytorium**
2. **Zapisanie klucza SSH** (z secretu `EC2_KEY`)
3. **Połączenie z EC2 przez SSH**
   - Instalacja Dockera i Gita (jeśli brak)
   - Klonowanie/pull repozytorium
   - Budowa obrazu Dockera
   - Uruchomienie kontenera na porcie 80

#### Przykład:
```yaml
on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      ...


## 🧑‍💻 Autor

Daria Krupińska  
[GitHub – Brasen93](https://github.com/Brasen93)