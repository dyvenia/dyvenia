import sqlite3
import random
from IPython.display import display, Markdown, Latex


def connect_to_generator(task_role, task_level, task_type, amount):
    try:
        if task_role == "DA" and task_level == "JUNIOR" and task_type == "SQL":
            display(
                Markdown(
                    f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"
                )
            )
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DA-SQL-JR'")
            tasks = cur.fetchall()
        elif task_role == "DA" and task_level == "MID" and task_type == "SQL":
            display(
                Markdown(
                    f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"
                )
            )
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DA-SQL-MID'")
            tasks = cur.fetchall()
        elif (
            task_role == "DA" and task_level == "SENIOR" and task_type == "SQL"
        ):
            display(
                Markdown(
                    f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"
                )
            )
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DA-SQL-SR'")
            tasks = cur.fetchall()
        elif (
            task_role == "DA"
            and task_level == "JUNIOR"
            and task_type == "PYTHON"
        ):
            # display(Markdown(f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"))
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DA-PY-JR'")
            tasks = cur.fetchall()
        elif (
            task_role == "DA" and task_level == "MID" and task_type == "PYTHON"
        ):
            # display(Markdown(f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"))
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DA-PY-MID'")
            tasks = cur.fetchall()
        elif (
            task_role == "DA"
            and task_level == "SENIOR"
            and task_type == "PYTHON"
        ):
            # display(Markdown(f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"))
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DA-PY-SR'")
            tasks = cur.fetchall()
        if task_role == "DE" and task_level == "JUNIOR" and task_type == "SQL":
            display(
                Markdown(
                    f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"
                )
            )
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DE-SQL-JR'")
            tasks = cur.fetchall()
        elif task_role == "DE" and task_level == "MID" and task_type == "SQL":
            display(
                Markdown(
                    f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"
                )
            )
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DE-SQL-MID'")
            tasks = cur.fetchall()
        elif (
            task_role == "DE" and task_level == "SENIOR" and task_type == "SQL"
        ):
            display(
                Markdown(
                    f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"
                )
            )
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DE-SQL-SR'")
            tasks = cur.fetchall()
        elif (
            task_role == "DE"
            and task_level == "JUNIOR"
            and task_type == "PYTHON"
        ):
            # display(Markdown(f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"))
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DE-PY-JR'")
            tasks = cur.fetchall()
        elif (
            task_role == "DE" and task_level == "MID" and task_type == "PYTHON"
        ):
            # display(Markdown(f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"))
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DE-PY-MID'")
            tasks = cur.fetchall()
        elif (
            task_role == "DE"
            and task_level == "SENIOR"
            and task_type == "PYTHON"
        ):
            # display(Markdown(f"![img](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)<br>"))
            con = sqlite3.connect("interview.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM Tasks WHERE CAT == 'DE-PY-SR'")
            tasks = cur.fetchall()
        if amount > len(tasks):
            return tasks
        else:
            return random.sample(tasks, amount)
    except ValueError:
        pass
