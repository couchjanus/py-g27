from msilib.schema import Error
import sqlite3 as lite

# print(lite.version)
# print(lite.sqlite_version)
# print(lite.sqlite_version_info)

# conn = lite.connect('mtdb.db')
# cur = conn.cursor()
# print(cur)
# cur.close()
# conn.close()


schema = 'schema.sql'
DB = 'mtdb.db'

# with lite.connect(DB) as conn:
#     print('Creating schema')
#     with open(schema, 'rt') as f:
#         s = f.read()
#     conn.executescript(s)
    
#     print('Schema created succesfully')

def connection(db):
    conn = None
    try: conn = lite.connect(db)
    except lite.Error as e: print(e)
    return conn

def create_role(conn, role):
    sql = "INSERT INTO roles(role) VALUES(?)"
    cur = conn.cursor()
    cur.execute(sql, role)
    conn.commit()
    return cur.lastrowid

def create_employee(conn, employee):
    sql = "INSERT INTO employees(first_name, last_name, role_id) VALUES(?, ?, ?)"
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    return cur.lastrowid

def all_employees(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def get_employees(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE role_id=?", (id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
       
def update_employee(conn, employee):
    sql = '''UPDATE employees 
    SET last_name = ?
    WHERE employee_id = ?
    '''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()

def delete_employee(conn, id):
    sql = "DELETE FROM employees WHERE employee_id=?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def delete_all(conn):
    sql = "DELETE FROM employees"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def get_emp(conn, id):
    sql = '''
    SELECT employees.*, role FROM employees
    LEFT JOIN roles ON
    roles.role_id = employees.role_id
    WHERE employee_id=?
    '''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    
    row = cur.fetchone()
    print(row)


def main():
    conn = connection(DB)
    
    with conn:
        # id = create_role(conn, ('manager',))
        # emp = ('Mary', 'Poppins', id)
        # create_employee(conn, emp)
        # id = create_role(conn, ('secretary',))
        # emp = ('John', 'Smith', id)
        # create_employee(conn, emp)
        # id = create_role(conn, ('sales',))
        # emp = ('Kevin', 'Bacon', id)
        # create_employee(conn, emp)
        # id = create_role(conn, ('factory',))
        # emp = ('Jane', 'Doe', id)
        # create_employee(conn, emp)
        
        all_employees(conn)
        # get_employees(conn, 4)
        
        # update_employee(conn, ('Gooru', 4))
        # delete_employee(conn, 5)
        
        # all_employees(conn)
        get_emp(conn, 2)
        
if __name__ == '__main__':
    main()