"""this file contains the insert query into countries db"""

import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="students")
    cursor = connection.cursor()
    """create tables here"""
    create_table_query = '''CREATE TABLE countries
                 (countryCode INT PRIMARY KEY  NOT NULL,
                 name  VARCHAR(255) NOT NULL,
                 states json); '''

    cursor.execute(create_table_query)
    connection.commit()
    """insert data into tables here"""
    insert_cities ='''INSERT INTO countries(countryCode, name, states) VALUES ('91','india','[{"name": "Kerala", "cities": [{"name": "Thrissur", "code": "680111"}, {"name": "kochi", "code": "680222"}, {"name": "trivandrum", "code": "680333"}]}, {"name": "TamilNadu", "cities": [{"name": "Chennai", "code": "380111"}, {"name": "Coimbatore", "code": "380222"}]}]'

    );'''
    cursor.execute(create_table_query,insert_cities)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into countries table")

except (Exception, psycopg2.Error) as error:
    if connection:
        print("Failed to insert record into countries table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")