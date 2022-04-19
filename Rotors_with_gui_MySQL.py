#from logging import root
#from ossaudiodev import control_labels
#from re import T
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
from mysql.connector import Error

# GUI root
root = Tk()
root.title('Wiegand Lab: Rotor Database')
#root.iconbitmap('-here insert path to logo-')
root.geometry("400x400")

##### DATABASE SECTION ####
# Create a database or try to connect to existing (our existing database is 'rotors')
try:
    connection = mysql.connector.connect( host="localhost",
                                          user="root",
                                          password="Erotte.Mysql21",
                                          database="rotors")
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        # Create cursor
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

# Creat Submit function for database
def submit():
    # Create a database or connect to one
    connection = mysql.connector.connect( host="localhost",
                                          user="root",
                                          password="Erotte.Mysql21",
                                          database="rotors")
    # Create cursor
    cursor = connection.cursor()

    # Insert into table
    cursor.execute("INSERT INTO rotors_infos VALUES (rotor_id, rotor_size, sample, storage_t, lab_location, filled_by, filling_date, entry_date, new_rotor, additional_info)",
                {
                    'rotor_id': rotor_id.get(),
                    'rotor_size': rotor_size.get(),
                    'sample': sample.get(),
                    'storage_t': storage_t.get(),
                    'lab_location': lab_location.get(),
                    'filled_by': filled_by.get(),
                    'filling_date': filling_date.get(),
                    'entry_date': entry_date.get(),
                    'new_rotor': new_rotor.get(),
                    'additional_info': additional_info.get()
                })

    # Commit changes to database
    connection.commit()

    # Close database connection
    connection.close()

    # Clear text boxes
    rotor_id.delete(0, END)
    rotor_size.delete(0, END)
    sample.delete(0, END)
    storage_t.delete(0, END)
    lab_location.delete(0, END)
    filled_by.delete(0, END)
    filling_date.delete(0, END)
    entry_date.delete(0, END)
    new_rotor.delete(0, END)
    additional_info.delete(0, END)

# Create Query function
def query():
    # Create a database or connect to one
    connection = mysql.connector.connect( host="localhost",
                                          user="root",
                                          password="Erotte.Mysql21",
                                          database="rotors")
    # Create cursor
    cursor = connection.cursor()

    # Query the database
    cursor.execute("SELECT * FROM rotors_infos")
    records = cursor.fetchall()

    # Loop through the database to show records
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + " " + str(record[6]) + " " + str(record[7]) + " " + str(record[8]) + " " + str(record[9]) +  "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes to database
    connection.commit()

    # Close database connection
    connection.close()

# Create entry text boxes in GUI
rotor_id = Entry(root, width=30)
rotor_id.grid(row=0, column=1, padx=20)
rotor_size = Entry(root, width=30)
rotor_size.grid(row=1, column=1)
sample = Entry(root, width=30)
sample.grid(row=2, column=1)
storage_t = Entry(root, width=30)
storage_t.grid(row=3, column=1)
lab_location = Entry(root, width=30)
lab_location.grid(row=4, column=1)
filled_by = Entry(root, width=30)
filled_by.grid(row=5, column=1)
filling_date = Entry(root, width=30)
filling_date.grid(row=6, column=1)
entry_date = Entry(root, width=30)
entry_date.grid(row=7, column=1)
new_rotor = Entry(root, width=30)
new_rotor.grid(row=8, column=1)
additional_info = Entry(root, width=30)
additional_info.grid(row=9, column=1)

# Create Text boxes labels
rotor_id_label = Label(root, text="Rotor ID")
rotor_id_label.grid(row=0, column=0)
rotor_size_label = Label(root, text="Rotor Size (mm)")
rotor_size_label.grid(row=1, column=0)
sample_label = Label(root, text="Sample")
sample_label.grid(row=2, column=0)
storage_t_label = Label(root, text="Storage T (K)")
storage_t_label.grid(row=3, column=0)
lab_location_label = Label(root, text="Lab Location")
lab_location_label.grid(row=4, column=0)
filled_by_label = Label(root, text="Filled by")
filled_by_label.grid(row=5, column=0)
filling_date_label = Label(root, text="Filling date")
filling_date_label.grid(row=6, column=0)
entry_date_label = Label(root, text="Entry date")
entry_date_label.grid(row=7, column=0)
new_rotor_label = Label(root, text="New Rotor?")
new_rotor_label.grid(row=8, column=0)
additional_info_label = Label(root, text="Additional Information")
additional_info_label.grid(row=9, column=0)


# Create Submit Button
submit_button = Button(root, text="Add Record to Rotor Database", command=submit)
submit_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query button
query_button = Button(root, text="Show Rotors List", command=query)
query_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Commit changes to database
connection.commit()

# Close database connection
connection.close()











root.mainloop()
