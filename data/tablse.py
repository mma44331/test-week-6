import sqlite3


conn = sqlite3.connect("Base.db", check_same_thread=False)
cursor = conn.cursor()


table_room = """CREATE TABLE IF NOT EXISTS Rooms (
        id INTEGER PRIMARY KEY,
        Number_of_beds int NOT NULL,
        turned_beds int NOT NULL
    );"""

table_soldier = """CREATE TABLE IF NOT EXISTS Soldier (
        personal_number INTEGER PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL,
        gender text NOT NULL,
        city int NOT NULL,
        distance text NOT NULL,
        placement_status int NOT NULL
        );"""




def create_table_room(table_room):
    cursor.execute(table_room)
    conn.commit()

def create_table_soldier(table_soldier):
    cursor.execute(table_soldier)
    conn.commit()

create_table_room(table_room)
create_table_soldier(table_soldier)

def insert_soldier_to_table(data:list):
    for row in data:
        cursor.execute(
            "INSERT INTO Soldier(personal_number, first_name, last_name, gender, city, distance, placement_status) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (row[0], row[1], row[2], row[3], row[4], row[5],"niy"))
        conn.commit()

def insert_room_to_table():
    cursor.execute(
        "INSERT INTO Rooms(id, Number_of_beds, turned_beds) VALUES(?, ?, ?)",
        (36, 8, 8))
    conn.commit()


cursor.execute("SELECT * FROM Soldier")
print(cursor.fetchall())
