-- UWAGA: tutaj wpisujemy wartości bezpośrednio, bo Docker init nie rozumie zmiennych środowiskowych

DO
$$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_roles WHERE rolname = 'schoolapp'
    ) THEN
        EXECUTE 'CREATE ROLE schoolapp LOGIN PASSWORD ''KarmazynowyKufel%''';
    END IF;
END
$$;

DO
$$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_database WHERE datname = 'schooldb'
    ) THEN
        EXECUTE 'CREATE DATABASE schooldb OWNER schoolapp';
    END IF;
END
$$;

ALTER DATABASE schooldb OWNER TO schoolapp;

