# Database_GUI

**Authors:** Leo Martinez III - [LinkedIn](https://www.linkedin.com/in/leo-martinez-iii/)

**Contact:** [leo.martinez@students.tamuk.edu](mailto:leo.martinez@students.tamuk.edu)

**Created:** Fall 2023

---

This Python program provides a graphical user interface (GUI) for interacting with a MySQL database. The application allows users to perform various operations such as adding, modifying, deleting, viewing, and searching records in the database. The GUI is designed using the Tkinter library, and the program utilizes the MySQL Connector for database connectivity.

### Features:

- Data Entry Widgets: Create and manage records with labeled entry fields for each database column.
- Functionality Buttons: Clear Table, Clear Entries, Add Record, Delete Record, View All Records, and Modify Record.
- Search Functionality: Users can search for specific records based on selected criteria.
- Treeview Display: A tabular view of database records with horizontal and vertical scrollbars for better navigation.

### Usage:

- Set up the MySQL database connection details (host, user, password, database) in the `connect_to_db` method.
- Enter your database columns and labels in the `create_data_entry_widgets` method.
- Run the program, and the GUI will provide an interactive environment to manage your MySQL database.

### Data utilized:

- CBM005.txt Data File

### Note:

- Program was created in Spyder 5.2.2 Anaconda with Python 3.9

---

**Folder Contents:**

- **src:** Folder containing the source code python script: `database_gui.py` (use this file to run the program)
- **data:** Contains the exported SQL self-contained file from MySQL Workbench and the data that was used for the program along with an SQL Query script used to import the data into the Schema.
- **README.md:** Contains the most basic information about the project
- **LICENSE:** Contains license information in regards to the Github repository

---

**Additional Information:**

- Everything needed along with additional installation information to run the program will be contained in this folder.
- Please ensure the **Tkinter** and **MySQL Connector** python libraries are installed before running.
