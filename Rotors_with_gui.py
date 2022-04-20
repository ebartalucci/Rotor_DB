#from logging import root
#from ossaudiodev import control_labels
#from re import T
from logging import PlaceHolder
from tkinter import *
from PIL import ImageTk,Image
import sqlite3 # here i switch to sqlite3 instead of mysql, less robust but works faster

# GUI root for Tkinter
root = Tk()
root.title('ssNMR Lab: Rotor Database')
root.geometry("400x600")
#root.iconbitmap('-here insert path to logo-') #here insert group logo


##### DATABASE SECTION ####

# Create a database or try to connect to existing (our existing database is 'rotor_database.db')
connection = sqlite3.connect('rotor_database.db')

# Create cursor
cursor = connection.cursor()

# Create rotors table in database and specify columns type (NEEDS TO BE RAN ONLY ONCE!!!)
# cursor.execute("""CREATE TABLE rotors (
#                 rotor_id text,
#                 user text,
#                 rotor_type text,
#                 sample text,
#                 storage_t text,
#                 location text,
#                 filled_by text,
#                 filling_date text,
#                 empty text,
#                 additional_info text)
#                 """)

# Create function to delete record
def delete():
    # Create a database or connect to one
    connection = sqlite3.connect('rotor_database.db')
    # Create cursor
    cursor = connection.cursor()

    # Delete a record
    cursor.execute("DELETE from rotors_infos WHERE oid= " + delete_box.get())

    delete_box.delete(0, END)


    # Commit changes to database
    connection.commit()

    # Close database connection
    connection.close()



# Create Edit function to update a database
def edit():

    # Create a database or connect to one
    connection = sqlite3.connect('rotor_database.db')
    # Create cursor
    cursor = connection.cursor()

    record_id = delete_box.get()

    cursor.execute("""UPDATE rotors_infos SET
                rotor_id = :rotor_id,
                user = :user,
                rotor_type = :rotor_type,
                sample = :sample,
                storage_t = :storage_t,
                location = :location,
                filled_by = :filled_by,
                filling_date = :filling_date,
                empty = :empty,
                additional_info = :additional_info

                WHERE oid = :oid""",

                {
                'rotor_id': rotor_id_editor.get(),
                'user': user_editor.get(),
                'rotor_type': rotor_type_editor.get(),
                'sample': sample_editor.get(),
                'storage_t': storage_t_editor.get(),
                'location': location_editor.get(),
                'filled_by': filled_by_editor.get(),
                'filling_date': filling_date_editor.get(),
                'empty': empty_editor.get(),
                'additional_info': additional_info_editor.get(),

                'oid': record_id
                })

    # Commit changes to database
    connection.commit()

    # Close database connection
    connection.close()

    editor.destroy()


# Create function to update record
def update():
    
    # GUI root for Tkinter
    global editor
    editor = Tk()
    editor.title('ssNMR Lab: Update a Record')
    editor.geometry("400x400")
    #root.iconbitmap('-here insert path to logo-') #here insert group logo

    # Create a database or connect to one
    connection = sqlite3.connect('rotor_database.db')
    # Create cursor
    cursor = connection.cursor()

    record_id = delete_box.get()
    # Update the database
    cursor.execute("SELECT * FROM rotors_infos WHERE oid =  " + record_id) #original id will be entry 10
    records = cursor.fetchall()

    # Create a global variable
    global rotor_id_editor
    global user_editor
    global rotor_type_editor
    global sample_editor
    global storage_t_editor
    global location_editor
    global filled_by_editor
    global filling_date_editor
    global empty_editor
    global additional_info_editor


    # Create entry text boxes in GUI
    rotor_id_editor = Entry(editor, width=30)
    rotor_id_editor.grid(row=0, column=1, padx=20)
    user_editor = Entry(editor, width=30)
    user_editor.grid(row=1, column=1)
    rotor_type_editor = Entry(editor, width=30)
    rotor_type_editor.grid(row=2, column=1)
    sample_editor = Entry(editor, width=30)
    sample_editor.grid(row=3, column=1)
    storage_t_editor = Entry(editor, width=30)
    storage_t_editor.grid(row=4, column=1)
    location_editor = Entry(editor, width=30)
    location_editor.grid(row=5, column=1)
    filled_by_editor = Entry(editor, width=30)
    filled_by_editor.grid(row=6, column=1)
    filling_date_editor = Entry(editor, width=30)
    filling_date_editor.grid(row=7, column=1)
    empty_editor = Entry(editor, width=30)
    empty_editor.grid(row=8, column=1)
    additional_info_editor = Entry(editor, width=30)
    additional_info_editor.grid(row=9, column=1)

    # Create Text boxes labels
    rotor_id_label = Label(editor, text="Rotor ID")
    rotor_id_label.grid(row=0, column=0)
    user_label = Label(editor, text="User")
    user_label.grid(row=1, column=0)
    rotor_type_label = Label(editor, text="Rotor Size (mm)")
    rotor_type_label.grid(row=2, column=0)
    sample_label = Label(editor, text="Sample")
    sample_label.grid(row=3, column=0)
    storage_t_label = Label(editor, text="Storage T (K)")
    storage_t_label.grid(row=4, column=0)
    location_label = Label(editor, text="Location")
    location_label.grid(row=5, column=0)
    filled_by_label = Label(editor, text="Filled by")
    filled_by_label.grid(row=6, column=0)
    filling_date_label = Label(editor, text="Filling date")
    filling_date_label.grid(row=7, column=0)
    empty_label = Label(editor, text="Suitable to empty?")
    empty_label.grid(row=8, column=0)
    additional_info_label = Label(editor, text="Additional Information")
    additional_info_label.grid(row=9, column=0)

    # Loop through results
    for record in records:
        rotor_id_editor.insert(0, record[0])
        user_editor.insert(0, record[1])
        rotor_type_editor.insert(0, record[2])
        sample_editor.insert(0, record[3])
        storage_t_editor.insert(0, record[4])
        location_editor.insert(0, record[5])
        filled_by_editor.insert(0, record[6])
        filling_date_editor.insert(0, record[7])
        empty_editor.insert(0, record[8])
        additional_info_editor.insert(0, record[9])



    # Create Update button
    save_button = Button(editor, text="Save Edited Record", command=edit)
    save_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


    # Commit changes to database
    connection.commit()

    # Close database connection
    connection.close()


# Creat Submit function for database
def submit():
    # Create a database or connect to one
    connection = sqlite3.connect('rotor_database.db')
    # Create cursor
    cursor = connection.cursor()

    # Insert into table
    cursor.execute("INSERT INTO rotors_infos VALUES (:rotor_id, :user, :rotor_type, :sample, :storage_t, :location, :filled_by, :filling_date, :empty, :additional_info)",
                {
                    'rotor_id': rotor_id.get(),
                    'user': user.get(),
                    'rotor_type': rotor_type.get(),
                    'sample': sample.get(),
                    'storage_t': storage_t.get(),
                    'location': location.get(),
                    'filled_by': filled_by.get(),
                    'filling_date': filling_date.get(),
                    'empty': empty.get(),
                    'additional_info': additional_info.get()
                })

    # Commit changes to database
    connection.commit()

    # Close database connection
    connection.close()

    # Clear text boxes
    rotor_id.delete(0, END)
    user.delete(0, END)
    rotor_type.delete(0, END)
    sample.delete(0, END)
    storage_t.delete(0, END)
    location.delete(0, END)
    filled_by.delete(0, END)
    filling_date.delete(0, END)
    empty.delete(0, END)
    additional_info.delete(0, END)

# Create Query function
def query():
    # Create a database or connect to one
    connection = sqlite3.connect('rotor_database.db')
    # Create cursor
    cursor = connection.cursor()

    # Query the database
    cursor.execute("SELECT *, oid FROM rotors_infos") #original id will be entry 10
    records = cursor.fetchall()

    # Loop through the database to show records
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + " " + str(record[6]) + " " + str(record[7]) + " " + str(record[8]) + " " + str(record[9]) + "\t" + str(record[10]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=15, column=0, columnspan=2)

    # Commit changes to database
    connection.commit()

    # Close database connection
    connection.close()

# Create entry text boxes in GUI
rotor_id = Entry(root, width=30)
rotor_id.grid(row=0, column=1, padx=20)
user = Entry(root, width=30)
user.grid(row=1, column=1)
rotor_type = Entry(root, width=30)
rotor_type.grid(row=2, column=1)
sample = Entry(root, width=30)
sample.grid(row=3, column=1)
storage_t = Entry(root, width=30)
storage_t.grid(row=4, column=1)
location = Entry(root, width=30)
location.grid(row=5, column=1)
filled_by = Entry(root, width=30)
filled_by.grid(row=6, column=1)
filling_date = Entry(root, width=30)
filling_date.grid(row=7, column=1)
empty = Entry(root, width=30)
empty.grid(row=8, column=1)
additional_info = Entry(root, width=30)
additional_info.grid(row=9, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=12, column=1)

# Create Text boxes labels
rotor_id_label = Label(root, text="Rotor ID")
rotor_id_label.grid(row=0, column=0)
user_label = Label(root, text="User")
user_label.grid(row=1, column=0)
rotor_type_label = Label(root, text="Rotor Size (mm)")
rotor_type_label.grid(row=2, column=0)
sample_label = Label(root, text="Sample")
sample_label.grid(row=3, column=0)
storage_t_label = Label(root, text="Storage T (K)")
storage_t_label.grid(row=4, column=0)
location_label = Label(root, text="Location")
location_label.grid(row=5, column=0)
filled_by_label = Label(root, text="Filled by")
filled_by_label.grid(row=6, column=0)
filling_date_label = Label(root, text="Filling date")
filling_date_label.grid(row=7, column=0)
empty_label = Label(root, text="Suitable to empty?")
empty_label.grid(row=8, column=0)
additional_info_label = Label(root, text="Additional Information")
additional_info_label.grid(row=9, column=0)

delete_box_label = Label(root, text="Select ID Number")
delete_box_label.grid(row=12, column=0)



# Create Submit Button
submit_button = Button(root, text="Add Record to Rotor Database", command=submit)
submit_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query button
query_button = Button(root, text="Show Rotor Lists", command=query)
query_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create Delete button ### CREATE SUPERUSER PASSWORD ###
delete_button = Button(root, text="Delete Record from Rotor Database", command=delete)
delete_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

# Create Update button ###  ADD USER PASSWORD TO CHANGE ROTORS ###
update_button = Button(root, text="Update Record from Rotor Database", command=update)
update_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

# Commit changes to database
connection.commit()

# Close database connection
connection.close()



root.mainloop()