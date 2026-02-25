import psycopg2

host = "localhost"
user = "postgres"
password = "admin"
database = "py_test"

try:

    connection = psycopg2.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO employees (name)
        VALUES ('Jan Kowalski'), ('Anna Nowak');
    """)

    cursor.execute("""
        CREATE OR REPLACE FUNCTION count_employees()
        RETURNS INTEGER AS $$
        DECLARE
            emp_count INTEGER;
        BEGIN
            SELECT COUNT(*) INTO emp_count FROM employees;
            RETURN emp_count;
        END;

    $$ LANGUAGE plpgsql;
    """)

    cursor.callproc("count_employees")
    count = cursor.fetchone()[0]
    print(f"Liczba pracowników: {count}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
