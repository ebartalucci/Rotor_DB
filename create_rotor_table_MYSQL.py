import mysql.connector
from mysql.connector import Error

# Database
connection = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="Erotte.Mysql21",
                                    database="rotors")

# Create cursor
cursor = connection.cursor()

# Create rotors_infos Table in database and specify columns type (need to be done only once)
cursor.execute("""CREATE TABLE rotors_infos (
                rotor_id text,
                rotor_size text,
                sample text,
                storage_t text,
                lab_location text,
                filled_by text,
                filling_date text,
                entry_date text,
                new_rotor text,
                additional_info text)
                """)

# Commit changes
connection.commit()

# Close connection
connection.close()
