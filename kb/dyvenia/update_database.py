from multiprocessing.sharedctypes import Value
import sqlite3
import csv

con = sqlite3.connect("../recruitment/interview.db")
cur = con.cursor()

table_exists = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Tasks'")

if table_exists.fetchall():
    cur.execute("DROP TABLE Tasks")

tasks_file = open("InterviewTasks.csv")
task = csv.reader(tasks_file)

try:
    cur.execute("CREATE TABLE Tasks (LEVEL varchar(255), TYPE varchar(255), TASK varchar(1000))")
    cur.executemany("INSERT INTO Tasks VALUES (?, ?, ?)", task)
    if cur.rowcount > 0:
        print(f"Successfully inserted {cur.rowcount} rows!")
        con.commit()
        con.close()

    else:
        raise ValueError(f"Table was not updated.")
except BaseException as e:
    print(f"Could not update the table. \nERROR: {e}")


