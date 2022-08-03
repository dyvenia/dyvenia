import sqlite3
import random

def connect_to_generator(task_level, task_type, amount):
    con = sqlite3.connect('interview.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM Tasks WHERE LEVEL == '{task_level}' AND TYPE == '{task_type}'")
    tasks = cur.fetchall()
    return random.sample(tasks, amount)
