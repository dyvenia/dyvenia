from IPython.display import display, Markdown, Latex

def error_check(ROLE, LEVEL, AMOUNT_OF_SQL_QUESTIONS, AMOUNT_OF_PYTHON_QUESTIONS):
      if ROLE == "" or LEVEL == "" :
        [display(Markdown('''<div class="alert alert-block alert-danger"> ERROR: Choose correct options </div>'''))]
      if AMOUNT_OF_SQL_QUESTIONS <= 0 and AMOUNT_OF_PYTHON_QUESTIONS <= 0: 
          [display(Markdown('''<div class="alert alert-block alert-danger"> <b><i>ERROR</i>: Any questions were chosen.<br> <i>Action needed</i>: modify AMOUNT_OF_SQL_QUESTIONS and AMOUNT_OF_PYTHON_QUESTIONS </b> </div>'''))]
      elif AMOUNT_OF_SQL_QUESTIONS <= 0 : 
          [display(Markdown('''<div class="alert alert-block alert-danger"> <b>WARNING</b>: Any SQL questions were chosen. If you want to change it, modify AMOUNT_OF_SQL_QUESTIONS </div>'''))]
      elif AMOUNT_OF_PYTHON_QUESTIONS <= 0 : 
          [display(Markdown('''<div class="alert alert-block alert-danger"> <b>WARNING</b>: Any PYTHON questions were chosen. If you want to change it, modify AMOUNT_OF_SQL_QUESTIONS </div>'''))] 
       