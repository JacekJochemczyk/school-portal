# 🏫 School Portal — Portal rekrutacyjny dla szkół niepublicznych

## 📜 Opis projektu

Projekt **School Portal** to system rekrutacyjny online, który umożliwia uczniom łatwe zapisywanie się do wybranych szkół niepublicznych. Celem aplikacji jest stworzenie przejrzystego i bezpiecznego środowiska, w którym:
- 🏫 Szkoły mogą prezentować swoją ofertę edukacyjną,  
- 👩‍🎓 Uczniowie mogą przeglądać dostępne placówki i wysyłać zgłoszenia online,  
- 👨‍💻 Administratorzy mogą zarządzać zgłoszeniami i danymi w jednym miejscu.

System powstaje w oparciu o:
- **Django** — backend i logika aplikacji,  
- **PostgreSQL** — relacyjna baza danych,  
- **Docker + Docker Compose** — konteneryzacja i powtarzalne środowisko,  
- **WSL2 + VS Code** — wygodne środowisko developerskie pod Windows.

 ---

## 🧰 Technologie i narzędzia

- 🐍 Python 3.14
- 🐳 Docker & Docker Compose
- 🐘 PostgreSQL 15
- 🌐 Django 5.2
- 🐧 WSL2 (Ubuntu)
- 💻 Visual Studio Code (Remote WSL)
- 🧭 Git

---

## 📂 Struktura projektu
school-portal/
│── backend/ # Kod źródłowy aplikacji Django

│── db/ # Wolumen danych Postgresa (trwałe dane)

│── db-init/ # Skrypty inicjalizujące bazę danych

│── .env # Zmienne środowiskowe 

│── .gitignore # Plik ignorujący śmieci i sekrety

│── docker-compose.yml # Definicja kontenerów

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
POSTGRES_USER=pgadmin_local
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

### 🌐 8. Uruchomienie środowiska

Polecenie:

`docker compose up backend`

uruchomiło:

kontener bazy danych,

kontener backendu,

migracje Django,

serwer developerski na porcie 8000.

W przeglądarce pojawił się komunikat:

Instalacja przebiegła pomyślnie! Gratulacje!

👉 To potwierdziło, że backend i baza danych są poprawnie spięte.

---

### 🧰 9. Konfiguracja środowiska developerskiego (VS Code + WSL)

Pojawiły się typowe problemy:

❌ \\wsl$ niedostępny z Eksploratora Windows,

❌ VS Code zamykał się przy starcie,

✅ rozwiązania:

restart WSL (wsl --shutdown),

czyszczenie cache serwera VS Code (rm -rf ~/.vscode-server),

ponowne uruchomienie code ..

Dzięki temu:

projekt działa teraz w trybie WSL,

edycja kodu odbywa się w VS Code z dostępem do terminala, lintera, debuggera i Docker Extension.

---

### 🧭 Aktualny stan projektu

✅ Działa:

Docker + Postgres + Django w jednym środowisku,

automatyczna konfiguracja bazy i backendu,

migracje Django,

dostęp do aplikacji przez przeglądarkę,

środowisko programistyczne VS Code w WSL2.

### 🧭 Planowane kolejne kroki

Stworzenie aplikacji schools z modelami bazy danych,

Utworzenie widoków i formularzy dla uczniów,

Panel administracyjny dla szkół,

Rejestracja i logowanie użytkowników,

Frontend React / Vue (osobny kontener),

Wdrożenie na serwer

--- 

### 👨‍💻 Autorzy

Twórcy projektu: Jacek Jochemczyk, Michał Gandyk
