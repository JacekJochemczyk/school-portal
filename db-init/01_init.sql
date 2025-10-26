-- 1. Utworzenie użytkownika, jeśli nie istnieje
DO
$$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_roles WHERE rolname = 'schoolapp'
    ) THEN
        EXECUTE 'CREATE ROLE (loginapp) LOGIN PASSWORD ''TwojeHasloApp''';
    END IF;
END
$$;

-- 2. Utworzenie bazy danych, jeśli nie istnieje
CREATE DATABASE schooldb OWNER schoolapp
    TEMPLATE template0
    ENCODING 'UTF8'
    LC_COLLATE='en_US.utf8'
    LC_CTYPE='en_US.utf8'
    CONNECTION LIMIT = -1;

-- UWAGA: CREATE DATABASE nie może być wewnątrz DO $$ $$ — musi być na zewnątrz.
