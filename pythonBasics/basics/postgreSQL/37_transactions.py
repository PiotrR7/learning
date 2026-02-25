import psycopg2

host = "localhost"
user = "postgres"
password = "admin"
database = "py_test"

try:

    connection = psycopg2.connect(host = host, user = user, password = password, database = database)

    connection.autocommit = False

    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS employees;
        DROP TABLE IF EXISTS departments;
        CREATE TABLE departments (
            department_id SERIAL PRIMARY KEY,
            department_name VARCHAR(255) NOT NULL,
        );
    """)

    cursor.execute("""
        CREATE TABLE employees
        (
            employee_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            department_id INTEGER NOT NULL,
        );
    """)

    cursor.execute("""
        INSERT INTO departments (department_name)
            VALUES ('HR'), ('Development'), ('Marketing'); 
    """)

    cursor.execute("""
        INSERT INTO employees (first_name, last_name, department_id)
            VALUES ('Tomasz', 'Nowak', 2);
    """)
    cursor.execute("""
        UPDATE departments SET department_name = 'IT' WHERE department_id = 2;
    """)

    connection.commit()
    print("Transakcja przebiegła pomyślnie.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
