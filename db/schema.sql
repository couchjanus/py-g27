DROP TABLE IF EXISTS roles;

CREATE TABLE roles (
    role_id INTEGER PRIMARY KEY,
    role TEXT
);

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    role_id INTEGER,
    FOREIGN KEY (role_id)
        REFERENCES roles (role_id)
);
