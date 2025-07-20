import sqlite3
import datetime

DB_FILE = 'attendance.db'

def initialize_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employee (
                    emp_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                    date TEXT,
                    emp_id TEXT,
                    name TEXT,
                    status TEXT,
                    PRIMARY KEY(date, emp_id))''')
    conn.commit()
    conn.close()

def add_employee(emp_id, name):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO employee (emp_id, name) VALUES (?, ?)", (emp_id, name))
        conn.commit()
        message = "Employee added successfully!"
    except sqlite3.IntegrityError:
        message = "Employee ID already exists!"
    conn.close()
    return message

def mark_attendance(attendance_dict):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT emp_id, name FROM employee")
    employees = dict(c.fetchall())
    
    date = datetime.date.today().isoformat()
    for emp_id, name in employees.items():
        status = attendance_dict.get(emp_id, 'A').upper()
        if status not in ['P', 'A']:
            status = 'A'
        try:
            c.execute("INSERT INTO attendance (date, emp_id, name, status) VALUES (?, ?, ?, ?)",
                      (date, emp_id, name, status))
            conn.commit()
        except sqlite3.IntegrityError:
            pass
    conn.close()
    return "Attendance marked."

def view_today_attendance():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    date = datetime.date.today().isoformat()
    c.execute("SELECT name, emp_id, status FROM attendance WHERE date=?", (date,))
    records = c.fetchall()
    output = f"Attendance for {date}:\n"
    if records:
        for record in records:
            output += f"{record[0]} ({record[1]}): {record[2]}\n"
    else:
        output += "No attendance found for today."
    conn.close()
    return output

def view_attendance_report(emp_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT date, status FROM attendance WHERE emp_id=?", (emp_id,))
    records = c.fetchall()
    output = f"Attendance report for Employee ID {emp_id}:\n"
    if records:
        for record in records:
            output += f"Date: {record[0]}, Status: {record[1]}\n"
    else:
        output += "No records found."
    conn.close()
    return output

def run_tests():
    initialize_db()
    print(add_employee("E001", "John Doe"))
    print(add_employee("E002", "Jane Smith"))
    print(add_employee("E003", "Eion Smith"))
    attendance_data = {"E001": "P", "E002": "A"}
    print(mark_attendance(attendance_data))
    print(view_today_attendance())
    print(view_attendance_report("E001"))
    print(view_attendance_report("E002"))

if __name__ == "__main__":
    run_tests()
