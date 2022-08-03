# dyvenia
## How to generate new tasks for database?

0. Obtain the mighty Excel file `InterviewTasks` - from Laura or others in the company
1. Download `InterviewTasks.csv` file from excel sheet (remember to change the name to `InterviewTasks` and save it as `.csv` file!)
2. Paste the file into this directory (`dyvenia/kb/dyvenia/InterviewTassk.csv`)
3. Run `update_database.py` script, by either pressing the `play` button in VSCode or run it in console with python:
```
python3 path/to/the/file/update_database.py
```
4. If any error occurs, it should print it. When successfully inserted, will inform by printing
```
Successfully inserted X rows!
```
