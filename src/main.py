# MySQL Database GUI
# Leo Martinez III
# Data used: 'cbm005.txt'
# MySQL Import: 'self_contained_SQL_Export.sql'

# Necessary Imports (Needs to be installed in virtual environment)
import mysql.connector
from tkinter import Tk, Label, Entry, Button, StringVar, ttk, Scrollbar, END, messagebox

class DatabaseGUI:
    
    # Intialization Code
    def __init__(self, root):
        self.root = root
        root.title("MySQL Database GUI")
        self.connect_to_db()
        
        # Fetch and store every records
        self.fetch_original_records()
    
        # Create Labels and Entry Fields
        self.create_data_entry_widgets()
        self.create_search_widgets()
        self.create_treeview()
        
        # Set the initial size of the window
        root.geometry("1300x500")
    
    # Used to connect Python to the MySQL Database
    # Make sure you the password is entered before running the code or an authentication error will appear!
    def connect_to_db(self):
        self.db = mysql.connector.connect( # During testing, MySQL Workbench was used
            host="127.0.0.1",
            user="root",
            password="", # Enter your password here <-----------
            database="cbm005_database" # Enter your database name here
        )

    # This method is used for creating both the labels and entries for the GUI
    # Additionally, it is also used for placing them in a specific areas of the GUI
    def create_data_entry_widgets(self):
        
        # Set Width for Labels as needed
        label_width = 10
        # Set Width for Buttons as needed
        button_width = 14
        
        # Labels
        self.label_recordCode = Label(self.root, text="Record Code:")
        self.label_institutionCode = Label(self.root, text="Institution Code:")
        self.label_subject = Label(self.root, text="Subject:")
        self.label_courseNumber = Label(self.root, text="Course Number:")
        self.label_sectionNumber = Label(self.root, text="Section Number:")
        self.label_building = Label(self.root, text="Building:")
        
        self.label_room = Label(self.root, text="Room:")
        self.label_daysOfWeek = Label(self.root, text="Days of Week:")
        self.label_startTime = Label(self.root, text="Start Time:")
        self.label_duration = Label(self.root, text="Duration:")
        self.label_semesterCredit = Label(self.root, text="Semester Credit:")
        self.label_year = Label(self.root, text="Year:")
        
        self.label_instructionType = Label(self.root, text="Room Type:")
        self.label_item15 = Label(self.root, text="Enrollment A:", width=label_width)
        self.label_item16 = Label(self.root, text="Enrollment B:", width=label_width)
        self.label_item17 = Label(self.root, text="Enrollment C:", width=label_width)
        self.label_item18 = Label(self.root, text="Enrollment D:", width=label_width)
        self.label_item19 = Label(self.root, text="Enrollment E:", width=label_width)
        
        # Entries
        self.entry_recordCode = Entry(self.root)
        self.entry_instituitionCode = Entry(self.root)
        self.entry_subject = Entry(self.root)
        self.entry_courseNumber = Entry(self.root)
        self.entry_sectionNumber = Entry(self.root)
        self.entry_building = Entry(self.root)
        
        self.entry_room = Entry(self.root)
        self.entry_daysOfWeek = Entry(self.root)
        self.entry_startTime = Entry(self.root)
        self.entry_duration = Entry(self.root)
        self.entry_semesterCredit = Entry(self.root)
        self.entry_year = Entry(self.root)
        
        self.entry_instructionType = Entry(self.root)
        self.entry_item_15 = Entry(self.root)
        self.entry_item_16 = Entry(self.root)
        self.entry_item_17 = Entry(self.root)
        self.entry_item_18 = Entry(self.root)
        self.entry_item_19 = Entry(self.root)
        
        # Functionality Buttons
        self.button_clear = Button(self.root, text="Clear Table", command=self.clear_table, width=button_width)
        self.button_clear_ent = Button(self.root, text="Clear Entries", command=self.clear_entries, width=button_width)
        self.button_add = Button(self.root, text="Add Record", command=self.add_record)
        self.button_delete = Button(self.root, text="Delete Record", command=self.delete_record)
        self.button_view = Button(self.root, text="View All Records", command=self.view_records)
        self.button_modify = Button(self.root, text="Modify Record", command=self.modify_record)

        # Grid layout for data entry/label widgets
        # First Column
        self.label_recordCode.grid(row=2, column=5, sticky="e")
        self.label_institutionCode.grid(row=3, column=5, sticky="e")
        self.label_subject.grid(row=4, column=5, sticky="e")
        self.label_courseNumber.grid(row=5, column=5, sticky="e")
        self.label_sectionNumber.grid(row=6, column=5, sticky="e")
        self.label_building.grid(row=7, column=5, sticky="e")
        
        self.entry_recordCode.grid(row=2, column=6, sticky="w")
        self.entry_instituitionCode.grid(row=3, column=6, sticky="w")
        self.entry_subject.grid(row=4, column=6, sticky="w")
        self.entry_courseNumber.grid(row=5, column=6, sticky="w")
        self.entry_sectionNumber.grid(row=6, column=6, sticky="w")
        self.entry_building.grid(row=7, column=6, sticky="w")
        
        # Second Column
        self.label_room.grid(row=2, column=7, sticky="e")
        self.label_daysOfWeek.grid(row=3, column=7, sticky="e")
        self.label_startTime.grid(row=4, column=7, sticky="e")
        self.label_duration.grid(row=5, column=7, sticky="e")
        self.label_semesterCredit.grid(row=6, column=7, sticky="e")
        self.label_year.grid(row=7, column=7, sticky="e")
        
        self.entry_room.grid(row=2, column=8, sticky="w")
        self.entry_daysOfWeek.grid(row=3, column=8, sticky="w")
        self.entry_startTime.grid(row=4, column=8, sticky="w")
        self.entry_duration.grid(row=5, column=8, sticky="w")
        self.entry_semesterCredit.grid(row=6, column=8, sticky="w")
        self.entry_year.grid(row=7, column=8, sticky="w")
        
        # Third Column
        self.label_instructionType.grid(row=2, column=9, sticky="e")
        self.label_item15.grid(row=3, column=9, sticky="e")
        self.label_item16.grid(row=4, column=9, sticky="e")
        self.label_item17.grid(row=5, column=9, sticky="e")
        self.label_item18.grid(row=6, column=9, sticky="e")
        self.label_item19.grid(row=7, column=9, sticky="e")
        
        self.entry_instructionType.grid(row=2, column=10, sticky="w")
        self.entry_item_15.grid(row=3, column=10, sticky="w")
        self.entry_item_16.grid(row=4, column=10, sticky="w")
        self.entry_item_17.grid(row=5, column=10, sticky="w")
        self.entry_item_18.grid(row=6, column=10, sticky="w")
        self.entry_item_19.grid(row=7, column=10, sticky="w")
        
        # Functionality Buttons
        self.button_clear.grid(row=2, column=2, sticky="w")
        self.button_clear_ent.grid(row=3, column=2, sticky="w")
        self.button_view.grid(row=2, column=3, sticky="w")
        self.button_add.grid(row=2, column=4, sticky="we")
        self.button_delete.grid(row=3, column=4, sticky="we")
        self.button_modify.grid(row=4, column=4, sticky="we")

    # This method is used specifically for the search box and drop down menu
    # The method is essential for searching for specific records (or groups of records)
    def create_search_widgets(self):
        self.label_column = Label(self.root, text="Select From:")
        
        # Mapping for more user friendly search terms
        self.column_mapping = {"Subject": "subject", "Course Number": "course_num", "Record Code": "record_code", "Institution Code": "inst_code", "Subject": "subject", "Course Number": "course_num", "Section Number": "section_num", "Unused": "unused", "Building": "building", "Room": "room","Days of Week": "days", "Start Time": "time", "Duration": "duration", "Semester": "semester", "Year": "year", "Room Type": "room_type"}
        self.column_names = list(self.column_mapping.keys())  # Display names for the dropdown
        self.column_var = StringVar()
        self.column_combobox = ttk.Combobox(self.root, textvariable=self.column_var, values=self.column_names)
        self.column_combobox.set(self.column_names[0])  # Set the default column
        self.label_search = Label(self.root, text="Search For:")
        self.entry_search = Entry(self.root)
        self.button_search = Button(self.root, text="Search", command=self.search_records)

        # Grid layout for search widgets
        self.label_column.grid(row=2, column=0, sticky="e")
        self.column_combobox.grid(row=2, column=1, sticky="nsew")
        self.label_search.grid(row=3, column=0, sticky="e")
        self.entry_search.grid(row=3, column=1, sticky="nsew")
        self.button_search.grid(row=4, column=1, stick="nsew")

    # This method is used for displaying the table itself, essentially the core component of the GUI
    def create_treeview(self):
        self.treeview = ttk.Treeview(self.root, columns=("Record Code", "Institution Code", "Subject", "Course Number", "Section Number", "Unused", "Building", "Room",
                                                        "Days of Week", "Start Time", "Duration", "Semester", "Year", "Room Type", "Enrollment A", "Enrollment B", "Enrollment C", "Enrollment D", "Enrollment E"), show="headings")
    
        # Automatically set headings for the rest of the columns
        for column_name in self.treeview["columns"][0:]:
            self.treeview.heading(column_name, text=column_name)
    
        # Create a vertical scrollbar
        yscrollbar = Scrollbar(self.root, orient="vertical", command=self.treeview.yview)
        self.treeview.config(yscrollcommand=yscrollbar.set)
    
        # Create a horizontal scrollbar
        xscrollbar = Scrollbar(self.root, orient="horizontal", command=self.treeview.xview)
        self.treeview.config(xscrollcommand=xscrollbar.set)    
    
        # Place the items into the GUI
        self.treeview.grid(row=0, column=0, columnspan=11, sticky="nsew")
        yscrollbar.grid(row=0, column=11, sticky="ns")
        xscrollbar.grid(row=1, column=0, columnspan=11, stick="ew")
    
        # Configure column and row weights to make the table and columns expand with the window
        for i in range(11):
            self.root.columnconfigure(i, weight=1)
    
        # Set a higher weight for the row containing the Treeview
        self.root.rowconfigure(0, weight=1)  # You can adjust the weight as needed
    
        # Bind the Treeview to a function that will handle record selection
        self.treeview.bind("<ButtonRelease-1>", self.select_record)

    # This is a simple method that was used to be implemented into other methods
    # We were originally having issues with the table not updating values in real time, this solves that problem
    def refresh_table(self):
        # Clear the table
        for record in self.treeview.get_children():
            self.treeview.delete(record)
    
        # Fetch and store the updated records
        self.fetch_original_records()
    
        # Repopulate the table with the updated records
        for record in self.original_records:
            self.treeview.insert("", "end", values=record)

    # Another simple method that clears the entry fields and is incorporated into other methods to reduce redundant code
    def clear_entries(self):
        # Clear the entry fields with this method
        self.entry_recordCode.delete(0, END)
        self.entry_instituitionCode.delete(0, END)
        self.entry_subject.delete(0, END)
        self.entry_courseNumber.delete(0, END)
        self.entry_sectionNumber.delete(0, END)
        self.entry_building.delete(0, END)
            
        self.entry_room.delete(0, END)
        self.entry_daysOfWeek.delete(0, END)
        self.entry_startTime.delete(0, END)
        self.entry_duration.delete(0, END)
        self.entry_semesterCredit.delete(0, END)
        self.entry_year.delete(0, END)
            
        self.entry_instructionType.delete(0, END)
        self.entry_item_15.delete(0, END)
        self.entry_item_16.delete(0, END)
        self.entry_item_17.delete(0, END)
        self.entry_item_18.delete(0, END)
        self.entry_item_19.delete(0, END)
    
    # This method is used for adding records to the table, it was fit to handle the "unused" column
    # It also features built-in error detection to handle certain cases as specified in the documentation
    def add_record(self):
        # Get the new values from the entry fields
        new_record_values = [
            self.entry_recordCode.get(),
            self.entry_instituitionCode.get(),
            self.entry_subject.get(),
            self.entry_courseNumber.get(),
            self.entry_sectionNumber.get(),
            "",  # Empty string for the sixth column ("Unused")
            self.entry_building.get(),
            self.entry_room.get(),
            self.entry_daysOfWeek.get(),
            self.entry_startTime.get(),
            self.entry_duration.get(),
            self.entry_semesterCredit.get(),
            self.entry_year.get(),
            self.entry_instructionType.get(),
            self.entry_item_15.get(),
            self.entry_item_16.get(),
            self.entry_item_17.get(),
            self.entry_item_18.get(),
            self.entry_item_19.get()
        ]
    
        # Check for empty entries (except 'unused')
        for value in new_record_values[:5] + new_record_values[6:]:
            if not value and value != "unused":
                messagebox.showerror("Error", "Please fill in all fields.")
                return
    
        # Check if a record with the same section_num already exists
        cursor = self.db.cursor()
        query = "SELECT * FROM cbm005_table WHERE section_num = %s"
        cursor.execute(query, (self.entry_sectionNumber.get(),))
        existing_record = cursor.fetchone()
        cursor.close()
    
        if existing_record:
            messagebox.showerror("Error", "A record with the same Section Number already exists.")
        else:
            # Insert the new record into the database
            cursor = self.db.cursor()
            query = """
            INSERT INTO cbm005_table
            (record_code, inst_code, subject, course_num, section_num, unused, building, room, days, time, duration, semester, year, room_type, item_15, item_16, item_17, item_18, item_19)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, tuple(new_record_values))
            self.db.commit()
            cursor.close()
    
            # Update the Treeview with the new record
            self.treeview.insert("", "end", values=new_record_values)
    
            self.clear_entries()
            
            # Clear the table
            for record in self.treeview.get_children():
                self.treeview.delete(record)
        
            # Fetch and store the updated records
            self.fetch_original_records()
        
            # Repopulate the table with the updated records
            for record in self.original_records:
                self.treeview.insert("", "end", values=record)
    
            messagebox.showinfo("Success", "Record was successfully added!")

    # This method to delete the selected record from the table
    # It also features built-in error detection to handle certain cases as specified in the documentation
    def delete_record(self):
        # Get the selected item in the treeview
        selected_item = self.treeview.selection()
        
        if selected_item:
            # Confirm with the user before deleting
            confirmation = messagebox.askyesno("Delete Record", "Are you sure you want to delete the selected record?")
            
            if confirmation:
                # Get the section number from the selected item
                section_num = self.treeview.item(selected_item, "values")[4]
                
                # Delete the record from the database
                cursor = self.db.cursor()
                delete_query = "DELETE FROM cbm005_table WHERE section_num = %s"
                cursor.execute(delete_query, (section_num,))
                self.db.commit()
                cursor.close()
                
                # Remove the selected item from the treeview
                self.treeview.delete(selected_item)
                
                self.refresh_table()
                
                messagebox.showinfo("Success", "Record was successfully deleted!")
        else:
            messagebox.showwarning("Warning", "Please select a record to delete.")

    # While this method was not explicitly required, we felt it was best if the user could display all records at once
    def view_records(self):
        # Clear the table
        for record in self.treeview.get_children():
            self.treeview.delete(record)

         # Repopulate the table with the original records
        for record in self.original_records:
            self.treeview.insert("", "end", values=record)
            
    # This method is an extension of the search section where the user can click a button to perform the search
    def search_records(self):
        cursor = self.db.cursor()
        selected_display_name = self.column_var.get()  # Get the selected user-friendly column name
        selected_column = self.column_mapping[selected_display_name]  # Map to actual column name
        search_value = self.entry_search.get()  # Get the search value from the entry field
        query = f"SELECT * FROM cbm005_table WHERE {selected_column} = %s"
        cursor.execute(query, (search_value,))
        records = cursor.fetchall()
    
        for record in self.treeview.get_children():
            self.treeview.delete(record)
    
        for record in records:
            self.treeview.insert("", "end", values=record)
        cursor.close()
      
    # This is another simple method for retrieving updated records which is built-in into other methods
    def fetch_original_records(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM cbm005_table")
        self.original_records = cursor.fetchall()
        cursor.close()
        
    # Very simple method similar to the clear_entries() method that is used for clearing the table
    # It is its own button, however, it also gets built-in into other methods for its functionality
    def clear_table(self):
        for record in self.treeview.get_children():
            self.treeview.delete(record)
        # Clear Entries    
        self.clear_entries()
        
        messagebox.showinfo("Success", "Table was successfully cleared!")
        
    # This is a simple yet extremely useful button, it is the foundation for both modify and delete record
    def select_record(self, event):
        item = self.treeview.selection()[0]
        record_values = self.treeview.item(item, "values")
        
        # Clear values inside the boxes for selected records
        self.clear_entries()
    
        # Set the entry fields with the selected record values
        self.entry_recordCode.insert(0, record_values[0])
        self.entry_instituitionCode.insert(0, record_values[1])
        self.entry_subject.insert(0, record_values[2])
        self.entry_courseNumber.insert(0, record_values[3])
        self.entry_sectionNumber.insert(0, record_values[4])
        self.entry_building.insert(0, record_values[6])

        self.entry_room.insert(0, record_values[7])
        self.entry_daysOfWeek.insert(0, record_values[8])
        self.entry_startTime.insert(0, record_values[9])
        self.entry_duration.insert(0, record_values[10])
        self.entry_semesterCredit.insert(0, record_values[11])
        self.entry_year.insert(0, record_values[12])
        
        self.entry_instructionType.insert(0, record_values[13])
        self.entry_item_15.insert(0, record_values[14])
        self.entry_item_16.insert(0, record_values[15])
        self.entry_item_17.insert(0, record_values[16])
        self.entry_item_18.insert(0, record_values[17])
        self.entry_item_19.insert(0, record_values[18])
    
    # This method is used for modifying the selected record
    # It also features built in error detection to handle certain cases as specified in the documentation       
    def modify_record(self):
        selected_item = self.treeview.selection()
        if selected_item:
            item = selected_item[0]  # Get the first selected item
            selected_record_values = self.treeview.item(item, "values")
    
            # Get the new values from the entry fields
            new_section_num = self.entry_sectionNumber.get()
            if new_section_num != selected_record_values[4]:  # Check if the section_num is being modified
                if self.record_exists(new_section_num):
                    messagebox.showerror("Error", "A record with the same Section Number already exists.")
                    return
    
            new_record_values = [
                self.entry_recordCode.get(),
                self.entry_instituitionCode.get(),
                self.entry_subject.get(),
                self.entry_courseNumber.get(),
                new_section_num,
                "",  # Empty because column 'Unused' is not needed
                self.entry_building.get(),
                self.entry_room.get(),
                self.entry_daysOfWeek.get(),
                self.entry_startTime.get(),
                self.entry_duration.get(),
                self.entry_semesterCredit.get(),
                self.entry_year.get(),
                self.entry_instructionType.get(),
                self.entry_item_15.get(),
                self.entry_item_16.get(),
                self.entry_item_17.get(),
                self.entry_item_18.get(),
                self.entry_item_19.get()
            ]
    
            # Update the record in the Treeview
            self.treeview.item(item, values=new_record_values)
    
            # Update the record in the database
            cursor = self.db.cursor()
            update_query = """
            UPDATE cbm005_table
            SET record_code = %s, inst_code = %s, subject = %s, course_num = %s, section_num = %s, unused = %s, building = %s,
                room = %s, days = %s, time = %s, duration = %s, semester = %s, year = %s, room_type = %s,
                item_15 = %s, item_16 = %s, item_17 = %s, item_18 = %s, item_19 = %s
            WHERE section_num = %s
            """
            cursor.execute(update_query, tuple(new_record_values + [selected_record_values[4]]))
            self.db.commit()
            cursor.close()
    
            # Clear the entry fields after modification
            self.clear_entries()
            self.refresh_table()
    
            messagebox.showinfo("Success", "Record was successfully modified!")
        else:
            messagebox.showwarning("Warning", "Please select a record to modify.")
    
    # This method is an extension to the modify_record() method
    # It was created because we had difficulties inplementing the SQL code to ensure the button also modified the database
    def record_exists(self, section_num):
        cursor = self.db.cursor()
        query = "SELECT * FROM cbm005_table WHERE section_num = %s"
        cursor.execute(query, (section_num,))
        existing_record = cursor.fetchone()
        cursor.close()
        return existing_record is not None

# Intialization Code
if __name__ == "__main__":
    root = Tk()
    app = DatabaseGUI(root)
    root.mainloop()