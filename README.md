# 🏫 School Portal — Portal rekrutacyjny dla szkół niepublicznych

## 📜 Opis projektu

Projekt **School Portal** to system rekrutacyjny online, który umożliwia uczniom łatwe zapisywanie się do wybranych szkół niepublicznych. Celem aplikacji jest stworzenie przejrzystego i bezpiecznego środowiska, w którym:
- 🏫 Szkoły mogą prezentować swoją ofertę edukacyjną,  
- 👩‍🎓 Uczniowie mogą przeglądać dostępne placówki i wysyłać zgłoszenia online,  
- 👨‍💻 Administratorzy mogą zarządzać zgłoszeniami i danymi w jednym miejscu.

System powstaje w oparciu o:
- **Django** — backend i logika aplikacji,
- **Django REST Framework (DRF)** - interfejs API,
- **SimpleJWT** - uwierzytelnianie tokenami,
- **PostgreSQL** — relacyjna baza danych,  
- **Docker + Docker Compose** — konteneryzacja i powtarzalne środowisko,  
- **WSL2 + VS Code** — wygodne środowisko developerskie pod Windows.

 ---

## 🧰 Technologie i narzędzia

- 🐍 Python 3.14
- 🐳 Docker & Docker Compose
- 🐘 PostgreSQL 15
- 🌐 Django 5.2
- ⚙️ Django REST Framework
- 🔐 SimpleJWT
- 🐧 WSL2 (Ubuntu)
- 💻 Visual Studio Code (Remote WSL)
- 🧭 Git

---

## 📁 Struktura projektu

```

SCHOOL-PORTAL/
├── backend/ # Główna aplikacja backendowa (Django)
│ ├── accounts/ # Moduł kont użytkowników
│ │ ├── migrations/ # Migracje bazy danych
│ │ ├── admin.py # Rejestracja modeli w panelu admina
│ │ ├── apps.py # Konfiguracja aplikacji
│ │ ├── auth.py # Logika autoryzacji / JWT
│ │ ├── models.py # Modele użytkowników (Student, School)
│ │ ├── serializers.py # Serializery dla API
│ │ ├── views_api.py # Widoki API dla użytkowników
│ │ └── views.py # Widoki klasyczne 
│ │
│ ├── portal/ # Główna aplikacja portalu
│ │ ├── api_views.py # Widoki API (endpointy)
│ │ ├── settings.py # Ustawienia Django
│ │ ├── urls.py # Główne trasy aplikacji
│ │ ├── asgi.py # ASGI config
│ │ └── wsgi.py # WSGI config
│ │
│ ├── manage.py # Główny plik do zarządzania Django
│ ├── Dockerfile # Definicja obrazu Docker
│ ├── requirements.txt # Lista zależności Pythona
│ └── .env.example # Przykładowy plik środowiskowy
│
├── db/ # Pliki SQL / inicjalizacja bazy
│ └── 01_init.sql
│
├── docker-compose.yml # Konfiguracja usług Docker
├── .env # Plik środowiskowy (lokalny)
└── README.md # Dokumentacja projektu

```

## 🚀 Etapy budowy projektu (KROK PO KROKU)

### 🧭 1. Przygotowanie środowiska

Zainstalowaliśmy:
- Git (kontrola wersji),
- Python 3.14,
- Docker i Docker Compose,
- WSL2 z Ubuntu jako środowisko developerskie (Linux w Windows),
- Node.js (planowany do frontendu w dalszych etapach).

👉 Dzięki temu mamy powtarzalne środowisko, które działa tak samo u każdego członka zespołu.

---

### 🐳 2. Inicjalizacja projektu

- Utworzyliśmy katalog `school-portal`.
- Dodaliśmy foldery:
  - `backend` (kod aplikacji),
  - `db` (dane Postgresa),
  - `db-init` (skrypty SQL),
- Utworzyliśmy `.env` i `.gitignore`.

👉 Taka struktura od początku daje porządek i przewidywalność rozwoju projektu.

---

### 🔐 3. Plik `.env`

W `.env` umieściliśmy:
```env
POSTGRES_USER=...
POSTGRES_PASSWORD=...
APP_DB=schooldb
APP_DB_USER=...
APP_DB_PASSWORD=...
DJANGO_SECRET_KEY=...
DJANGO_DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1
```

👉 Sekrety i hasła są poza repozytorium, co poprawia bezpieczeństwo i ułatwia zmianę środowiska (np. DEV → PROD).

---

### 🐘 4. Konfiguracja docker-compose.yml

Dodaliśmy dwie usługi:

db — Postgres + skrypty inicjalizacyjne,

backend — aplikacja Django.

Ustawiliśmy:

wolumeny,

zmienne środowiskowe,

healthcheck,

mapowanie portów.

👉 Dzięki temu jednym poleceniem docker compose up uruchamiamy cały stack aplikacji.

---

### 🧱 5. Skrypt inicjalizacyjny bazy

W pliku db-init/01_init.sql dodaliśmy:

tworzenie użytkownika schoolapp,

tworzenie bazy danych schooldb,

nadanie uprawnień.

👉 Eliminuje to ręczne tworzenie bazy — środowisko konfiguruje się samo.

---

### 🐍 6. Utworzenie projektu Django

W kontenerze backendu uruchomiliśmy:

`docker compose run --rm backend bash -lc "django-admin startproject portal ."`

W folderze backend pojawiły się:

manage.py,

folder portal z plikami konfiguracyjnymi Django.

👉 To punkt wyjścia dla dalszej rozbudowy aplikacji.

---

### ⚙️ 7. Konfiguracja Django i Postgresa

W portal/settings.py:

podmieniliśmy SQLite na PostgreSQL,

użyliśmy zmiennych środowiskowych z .env.

👉 Dzięki temu backend korzysta z tej samej bazy co kontener Postgres — działa od razu po uruchomieniu.

---
### 🔐 7. Aplikacja „accounts” – model użytkownika

Dodano aplikację accounts zawierającą:

model User z polami username, user_type (student/school) i is_approved,

migracje,

rejestrację w INSTALLED_APPS.
---

### 🌐 8. Django REST Framework + JWT

Zainstalowano:

djangorestframework
djangorestframework-simplejwt

W settings.py dodano konfigurację REST i SimpleJWT.

Dodano:

accounts/serializers.py — rejestracja użytkownika (walidacja haseł, logika tworzenia konta szkoły),

accounts/views_api.py — endpointy /api/register/, /api/me/,

accounts/auth.py — logowanie JWT z blokadą niezatwierdzonych szkół,

aktualizację portal/urls.py z trasami REST API.
---
### ✅ 9. Działające endpointy API
|  Metoda  | Endpoint              | Opis                                            | Uwagi         |
| :------: | :-------------------- | :---------------------------------------------- | :------------ |
| **POST** | `/api/register/`      | Rejestracja nowego użytkownika (student/school) | —             |
| **POST** | `/api/login/`         | Logowanie — zwraca JWT (`access`, `refresh`)    | —             |
| **POST** | `/api/token/refresh/` | Odświeżanie tokena JWT                          | —             |
|  **GET** | `/api/me/`            | Zwraca dane zalogowanego użytkownika            | Wymaga tokena |
|  **GET** | `/api/ping/`          | Testowy endpoint (sprawdzenie API)              | —             |


✅ Dodatkowo:

Szkoła niezatwierdzona nie może się zalogować (401 + komunikat),

Student loguje się normalnie,

/api/me/ działa tylko z nagłówkiem Authorization: Bearer <token>.

---

### 🧰 10. Konfiguracja środowiska developerskiego (VS Code + WSL2)

Rozwiązano typowe problemy z WSL i VS Code:

restart WSL (wsl --shutdown),

czyszczenie cache (rm -rf ~/.vscode-server),

poprawne mapowanie folderów projektu w kontenerze.
---

### 🧭 Aktualny stan projektu (listopad 2025)

✅ Działa w pełni:

Docker + PostgreSQL + Django w jednym środowisku,

REST API z rejestracją i logowaniem JWT,

weryfikacja kont szkół przez admina,

poprawne migracje i konfiguracja bazy,

stabilne środowisko developerskie w WSL2 + VS Code.

🧭 Kolejne kroki

Stworzenie aplikacji schools – modele dla szkół i ofert edukacyjnych,

Panel admina – zatwierdzanie szkół i przegląd kont,

Formularze uczniów – wybór szkoły i składanie zgłoszenia,

Frontend (React/Next.js) – logowanie, dashboard, przegląd ofert,

Wdrożenie – przygotowanie środowiska produkcyjnego (Docker + Nginx + SSL).
--- 

### 👨‍💻 Autorzy

Twórcy projektu: Jacek Jochemczyk, Michał Gandyk
