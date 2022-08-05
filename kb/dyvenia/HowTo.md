# dyvenia
## How to generate new tasks for database?

0. Obtain the mighty Excel file [InterviewTasks](https://docs.google.com/spreadsheets/d/1vVRuPR-BHYjxkFpO_RTpTpiEg3ptRjj5-D_xXtCl4eE/edit?usp=sharing)
1. Download `InterviewTasks.csv` file from excel sheet (remember to change the name to `InterviewTasks` and save it as `.csv` file!)
2. Paste the file into this directory (`dyvenia/kb/dyvenia/InterviewTask.csv`)
3. Run `update_database.py` script, by either pressing the `play` button in VSCode or run it in console with python. <br>
**Note:** Make sure you are in the project directory!
```
python3 kb/dyvenia/update_database.py
```
4. If any error occurs, it should print it. When successfully inserted, will inform by printing
```
Successfully inserted X rows!
```
5. Push the updated database to the repository! Location of the database:
```
dyvenia/recruitment/interview.db
```
