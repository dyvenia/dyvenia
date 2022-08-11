import sqlite3
import random
from IPython.display import display, Markdown, Latex

def connect_to_generator(task_level, task_type, amount):
    try:
        if task_type == "SQL":
            display(Markdown(f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"))
        con = sqlite3.connect('interview.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Tasks WHERE LEVEL == '{task_level}' AND TYPE == '{task_type}'")
        tasks = cur.fetchall()
        if amount > len(tasks):
            return tasks
        else: 
            return random.sample(tasks, amount)
    except ValueError:
            pass
